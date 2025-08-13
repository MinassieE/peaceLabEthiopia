tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks found!")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        print(str(i) + ". " + task)

def add_task():
    name = input("Enter new task: ").strip()
    if name:
        tasks.append(name)
        print("Task added!")
    else:
        print("Task cannot be empty.")

def delete_task():
    show_tasks()
    n = int(input("Enter task number to delete: "))
    if 1 <= n <= len(tasks):
        removed = tasks.pop(n-1)
        print("Task '" + removed + "' deleted!")
    else:
        print("Invalid number.")

def main():
    while True:
        print("\nMenu: \n1. View Tasks  \n2. Add Task  \n3. Delete Task  \n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
