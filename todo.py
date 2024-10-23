# To-Do List App

def display_menu():
    print("\n----- To-Do List Menu -----")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour to-do list:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("\nEnter the task to add: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

def remove_task(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return
    try:
        task_num = int(input("\nEnter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 4.")

if __name__ == "__main__":
    main()
