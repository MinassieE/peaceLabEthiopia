tasks = []

def show_tasks():
    return

def add_task():
   return

def delete_task():
    return

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