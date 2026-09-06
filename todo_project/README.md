# CLI To-Do List

A simple command-line To-Do List app built as a beginner Python project.

## Features
- View, add, complete, and delete tasks
- Tasks persist between runs (saved to `data/tasks.json`)
- Clean separation between app logic (`tasks.py`) and the user interface (`main.py`)

## Project Structure
```
todo_project/
├── main.py          # entry point — menu and program loop
├── tasks.py         # task data logic (load, save, add, complete, delete)
├── data/
│   └── tasks.json   # auto-created on first save
├── README.md
└── .gitignore
```

## How to Run
```bash
python main.py
```

## What This Project Covers
- Variables & f-strings
- Loops and conditionals
- Functions
- Lists and dictionaries
- File I/O with JSON
- Splitting a program into multiple modules (`import`)

## Possible Next Steps
- Add due dates or priority levels to tasks
- Add task categories/tags
- Write unit tests for `tasks.py`
- Turn it into a package with `setup.py` or `pyproject.toml`
