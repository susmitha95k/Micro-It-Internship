# Simple To-Do List Program

# List to store tasks
tasks = []

# Menu for the program
while True:
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        if not tasks:
            print("Your to-do list is empty!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter a task to add: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Task '{removed}' removed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please try again!")