from datetime import datetime
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Global tasks list
tasks = []

def add_task(title, description, due_date):
    if len(title):
        pass
    else:
        raise ValueError("Title must be a non-empty string.")
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)
    
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
    if not isinstance(index, int):
        raise ValueError("Index must be an integer.")
    if index < 0 or index >= len(tasks_list):
        raise ValueError("Invalid task index.")
    
    tasks_list[index]["completed"] = True
    print("Task marked as complete!")
    return True

def view_pending_tasks(tasks_list=tasks):
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
    if not tasks_list:
        return 0.0
    
    completed_count = sum(1 for task in tasks_list if task["completed"])
    progress = (completed_count / len(tasks_list)) * 100
    return progress