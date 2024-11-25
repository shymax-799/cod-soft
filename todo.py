def show_menu():
    print("\n-- To-Do List Menu --")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")

def show_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")

def add_task(todo_list):
    task = input("Enter the task to add: ")
    todo_list.append(task)
    print(f"Task '{task}' has been added to your to-do list.")

def remove_task(todo_list):
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    todo_list = []

    while True:
        show_menu()

        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            show_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            print("Exiting the To-Do List app. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")
ma