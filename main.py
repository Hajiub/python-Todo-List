import argparse

TODO_LIST_TASKS = []


def add_task():
    """Add a task to the todo list."""
    task = input("Enter your task: ")
    TODO_LIST_TASKS.append(task)
    print("Task has been added!")
    if args.verbose:
        print(f"Task '{task}' has been added to the list.")


def delete_task():
    """Delete a task from the todo list."""
    for index, task in enumerate(TODO_LIST_TASKS):
        print(f"{index + 1}. {task}")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(TODO_LIST_TASKS):
                break
            else:
                print("Invalid task number!")
        except ValueError:
            pass
    task = TODO_LIST_TASKS.pop(choice - 1)
    print("Task has been deleted!")
    if args.verbose:
        print(f"Task '{task}' has been deleted from the list.")


def show_tasks():
    """Show all tasks in the todo list."""
    if not TODO_LIST_TASKS:
        print("Your task list is empty")
    for index, task in enumerate(TODO_LIST_TASKS):
        print(f"{index + 1}. {task}")


def clear_todo_list():
    """Clear all tasks from the todo list."""
    if not TODO_LIST_TASKS:
        print("Your task list is already empty!")
    elif TODO_LIST_TASKS:
        TODO_LIST_TASKS.clear()
        print("Your task list has been cleared!")
        if args.verbose:
            print("All tasks have been cleared from the list.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A todo list program.")
    parser.add_argument("--verbose", action="store_true", help="Verbose mode")
    args = parser.parse_args()
    if args.verbose:
        print("Verbose mode is on.")
    while True:
        print("\nMenu")
        print("1. Add task")
        print("2. Delete task")
        print("3. Show tasks")
        print("4. Clear todo list")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 5:
                if choice == 1:
                    add_task()
                elif choice == 2:
                    delete_task()
                elif choice == 3:
                    show_tasks()
                elif choice == 4:
                    clear_todo_list()
                else:
                    break
            else:
                print("Invalid task number!")
        except ValueError:
            pass
