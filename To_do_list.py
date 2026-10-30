
# To-Do List Application

tasks = []

while True:
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append({"name": task, "completed": False})
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['name']} - {status}")

    # Complete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            try:
                number = int(input("Enter task number to complete: "))

                if 1 <= number <= len(tasks):
                    tasks[number - 1]["completed"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # Delete Task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            try:
                number = int(input("Enter task number to delete: "))

                if 1 <= number <= len(tasks):
                    deleted_task = tasks.pop(number - 1)
                    print("Deleted task:", deleted_task["name"])
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # Exit
    elif choice == "5":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")
