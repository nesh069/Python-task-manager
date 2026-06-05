from datetime import datetime

def validate_task_title(title):
    if len(title):
        if len(title.strip()):
            return True
    raise ValueError("Title must be a non-empty string.")

def validate_task_description(description):
    if len(description):
        if len(description.strip()):
            return True
    raise ValueError("Description must be a non-empty string.")

def validate_due_date(due_date):
    if len(due_date):
        pass
    else:
        raise ValueError("Due date must be a non-empty string.")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
    return True