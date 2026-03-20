# CLI Task Manager (Interactive Python Application)

## Overview

This project is a command-line task management application implemented in Python. It provides a simple, interactive interface that allows users to create, view, and delete tasks. The application is designed to be lightweight, easy to understand, and suitable for educational or portfolio use.

The system uses a persistent storage mechanism based on a local JSON file, ensuring that tasks remain available across multiple executions of the program.

---

## Features

### Task Creation

* Users can input multiple tasks in a single session.
* Task entry continues until a blank line is submitted.

### Task Viewing

* Displays all current tasks in a structured, numbered format.
* Handles empty task lists gracefully.

### Task Deletion

* Tasks can be removed by selecting their corresponding number.
* Updates are immediately reflected in persistent storage.

### Persistent Storage

* Tasks are stored in a local `tasks.json` file.
* Data persists between program executions.

### Interactive Interface

* Menu-driven system for ease of use.
* Continuous execution loop until the user exits.

---

## Project Structure

```text
task-manager/
├── main.py
└── tasks.json
```

### File Descriptions

#### main.py

The primary application file. It contains:

* Core program logic
* Menu system
* Task manipulation functions
* File input/output handling

#### tasks.json

A JSON file used for persistent storage of tasks. It is automatically created when tasks are first saved.

Example structure:

```json
[
  "Complete assignment",
  "Review lecture notes",
  "Prepare for exam"
]
```

---

## Requirements

* Python 3.6 or higher
* No external libraries are required

---

## Installation and Setup

1. Ensure Python is installed on your system.
2. Place `main.py` in a directory of your choice.
3. Open a terminal or command prompt and navigate to the project directory.

---

## Execution

Run the application using:

```bash
python main.py
```

---

## Usage

### Main Menu

Upon execution, the application presents the following interface:

```text
Welcome to your Task Manager.

Choose an option:
1. Add tasks
2. View tasks
3. Delete a completed task
4. Exit
```

---

### Adding Tasks

Users can enter tasks sequentially:

```text
What tasks do you need to do?
Type one task at a time.
Press Enter on a blank line when you're done.

> Complete assignment
> Study Python
>
Tasks saved.
```

Each line corresponds to a new task. An empty input terminates the entry process.

---

### Viewing Tasks

Displays all stored tasks:

```text
Your tasks:
1. Complete assignment
2. Study Python
```

If no tasks exist:

```text
No tasks right now.
```

---

### Deleting Tasks

Users can remove tasks by selecting their index:

```text
Your tasks:
1. Complete assignment
2. Study Python

Enter the number of the task you finished: 1

Removed task: "Complete assignment"
```

Invalid inputs are handled with appropriate error messages.

---

### Exiting the Application

Selecting option 4 terminates the program:

```text
Goodbye.
```

---

## Technical Design

### Data Management

* Tasks are stored as a list of strings in a JSON file.
* The application loads tasks into memory at startup.
* Modifications are written back to the file immediately after changes.

### Core Functions

#### load_tasks()

* Reads task data from `tasks.json`.
* Returns an empty list if the file does not exist or is invalid.

#### save_tasks(tasks)

* Writes the current task list to the JSON file.
* Ensures data persistence.

#### add_tasks(tasks)

* Collects user input in a loop.
* Appends new tasks to the existing list.

#### show_tasks(tasks)

* Outputs tasks in a numbered format.
* Handles empty lists appropriately.

#### delete_task(tasks)

* Validates user input.
* Removes the selected task from the list.

#### main()

* Controls application flow.
* Implements the interactive loop and menu system.

---

## Error Handling

The application includes basic error handling mechanisms:

* Invalid numeric input when selecting tasks
* Out-of-range task indices
* Missing or corrupted JSON file
* Empty task list conditions

---

## Design Considerations

### Simplicity

The application prioritizes clarity and ease of understanding. It avoids unnecessary complexity, making it suitable for educational purposes.

### No External Dependencies

All functionality is implemented using Python’s standard library.

### Interactive Approach

The menu-driven interface was chosen over command-line arguments to provide a more guided user experience.

---

## Potential Enhancements

* Task completion status instead of deletion
* Task editing functionality
* Due dates and priority levels
* Search and filtering capabilities
* Terminal output formatting (e.g., color support)
* Conversion to a modular, multi-file architecture
* Packaging as an installable command-line tool

---

## Example Session

```text
Welcome to your Task Manager.

Choose an option:
1. Add tasks
2. View tasks
3. Delete a completed task
4. Exit

Enter your choice: 1

What tasks do you need to do?

> Study for exam
> Go to gym
>

Tasks saved.

Enter your choice: 2

Your tasks:
1. Study for exam
2. Go to gym

Enter your choice: 3

Enter the number of the task you finished: 1

Removed task: "Study for exam"
```

---

## Conclusion

This project demonstrates fundamental concepts in Python programming, including file handling, user input processing, and application control flow. It serves as a strong foundation for building more advanced command-line tools and reinforces best practices in structuring small-scale software projects.
