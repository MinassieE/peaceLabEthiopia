tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks found!")
        return
    print("\nTo-Do List:")
    i = 1
    for t in tasks:
        if t["done"]:
            status = "DONE"
        else:
            status = "PENDING"
        print(str(i) + ". " + t["task"] + " [" + status + "]")
        i += 1

def add_task():
    name = input("Enter new task: ").strip()
    if name:
        tasks.append({"task": name, "done": False})
        print("Task added!")
    else:
        print("Task cannot be empty.")

def mark_done():
    show_tasks()
    try:
        n = int(input("Enter task number to mark as done: "))
        if 1 <= n <= len(tasks):
            tasks[n-1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    try:
        n = int(input("Enter task number to delete: "))
        if 1 <= n <= len(tasks):
            removed = tasks.pop(n-1)
            print("Task '" + removed["task"] + "' deleted!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nMenu: \n1.View Tasks  \n2.Add Task  \n3.Mark Done  \n4.Delete Task  \n5.Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()