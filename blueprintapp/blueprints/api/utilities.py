from flask import jsonify, Response
from typing import Union
from blueprintapp.utilities.validators import validate_title, validate_duedate
from wtforms import ValidationError
from datetime import datetime


def jsend_success(
    data_key: str = None,
    data_value: Union[dict, list[dict]] = None,
    status_code: int = 200,
) -> Response:
    """
    Returns a JSend-compliant success response.

    This function formats a successful JSON response following the JSend specification.
    It includes a 'status' of 'success' and wraps the data inside a 'data' key.

    Args:
        data_key (str, optional): The key to use for the data payload. Defaults to None.
        data_value (Union[dict, list[dict]], optional): The value associated with the data_key.
            Can be a dictionary or a list of dictionaries. Defaults to None.
        status_code (int, optional): HTTP status code for the response. Defaults to 200.

    Returns:
        Response: Flask JSON response object with 'success' status and provided data.
    """
    if data_key == None and data_value == None:
        return jsonify({"status": "success", "data": None}), status_code

    return jsonify({"status": "success", "data": {data_key: data_value}}), status_code


def jsend_fail(data_key: str, data_value: str, status_code: int = 400) -> Response:
    """
    Returns a JSend-compliant failure response.

    This function formats a failure JSON response following the JSend specification.
    It includes a 'status' of 'fail' and wraps the data inside a 'data' key.

    Args:
        data_key (str): The key representing the specific failure data.
        data_value (str): A message or value explaining the failure.
        status_code (int, optional): HTTP status code for the response. Defaults to 400.

    Returns:
        Response: Flask JSON response object with 'fail' status and provided failure data.
    """
    return jsonify({"status": "fail", "data": {data_key: data_value}}), status_code


def jsend_error() -> Response:
    # TODO integrate errors?
    pass


def valid_title_and_duedate(data) -> Union[dict, Response]:
    """
    Validates the 'title' and 'duedate' fields from the provided data.

    Args:
        data (dict): A dictionary containing the 'title' and 'duedate' fields to validate.

    Returns:
        Union[dict, Response]:
            - If validation succeeds, returns a dictionary with 'title' and 'duedate'.
            - If validation fails, returns a JSend 'fail' response indicating the validation error.

    Validation Steps:
        - 'title' must be present and not consist solely of numbers.
        - 'duedate' must be present, in ISO format, and cannot be in the past.
    """
    title = data.get("title")
    # title must be provided in the request
    if not title:
        return jsend_fail(data_key="title", data_value="title is required")
    # title must not be comprised of only numbers
    try:
        validate_title(title)
    except ValidationError as e:
        return jsend_fail(data_key="title", data_value=f"{str(e)}")

    duedate_str = data.get("duedate")
    # duedate must be provided in the request
    if not duedate_str:
        return jsend_fail(data_key="duedate", data_value="duedate is required")
    # duedate must not be in the past and in valid date format
    try:
        duedate = datetime.fromisoformat(duedate_str).date()
        validate_duedate(duedate)
    except ValueError:
        return jsend_fail(
            data_key="duedate", data_value="due date must be a valid ISO format date"
        )
    except ValidationError as e:
        return jsend_fail(data_key="duedate", data_value=f"{str(e)}")

    return {"title": title, "duedate": duedate}
