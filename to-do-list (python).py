def main():
    todo_list = []
    print("--- Welcome to Your Python To-Do List ---")
    while True:
        print("\nOptions:")
        print("1. View Tasks")
        print("2. Add a Task")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()
        if choice == "1":
            print("\n--- Your Current Tasks ---")
            if not todo_list:
                print("Your list is currently empty!")
            else:
                for index, task in enumerate(todo_list, start=1):
                    print(f"{index}. {task}")
        elif choice == "2":
            new_task = input("\nEnter the task you want to add: ").strip()
            if new_task:
                todo_list.append(new_task)
                print(f"'{new_task}' has been added to your list.")
            else:
                print("Task cannot be empty!")             
        elif choice == "3":
            print("\nGoodbye! Have a productive day!")
            break         
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main()
