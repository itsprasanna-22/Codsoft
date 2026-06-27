# To-Do List Application

tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔ Completed" if task["completed"] else "✘ Pending"
        print(f"{i}. {task['task']} - {status}")

def complete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to mark as completed: "))
            tasks[task_num - 1]["completed"] = True
            print("Task marked as completed!")
        except (ValueError, IndexError):
            print("Invalid task number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed['task']}' deleted!")
        except (ValueError, IndexError):
            print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")