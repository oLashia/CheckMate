# Check Mate

## Project Overview

Check Mate is a console based to-do list manager that allows users to create, view, modify, and manage multiple to-do lists and tasks interactively. The project is designed to provide a simple yet effective way to organize tasks, ensuring users can stay on top of their responsibilities. This project was developed as part of the CS50P final project to demonstrate the application of Python programming skills in creating a practical tool.

## File Descriptions

### `main.py`
The main file of the project where the core functionality is implemented. This file includes the primary class `TodoListManager` and functions for creating, viewing, and managing to-do lists and tasks. The main loop that interacts with the user through the console is also located here. The functions in this file include:
- `main()`: The main function that runs the program and handles user input.
- `main_menu()`: Displays the main menu and handles user choices.
- `view_all_todo_lists_menu()`: Displays all to-do lists and handles user interactions with them.
- `new_todo_list_menu()`: Prompts the user to create a new to-do list.
- `remove_todo_list_menu()`: Prompts the user to remove a to-do list.
- `selected_todo_list_menu()`: Displays a selected to-do list and handles task-related operations.
- `new_task_menu()`: Prompts the user to create a new task.
- `remove_task_menu()`: Prompts the user to remove a task.

### `todo_list.py`
This file contains the `TodoList` class, which manages individual to-do lists. Each to-do list can have multiple tasks, and this class provides methods to add, complete, and remove tasks. The main methods in this file include:
- `__init__(self, name)`: Initializes a new to-do list with a given name.
- `add_task(self, task)`: Adds a new task to the to-do list.
- `complete_task(self, task_id)`: Toggles the completion status of a task.
- `remove_task(self, task_id)`: Removes a task from the to-do list.

## Design Choices

### Class-Based Structure
One of the primary design choices for this project was to use a class-based structure to manage to-do lists. This decision was made to keep the code organized and to encapsulate the functionality related to to-do lists and tasks within the `TodoList` class. This approach makes the code more modular and easier to maintain.

### Console-Based Interaction
The project is designed to be run in a console, providing a simple text-based interface for users to interact with. This choice was made to focus on core functionality and avoid the complexity of building a graphical user interface. The console-based approach also aligns well with the objectives of the CS50P course, emphasizing fundamental programming skills.

### User Input Handling
The main loop in `main.py` handles user input through various menu functions. This design choice ensures that the user is guided through the process of creating and managing to-do lists in a clear and structured manner. Each menu function includes input validation to ensure the user enters valid choices, enhancing the robustness of the program.

### Task Completion
A notable feature of the project is the ability to toggle the completion status of tasks. This functionality is implemented in the `complete_task` method of the `TodoList` class. The design choice to use a simple boolean toggle for task completion ensures that the user can easily mark tasks as done or undone.

### Feedback and Guidance
To improve the user experience, the program provides feedback messages after each operation. For example, when a new to-do list or task is created, a confirmation message is displayed. This design choice helps users understand that their actions have been successfully processed.

## Future Improvements

While the current version of Check Mate meets the basic requirements of a to-do list manager, there are several areas for potential improvement:
- **Enhanced User Interface**: Adding a graphical user interface (GUI) would make the program more user-friendly and visually appealing.
- **Persistence**: Implementing a way to save and load to-do lists from a file would allow users to retain their tasks between sessions.
- **Task Prioritization**: Adding features to set and view task priorities could help users manage their tasks more effectively.
- **Notifications**: Integrating reminders or notifications for upcoming tasks would further enhance the usability of the program.

Check Mate is a robust foundation for managing tasks and to-do lists, demonstrating practical Python programming skills and providing a solid starting point for future enhancements.
