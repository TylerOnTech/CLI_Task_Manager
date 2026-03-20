#!/usr/bin/env python3
import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks right now.\n")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()


def add_tasks(tasks):
    """Let the user enter tasks."""
    print("\nWhat tasks do you need to do?")
    print("Type one task at a time.")
    print("Press Enter on a blank line when you're done.\n")

    while True:
        task = input("> ").strip()
        if task == "":
            break
        tasks.append(task)

    save_tasks(tasks)
    print("\nTasks saved.\n")


def delete_task(tasks):
    """Delete a task by number."""
    if not tasks:
        print("\nNo tasks to delete.\n")
        return

    show_tasks(tasks)

    choice = input("Enter the number of the task you finished: ").strip()

    if not choice.isdigit():
        print("\nPlease enter a valid number.\n")
        return

    index = int(choice) - 1

    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f'\nRemoved task: "{removed}"\n')
    else:
        print("\nThat task number does not exist.\n")


def main():
    tasks = load_tasks()

    print("Welcome to your Task Manager.")

    while True:
        print("Choose an option:")
        print("1. Add tasks")
        print("2. View tasks")
        print("3. Delete a completed task")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("\nGoodbye.")
            break
        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
