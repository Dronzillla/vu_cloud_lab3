from blueprintapp.app import db
from sqlalchemy.orm import Session
from blueprintapp.blueprints.api.models import Todo
from datetime import datetime
from typing import Optional


def db_read_all_todos() -> list[Todo]:
    """Read all 'Todo' records in database.

    Returns:
        list[Todo]: list of 'Todo' objects, that were uploaded in database.
    """
    todos = Todo.query.all()
    return todos


def db_create_new_todo_obj(todo: Todo, db_session: Session) -> Todo:
    """Records 'Todo' object to provided database session.

    Args:
        todo (Todo): 'Todo' object.
        db_session (Session): database session.

    Returns:
        Todo: created 'Todo' object.
    """
    db_session.add(todo)
    db_session.commit()
    return todo


def db_create_new_todo(title: str, description: str, duedate: datetime) -> Todo:
    """Create new 'Todo' record in database.

    Args:
        title (str): Title of a task.
        description (str): Description of a task.
        duedate (datetime): Date when the task should be completed.

    Returns:
        Todo: 'Todo' object
    """
    todo = Todo(title=title, description=description, duedate=duedate, done=False)
    db.session.add(todo)
    db.session.commit()
    return todo


def db_delete_todo(todo: Todo) -> None:
    """Deletes 'Todo' object from database.

    Args:
        todo (Todo): 'Todo' object to delete.
    """
    db.session.delete(todo)
    db.session.commit()


def db_read_todo_by_tid(tid: int) -> Optional[Todo]:
    """Search for 'Todo' record by provided id.

    Args:
        tid (int): Todo.tid

    Returns:
        Optional[Todo]: 'Todo' object if record was found, 'None' if no 'Todo' object matching the filters was found.
    """
    result = Todo.query.filter_by(tid=tid).one_or_none()
    return result


def db_update_todo(
    todo: Todo, title: str, description: str, duedate: datetime, done: bool
) -> None:
    """Update 'Todo' object with provided values.

    Args:
        todo (Todo): Todo object
        title (str): new title
        description (str): new description
        duedate (datetime): new due date
        done (bool): new task completion status
    """
    todo.title = title
    todo.description = description
    todo.duedate = duedate
    todo.done = done
    db.session.commit()
