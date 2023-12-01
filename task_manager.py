from json import dump, load


class TaskManager():
    def __init__(self):
        """Initialize the TaskManager instance with the path to the JSON file."""
        self._json_file_path = "python-task-manager/task.json"
        # read json file and store it on a variable as a list
        with open(self._json_file_path, "r") as file:
            self._task_json = load(file)

    def view_all_items(self):
        """Print all task items and display statistics."""
        view_all_result_count = 0
        completed_task_count = 0
        pending_task_count = 0
        category_completed_task_count = {}
        category_pending_task_count = {}
        category_count_dict = {}
        if len(self._task_json) < 1:
            print("No Task Records")
        else:
            # Display Task Table
            task_table_header = f"{'ID':<3} | {'Title':<10} | {
                'Description':<25} | {'Category':<10} | {'Status':<10} |"
            print(task_table_header)
            print(len(task_table_header) * "-")
            for index, task_item in enumerate(self._task_json):
                view_all_result_count += 1
                print(f"{index+1:<3} | {task_item["title"]:<10} | {task_item["description"]:<25} | {task_item["category"]:<10} | {task_item["status"]:<10} |")
                # Total count per category
                if task_item["category"] in category_count_dict:
                    category_count_dict[task_item["category"]] += 1
                else:
                    category_count_dict[task_item["category"]] = 1

                # Item count per status
                if task_item["status"] == "Completed":
                    completed_task_count += 1
                    if task_item["category"] in category_completed_task_count:
                        category_completed_task_count[task_item["category"]] += 1
                    else:
                        category_completed_task_count[task_item["category"]] = 1
                else:
                    pending_task_count += 1
                    if task_item["category"] in category_pending_task_count:
                        category_pending_task_count[task_item["category"]] += 1
                    else:
                        category_pending_task_count[task_item["category"]] = 1
            # Display total row count
            print(f"{view_all_result_count} item(s) Pending Task: {pending_task_count} Completed Task: {completed_task_count}")
            # Display stats table
            category_count_header = f"{"Category":<10} | {
                "Completed":<10} | {"Pending":<10} | {"Total":<10}"
            print(category_count_header)
            print(len(category_count_header) * "-")
            for category, count in category_count_dict.items():
                print(f"{category:<10} | {category_completed_task_count[category]:<10} | {category_pending_task_count[category]:<10} | {count:<10}")
            print(len(category_count_header) * "-")

    def add_task(self):
        """Add a new task to the task list."""
        print("Add New Task:")
        task_title = input("Task Title: ")
        task_description = input("Description: ")
        task_category = input("Category: ")
        add_new_loop = True
        while add_new_loop:
            save_item_input = input("Want to save item(Y/N): ")
            if save_item_input.lower() == "y":
                self._task_json.append(
                    {"title": task_title, "description": task_description, "category": task_category, "status": "Pending"})
                with open(self._json_file_path, "w") as file:
                    dump(self._task_json, file)
                self.view_all_items()
                add_new_loop = False
            elif save_item_input.lower() == "n":
                add_new_loop = False
            else:
                print("Invalid input: Enter y for Yes and n for No.")

    def remove_task(self):
        """Remove a task from the task list."""
        print("Delete Task")
        self.view_all_items()
        remove_task_loop = True
        while remove_task_loop:
            try:
                remove_task_input = int(input("Enter Task ID to remove: "))
                task_item = self._task_json[remove_task_input-1]
                print(f"Title: {task_item['title']}\nDescription: {task_item['description']}\nCategory: {task_item['category']}\nStatus: {task_item['status']}")
                remove_task_confirmation_loop = True
                while remove_task_confirmation_loop:
                    remove_task_confirmation_input = input(
                        "Do you want to proceed on deleting this item? (y/n): ")
                    if remove_task_confirmation_input.lower() == "y":
                        self._task_json.pop(remove_task_input - 1)
                        with open(self._json_file_path, "w") as file:
                            dump(self._task_json, file)
                        remove_task_confirmation_loop = False
                        remove_task_loop = False
                    elif remove_task_confirmation_input.lower() == "n":
                        remove_task_confirmation_loop = False
                        remove_task_loop = False
                    else:
                        print(
                            "Invalid input: Please enter y if Yes and n if No only.")
            except ValueError:
                print("Invalid entry: Please enter numerical value only.")
            except IndexError:
                print("Item ID does not exist. Choose another one.")

    def change_task_status(self):
        """Change the status of a task."""
        print("Change Task Status")
        self.view_all_items()
        change_task_status_loop = True
        while change_task_status_loop:
            try:
                # Ask for item ID
                change_task_status_input = int(
                    input("Enter Task ID to Change Status: "))
                task_item = self._task_json[change_task_status_input - 1]
                print(f"Title: {task_item['title']}\nDescription: {task_item['description']}\nCategory: {task_item['category']}\nStatus: {task_item['status']}")
                status_change_to = "Completed" if task_item['status'] == "Pending" else "Pending"
                change_task_status_confirmation_loop = True
                while change_task_status_confirmation_loop:
                    change_task_status_confirmation_input = input(
                        f"Do you want to change status of this item to {status_change_to}? (y/n): ")
                    if change_task_status_confirmation_input.lower() == "y":
                        self._task_json[change_task_status_input - 1]['status'] = status_change_to
                        with open(self._json_file_path, "w") as file:
                            dump(self._task_json, file)
                        change_task_status_confirmation_loop = False
                        change_task_status_loop = False
                        task_item = self._task_json[change_task_status_input - 1]
                        print(f"Title: {task_item['title']}\nDescription: {task_item['description']}\nCategory: {task_item['category']}\nStatus: {task_item['status']}")
                    elif change_task_status_confirmation_input.lower() == "n":
                        change_task_status_confirmation_loop = False
                        change_task_status_loop = False
                    else:
                        print(
                            "Invalid input: Please enter y if Yes and n if No only.")
            except ValueError:
                print("Invalid Entry: Enter numerical value only.")
            except IndexError:
                print("Item ID does not exist. Choose another one.")

    def view_filtered_items(self, category):
        """Display filtered task list by category."""
        record_count = 0
        completed_task_count = 0
        pending_task_count = 0
        # Display filtered table
        task_table_header = f"{'ID':<3} | {'Title':<10} | {
            'Description':<25} | {'Category':<10} | {'Status':<10} |"
        print(task_table_header)
        print(len(task_table_header) * "-")
        for index, task_item in enumerate(self._task_json):
            if task_item["category"].lower() == category.lower():
                print(f"{index + 1:<3} | {task_item["title"]:<10} | {task_item["description"]:<25} | {
                      task_item["category"]:<10} | {task_item["status"]:<10} |")
                record_count += 1
                if task_item["status"] == "Completed":
                    completed_task_count += 1
                else:
                    pending_task_count += 1
        if record_count == 0:
            print(" No record to display")
        else:
            # Display row count
            print(f"{record_count} item(s) Pending Task: {
                  pending_task_count} Completed Task: {completed_task_count}")

    def view_menu(self):
        """Display the view menu with options to view all tasks or tasks by category."""
        view_menu_loop = True
        while view_menu_loop:
            try:
                view_menu_input = int(input(
                    "View Menu:\nEnter 1: View all task, 2: View task by category 3: Back to Main Menu: "))
                if view_menu_input == 1:
                    self.view_all_items()
                elif view_menu_input == 2:
                    category_input = input("Search category: ")
                    self.view_filtered_items(category_input)
                elif view_menu_input == 3:
                    view_menu_loop = False
                else:
                    print("Invalid input: Please enter 1, 2 or 3 only.")
            except ValueError:
                print("Invalid input: Please enter numerical value only.")

    def manage_menu(self):
        manage_menu_loop = True
        while manage_menu_loop:
            try:
                manage_menu_input = int(input(
                    "Manage Task Menu:\nEnter 1: Add Item, 2: Change Task Status, 3: Delete Item, 4: Back to Main Menu: "))
                if manage_menu_input == 1:
                    self.add_task()
                elif manage_menu_input == 2:
                    self.change_task_status()
                elif manage_menu_input == 3:
                    self.remove_task()
                elif manage_menu_input == 4:
                    manage_menu_loop = False
                else:
                    print("Invalid input: Please enter 1, 2, 3 or 4 only.")
            except ValueError:
                print("Invalid input: Please enter numerical value only.")

# Main Application loop
app_running = True
task_manager = TaskManager()
print("Task Manager App")
while app_running:
    try:
        menu_input = int(
            input("Main Menu:\nEnter 1: View Task, 2: Manage Task, 3: Exit App: "))
        if menu_input == 1:
            task_manager.view_menu()
        elif menu_input == 2:
            task_manager.manage_menu()
        elif menu_input == 3:
            print("Exiting App...")
            app_running = False
    except ValueError:
        print("Invalid Input: Please enter Numerical value.")
