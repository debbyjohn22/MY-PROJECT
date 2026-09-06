"""
tasks.py
--------
Handles everything related to task data:
- loading tasks from disk
- saving tasks to disk
- adding, completing, deleting tasks

Keeping this separate from main.py means the "data logic" doesn't
know or care how the menu looks — that's a core idea in clean code
called separation of concerns.
"""

import json
import os

TASKS_FILE = os.path.join(os.path.dirname(__file__), "data", "tasks.json")


def load_tasks():
    """Load tasks from the JSON file, or return an empty list if none exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Save the current list of tasks to the JSON file."""
    os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, title):
    """Add a new task. Returns True if added, False if title was empty."""
    title = title.strip()
    if not title:
        return False
    tasks.append({"title": title, "done": False})
    return True


def mark_done(tasks, index):
    """Mark the task at the given 1-based index as done. Returns the task or None."""
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        return tasks[index - 1]
    return None


def delete_task(tasks, index):
    """Remove the task at the given 1-based index. Returns the removed task or None."""
    if 1 <= index <= len(tasks):
        return tasks.pop(index - 1)
    return None
