from flask import Blueprint, request, jsonify
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
# @api.route("/todos", methods=["POST"])
# def create_todo():
#     data = request.get_json()
#     response = valid_title_and_duedate(data=data)
#     if type(response) is not dict:
#         return response

#     # Create the new todo object
#     new_todo = Todo(
#         title=response.get("title"),
#         description=data.get("description"),
#         duedate=response.get("duedate"),
#         done=data.get("done", False),
#     )
#     # TODO dependency injection?
#     db_create_new_todo_obj(todo=new_todo, db_session=db.session)
#     # TODO success follow delete patern? Maybe returning newly created todo object in the response?
#     return jsend_success(status_code=201)


@api.route("/todos", methods=["POST"])
def create_todo():
    import logging

    logger = logging.getLogger(__name__)

    logger.info("=== CREATE_TODO ENDPOINT HIT ===")
    data = request.get_json()
    logger.info(f"Request data: {data}")

    response = valid_title_and_duedate(data=data)
    logger.info(f"Validation response type: {type(response)}")

    if type(response) is not dict:
        logger.warning(f"Validation failed, early return")
        return response

    logger.info("Creating Todo object...")
    # Create the new todo object
    new_todo = Todo(
        title=response.get("title"),
        description=data.get("description"),
        duedate=response.get("duedate"),
        done=data.get("done", False),
    )
    logger.info(f"Todo created: {new_todo.title}, {new_todo.duedate}")

    # TODO dependency injection?
    logger.info("Calling db_create_new_todo_obj...")
    result = db_create_new_todo_obj(todo=new_todo, db_session=db.session)
    logger.info(f"db_create_new_todo_obj returned: {result.tid if result else None}")

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


@api.route("/debug/schema")
def debug_schema():
    from sqlalchemy import inspect, text

    inspector = inspect(db.engine)

    tables = inspector.get_table_names()
    schema_info = {}

    for table in tables:
        columns = inspector.get_columns(table)
        schema_info[table] = [col["name"] for col in columns]

    # Also check row count
    counts = {}
    for table in tables:
        result = db.session.execute(text(f"SELECT COUNT(*) FROM {table}"))
        counts[table] = result.scalar()

    return jsonify({"tables": tables, "schema": schema_info, "row_counts": counts}), 200


@api.route("/test/direct-create", methods=["GET"])
def test_direct_create():
    from datetime import datetime, timedelta

    try:
        test_todo = Todo(
            title="Direct Test",
            description="Testing direct creation",
            duedate=datetime.now() + timedelta(days=1),
            done=False,
        )
        db_create_new_todo_obj(todo=test_todo, db_session=db.session)

        # Check if it exists
        count = Todo.query.count()
        found = Todo.query.filter_by(title="Direct Test").first()

        return (
            jsonify(
                {
                    "success": True,
                    "created_tid": test_todo.tid,
                    "found": found.tid if found else None,
                    "total_count": count,
                }
            ),
            200,
        )
    except Exception as e:
        import traceback

        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500
