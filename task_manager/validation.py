from datetime import datetime

def validate_task_title(title):
    """
    Validates the task title.
    Returns True if valid, raises ValueError with message if invalid.
    """
    if not title or not isinstance(title, str):
        raise ValueError("Title must be a non-empty string.")
    if len(title.strip()) == 0:
        raise ValueError("Title cannot be empty or whitespace only.")
    return True

def validate_task_description(description):
    """
    Validates the task description.
    Returns True if valid, raises ValueError with message if invalid.
    """
    if not description or not isinstance(description, str):
        raise ValueError("Description must be a non-empty string.")
    if len(description.strip()) == 0:
        raise ValueError("Description cannot be empty or whitespace only.")
    return True

def validate_due_date(due_date):
    """
    Validates the due date format (YYYY-MM-DD).
    Returns True if valid, raises ValueError with message if invalid.
    """
    if not due_date or not isinstance(due_date, str):
        raise ValueError("Due date must be a non-empty string.")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
    return True