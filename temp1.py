import easygui as eg
import json
from datetime import datetime

TASKS_FILE = "Python/tasks.json"  # File to store tasks

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
            return []


def format_relative_day(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    today = datetime.now()
    delta_days = (today - date_obj).days

    if delta_days == 0:
        return "Today"
    elif delta_days == 1:
        return "Yesterday"
    elif delta_days < 7:
        return f"Last {date_obj.strftime('%A')}"
    else:
        return date_obj.strftime("%B %d")


def todo_list():
    tasks = load_tasks()

    while True:
         task_display = "\n".join(f"{t['task']} (Added: {format_relative_day(t['timestamp'])})" for t in tasks) or "No tasks yet."

         choice = eg.buttonbox(f"Current Tasks:\n{task_display}\n\nChoose an action:",
                               "To-Do List Manager",
                               choices=["Add Task", "Remove Task", "Exit"])