from datetime import date
from wtforms import ValidationError


def validate_title(title: str):
    """Ensure the title is not only numbers.

    Args:
        title (str): title of a 'Todo' object.

    Raises:
        ValidationError: wtforms Validation error.
    """
    if title.isdigit():
        raise ValidationError("Title cannot contain only numbers.")


def validate_duedate(duedate: date):
    """Ensure the due date is not in the past.

    Args:
        duedate (date): datetime.date object.

    Raises:
        ValidationError: wtforms Validation error.
    """
    if duedate < date.today():
        raise ValidationError("Due date cannot be in the past.")
