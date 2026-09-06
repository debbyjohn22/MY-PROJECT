"""
main.py
-------
Entry point for the To-Do List app. Handles the menu, user input,
and the main program loop. All task data logic lives in tasks.py.

Run with: python main.py
"""

from tasks import load_tasks, save_tasks, add_task, mark_done, delete_task


def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Quit")


def print_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Add one!")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['title']}")


def prompt_task_number(prompt_text):
    """Ask the user for a task number, return an int or None if invalid."""
    try:
        return int(input(prompt_text))
    except ValueError:
        print("Please enter a valid number.")
        return None


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            print_tasks(tasks)

        elif choice == "2":
            title = input("Enter the new task: ")
            if add_task(tasks, title):
                print(f"Added: '{title.strip()}'")
                save_tasks(tasks)
            else:
                print("Task can't be empty.")

        elif choice == "3":
            print_tasks(tasks)
            if tasks:
                index = prompt_task_number("Enter task number to mark as done: ")
                if index is not None:
                    task = mark_done(tasks, index)
                    if task:
                        print(f"Marked '{task['title']}' as done.")
                        save_tasks(tasks)
                    else:
                        print("Invalid task number.")

        elif choice == "4":
            print_tasks(tasks)
            if tasks:
                index = prompt_task_number("Enter task number to delete: ")
                if index is not None:
                    removed = delete_task(tasks, index)
                    if removed:
                        print(f"Deleted '{removed['title']}'.")
                        save_tasks(tasks)
                    else:
                        print("Invalid task number.")

        elif choice == "5":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
