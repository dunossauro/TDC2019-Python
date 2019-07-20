from app.exemplo import DataBase


def before_scenario(context, scenario):
    context.db = DataBase()


def after_scenario(context, scenario):
    context.db.clear_database()
