import pickle
FILE_NAME = 'todo_list.pkl'

def load_tasks():
    
    try:
        with open(FILE_NAME, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(tasks, file)

def add_task(tasks):
    
    task = input("Enter the task description: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    
    if not tasks:
        print("No tasks to show.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(tasks):
    
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the number of the task to remove: "))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                save_tasks(tasks)
                print("Task removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()