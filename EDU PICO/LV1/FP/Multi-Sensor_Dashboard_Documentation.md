# Multi-Sensor Dashboard - Final Project (Level 1)

## 🎯 Project Goal

Create a comprehensive **multi-sensor monitoring system** using a Raspberry Pi Pico that displays real-time environmental data, proximity detection, color sensing, and control inputs on an OLED screen with interactive navigation and audio feedback.

## 📋 What Students Need to Build

### **Requirements:**

#### **🖥️ Multi-Screen Display System**
Students must implement **three distinct screens** that cycle through different sensor data:

**Screen 1 - Environment Monitor:**
- Display current temperature in Celsius
- Show humidity percentage
- Monitor sound level in decibels
- Include visual indicators and clear labels

**Screen 2 - Proximity & Color Detection:**
- Show distance readings from proximity sensor
- Detect and display dominant color (Red/Green/Blue/Mixed)
- Display RGB values in readable format
- Real-time updates as objects change

**Screen 3 - Controls & Input Status:**
- Show potentiometer position as percentage
- Display potentiometer level as visual progress bar
- Show current button states (Pressed/Released)
- Real-time control feedback

#### **🎛️ User Interface Controls**
Students must implement intuitive navigation:

**Button A (Screen Navigation):**
- Press to cycle through screens: 1 → 2 → 3 → 1
- Provide audio feedback (buzzer) on each press
- Display current screen number (e.g., "[2/3]")
- Smooth transitions between screens

**Button B (System Interaction):**
- Trigger buzzer test sounds
- Provide different audio patterns for variety
- Audio confirmation for user actions

**Visual Status Indicators:**
- NeoPixel LED changes color based on sensor readings:
  - **Red:** Object very close (proximity > 100)
  - **Orange:** High temperature (> 30°C)
  - **Blue:** High potentiometer setting (> 80%)
  - **Green:** Normal operation status

## 📋 Components List

### **Required Hardware:**

| Component | Quantity | Chapter Reference | Purpose |
|-----------|----------|-------------------|---------|
| Raspberry Pi Pico | 1 | All | Main microcontroller |
| OLED Display (128x64, I2C) | 1 | Chapter 15 | Visual data display |
| Temperature/Humidity Sensor (AHT20) | 1 | Chapters 7 & 8 | Environmental monitoring |
| Color/Proximity Sensor (APDS9960) | 1 | Chapters 4 & 5 | Color detection & distance sensing |
| PDM Microphone | 1 | Chapter 9 | Sound level detection |
| Potentiometer | 1 | Chapter 2 | Analog input control |
| Push Buttons | 2 | Chapter 1 | User interface navigation |
| NeoPixel RGB LED | 1 | Chapter 3 | Status indication |
| Buzzer | 1 | Chapter 10 | Audio feedback |
