import os

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nYour Tasks:")
        for index, task in enumerate(self.tasks):
            status = "✓" if task.completed else "✗"
            print(f"{index + 1}. {task.description} [{status}]")

    def mark_task_completed(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f"Task '{removed_task.description}' deleted successfully!")
        else:
            print("Invalid task number.")

# CLI for the To-Do List Manager
def main():
    manager = TaskManager()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("To-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nChoose an option: ")
        if choice == "1":
            description = input("Enter the task description: ")
            manager.add_task(description)
        elif choice == "2":
            manager.view_tasks()
            input("\nPress Enter to continue...")
        elif choice == "3":
            manager.view_tasks()
            try:
                task_number = int(input("\nEnter the task number to mark as completed: ")) - 1
                manager.mark_task_completed(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            manager.view_tasks()
            try:
                task_number = int(input("\nEnter the task number to delete: ")) - 1
                manager.delete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
1