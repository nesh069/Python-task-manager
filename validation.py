from datetime import datetime

def validate_task_title(title):
    if len(title) > 0:
        if len(title.strip()) > 0:
            return True
    raise ValueError("Title must be a non-empty string.")

def validate_task_description(description):
    if len(description) > 500:
        raise ValueError("Description must be 500 characters or less.")
    if len(description) > 0:
        if len(description.strip()) > 0:
            return True
    raise ValueError("Description must be a non-empty string.")

def validate_due_date(due_date):
    if len(due_date) > 0:
        pass
    else:
        raise ValueError("Due date must be a non-empty string.")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
    return True