from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DateField,
    SubmitField,
    BooleanField,
)
from wtforms.validators import DataRequired, Length
from blueprintapp.utilities.validators import validate_title, validate_duedate


class BaseTodoForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(1, 64)])
    description = StringField("Description")
    duedate = DateField("Due date", validators=[DataRequired()])

    def validate_title(self, field):
        validate_title(field.data)

    def validate_duedate(self, field):
        validate_duedate(field.data)


class TodoForm(BaseTodoForm):
    submit = SubmitField("Submit")


class UpdateForm(BaseTodoForm):
    done = BooleanField("Is completed")
    submit = SubmitField("Submit")
