tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def view_tasks():
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

while True:
    print("Options: [1] Add Task  [2] View Tasks  [3] Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
