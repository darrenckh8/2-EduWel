import board
import time
import array
import audiobusio
import neopixel

# Initialize PDM Microphone - maximum speed settings
mic = audiobusio.PDMIn(board.GP3, board.GP2, sample_rate=16000, bit_depth=16)
# Much smaller buffer for maximum speed
SAMPLE_SIZE = 256  # Minimal size for speed
samples = array.array('H', [0] * SAMPLE_SIZE)

# Initialize NeoPixel Strip (using 5 LEDs for spectrum display)
num_pixels = 5
pixel_pin = board.GP14
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.4, auto_write=False)

# Ultra-fast spectrum configuration
FREQUENCY_BINS = num_pixels
MAX_MAGNITUDE = 10000  # Maximum audio level (LOWER = more sensitive)
MIN_MAGNITUDE = 100    # Minimum threshold to show (LOWER = more sensitive)
NOISE_GATE = 150      # Background noise filter (LOWER = more sensitive)

# Divide 256 samples into 5 frequency bands (~51 samples each)
BAND_SIZE = SAMPLE_SIZE // FREQUENCY_BINS  # ~51 samples per band

# Color palette for 5-LED spectrum (from low to high frequency)
SPECTRUM_COLORS = [
    (255, 0, 255),    # Magenta - Low bass (0-500 Hz)
    (0, 0, 255),      # Blue - Bass/Low mid (500-1500 Hz)
    (0, 255, 255),    # Cyan - Mid range (1500-3000 Hz)
    (0, 255, 0),      # Green - High mid (3000-5000 Hz)
    (255, 255, 0),    # Yellow - High frequencies (5000+ Hz)
]


def spectrum(samples):

    frequency_magnitudes = []

    # Process each frequency band
    for band in range(FREQUENCY_BINS):
        start_idx = band * BAND_SIZE
        # Ensure we don't exceed sample array
        end_idx = min(start_idx + BAND_SIZE, len(samples))

        # Get samples for this band
        band_samples = samples[start_idx:end_idx]

        if len(band_samples) == 0:
            frequency_magnitudes.append(0)
            continue

        # Energy calculation
        # Calculate center value
        center = sum(band_samples) // len(band_samples)
        energy = 0

        for sample in band_samples:
            diff = sample - center
            energy += diff * diff if diff > 0 else -diff * diff

        # Scale energy based on actual band size
        scaled_energy = energy >> 12  # Adjust scaling for larger bands
        if scaled_energy < NOISE_GATE:
            scaled_energy = 0

        frequency_magnitudes.append(scaled_energy)

    return frequency_magnitudes


def brightness(magnitude):

    if magnitude <= MIN_MAGNITUDE:
        return 0

    # Fast integer scaling - no floating point
    if magnitude >= MAX_MAGNITUDE:
        return 255

    # Simple linear mapping with bit shifting
    brightness = ((magnitude - MIN_MAGNITUDE) *
                  255) // (MAX_MAGNITUDE - MIN_MAGNITUDE)

    # Clamp to valid range
    return min(255, max(0, brightness))


def display(frequency_magnitudes):
    for i in range(num_pixels):
        magnitude = frequency_magnitudes[i] if i < len(
            frequency_magnitudes) else 0

        if magnitude > MIN_MAGNITUDE:
            # Brightness calculation
            led_brightness = brightness(magnitude)

            if led_brightness > 5:  # Skip very dim LEDs
                # Get base color and scale with bit operations
                base_color = SPECTRUM_COLORS[i]
                pixels[i] = (
                    (base_color[0] * led_brightness) >> 8,
                    (base_color[1] * led_brightness) >> 8,
                    (base_color[2] * led_brightness) >> 8
                )
            else:
                pixels[i] = (0, 0, 0)
        else:
            pixels[i] = (0, 0, 0)

    pixels.show()


# Simple peak hold array
peak_hold = [0] * num_pixels

while True:
    try:
        # Record audio samples
        mic.record(samples, len(samples))

        # Ultra-fast frequency analysis
        frequency_magnitudes = spectrum(samples)

        # Simple peak hold with decay
        for i in range(len(frequency_magnitudes)):
            if i < len(peak_hold):
                if frequency_magnitudes[i] > peak_hold[i]:
                    peak_hold[i] = frequency_magnitudes[i]
                else:
                    # Decay using bit shift (equivalent to multiply by ~0.9)
                    peak_hold[i] = (peak_hold[i] * 230) >> 8
                frequency_magnitudes[i] = peak_hold[i]

        # Update LEDs
        display(frequency_magnitudes)

    except Exception as e:
        # Quick error indication
        pixels.fill((255, 0, 0))
        pixels.show()
