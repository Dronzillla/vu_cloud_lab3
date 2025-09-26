from blueprintapp.app import db


class Todo(db.Model):
    __tablename__ = "todos"

    tid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    duedate = db.Column(db.Date, nullable=False)
    done = db.Column(db.Boolean)

    def __repr__(self):
        return f"Title: {self.title}, Description: {self.description}, Due Date: {self.duedate}, Done: {self.done}"
