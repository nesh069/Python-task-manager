# Import functions from task_manager.task_utils package
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks

# Define the main function
def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            try:
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                add_task(title, description, due_date)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                if not tasks:
                    print("No tasks available.")
                    continue
                print("\nCurrent Tasks:")
                for i, task in enumerate(tasks, start=1):
                    status = "Done" if task["completed"] else "Pending"
                    print(f"{i}. {task['title']} [{status}]")
                index = int(input("Enter task index to mark as complete: "))
                mark_task_as_complete(index - 1)
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            progress = calculate_progress()
            print(f"\nOverall Progress: {progress:.1f}%")
            print(f"Total Tasks: {len(tasks)}")
            completed = sum(1 for t in tasks if t["completed"])
            print(f"Completed: {completed}")
            print(f"Pending: {len(tasks) - completed}")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()