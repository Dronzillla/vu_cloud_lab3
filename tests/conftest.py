from datetime import date
import pytest
from blueprintapp.app import create_app, db
from blueprintapp.blueprints.api.models import Todo


@pytest.fixture
def app():
    app = create_app(config_class="config.config.TestingConfig")
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def init_database(app):
    # Create some example todos with date objects
    todo1 = Todo(
        title="Test Todo 1",
        description="First test",
        duedate=date(2024, 9, 30),
        done=False,
    )
    todo2 = Todo(
        title="Test Todo 2",
        description="Second test",
        duedate=date(2024, 10, 5),
        done=False,
    )

    db.session.add(todo1)
    db.session.add(todo2)
    db.session.commit()

    yield db

    db.session.remove()
    db.drop_all()
