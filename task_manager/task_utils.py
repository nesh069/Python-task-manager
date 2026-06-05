from datetime import datetime
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Global tasks list
tasks = []

def add_task(title, description, due_date):
    """
    Adds a new task to the tasks list after validating inputs.
    Returns True if task was added successfully.
    """
    # Validate all inputs
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)
    
    # Create task dictionary
    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False
    }
    
    tasks.append(task)
    print("Task added successfully!")
    return True

def mark_task_as_complete(index, tasks_list=tasks):
    """
    Marks a task at the given index as complete.
    Returns True if successful, raises error if index is invalid.
    """
    if not isinstance(index, int):
        raise ValueError("Index must be an integer.")
    if index < 0 or index >= len(tasks_list):
        raise ValueError("Invalid task index.")
    
    tasks_list[index]["completed"] = True
    print("Task marked as complete!")
    return True

def view_pending_tasks(tasks_list=tasks):
    """
    Displays all pending (not completed) tasks.
    Returns the list of pending tasks.
    """
    pending = [task for task in tasks_list if not task["completed"]]
    
    if not pending:
        print("No pending tasks.")
    else:
        print("\nPending Tasks:")
        print("-" * 50)
        for i, task in enumerate(tasks_list):
            if not task["completed"]:
                print(f"{i}. {task['title']} - Due: {task['due_date']}")
                print(f"   Description: {task['description']}")
        print("-" * 50)
    
    return pending

def calculate_progress(tasks_list=tasks):
    """
    Calculates and returns the completion progress as a percentage.
    Returns a float between 0.0 and 100.0.
    """
    if not tasks_list:
        return 0.0
    
    completed_count = sum(1 for task in tasks_list if task["completed"])
    progress = (completed_count / len(tasks_list)) * 100
    return progress