from flask import Blueprint, request
from blueprintapp.app import db
from blueprintapp.blueprints.api.models import Todo
from blueprintapp.blueprints.api.db_operations import (
    db_read_all_todos,
    db_read_todo_by_tid,
    db_delete_todo,
    db_create_new_todo_obj,
    db_update_todo,
)
from blueprintapp.blueprints.api.utilities import (
    valid_title_and_duedate,
    jsend_success,
    jsend_fail,
)


api = Blueprint("api", __name__, template_folder="templates")


# Get all todos
@api.route("/todos", methods=["GET"])
def get_todos():
    todos = db_read_all_todos()

    todos_list = [
        {
            "tid": todo.tid,
            "title": todo.title,
            "description": todo.description,
            "duedate": todo.duedate.isoformat(),
            "done": todo.done,
        }
        for todo in todos
    ]
    return jsend_success(data_key="todos", data_value=todos_list)


# Get a specific todo by id
@api.route("/todos/<int:tid>", methods=["GET"])
def get_todo(tid):
    todo = db_read_todo_by_tid(tid=tid)

    if todo == None:
        return jsend_fail(
            data_key="todo", data_value="Todo does not exist", status_code=404
        )

    todo_data = {
        "tid": todo.tid,
        "title": todo.title,
        "description": todo.description,
        "duedate": todo.duedate.isoformat(),
        "done": todo.done,
    }
    return jsend_success(data_key="todo", data_value=todo_data)


# Create new todo
@api.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    response = valid_title_and_duedate(data=data)
    if type(response) is not dict:
        return response

    # Create the new todo object
    new_todo = Todo(
        title=response.get("title"),
        description=data.get("description"),
        duedate=response.get("duedate"),
        done=data.get("done", False),
    )
    # TODO dependency injection?
    db_create_new_todo_obj(todo=new_todo, db_session=db.session)
    # TODO success follow delete patern? Maybe returning newly created todo object in the response?
    return jsend_success(status_code=201)


# Update an existing todo
@api.route("/todos/<int:tid>", methods=["PUT"])
def update_todo(tid):
    # todo = db_read_todo_by_tid_or_404(tid=tid)
    todo = db_read_todo_by_tid(tid=tid)

    if todo == None:
        return jsend_fail(
            data_key="todo", data_value="Todo does not exist", status_code=404
        )

    data = request.get_json()
    response = valid_title_and_duedate(data=data)
    if type(response) is not dict:
        return response

    db_update_todo(
        todo=todo,
        title=response.get("title"),
        description=data.get("description"),
        duedate=response.get("duedate"),
        done=data.get("done"),
    )
    # TODO should update follow delete patern?
    return jsend_success()


# Delete an existing todo
@api.route("/todos/<int:tid>", methods=["DELETE"])
def delete_todo(tid):
    todo = db_read_todo_by_tid(tid=tid)

    if todo == None:
        return jsend_fail(
            data_key="todo", data_value="Todo does not exist", status_code=404
        )

    db_delete_todo(todo=todo)
    return jsend_success()
