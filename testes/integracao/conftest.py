import pytest
from app.exemplo import DataBase


@pytest.fixture
def db():
    database = DataBase()
    yield database
    database.clear_database()
