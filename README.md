# Task Manager Application
This is a simple Task Manager application implemented in Python. The application allows users to manage their tasks by providing functionalities such as adding tasks, changing task status, deleting tasks, and viewing tasks. Task data is stored in a JSON file.

## Usage
1. View Menu:
    - Enter 1 to view all tasks.
    - Enter 2 to view tasks by category.
    - Enter 3 to go back to the Main Menu.
2. Manage Task Menu:
    - Enter 1 to add a new task.
    - Enter 2 to change the status of a task.
    - Enter 3 to delete a task.
    - Enter 4 to go back to the Main Menu.
3. Exiting the App:
    - Enter 3 in the Main Menu to exit the application.

## Task Data Structure
Each task has the following attributes:

- Title: The title of the task.
- Description: A brief description of the task.
- Category: The category to which the task belongs.
- Status: The status of the task, which can be either "Pending" or "Completed."

## File Structure
- task.json: JSON file to store task data.
- task_manager.py: Python script containing the TaskManager class and the main application loop.

## How to Run
1. Clone the repository:
    - git clone https://github.com/duvalld/python-task-manager.git
2. Navigate to the project directory:
    - cd python-task-manager
3. Run the application:
    - python task_manager.py