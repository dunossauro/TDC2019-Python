from behave import given, when, then
from app.exemplo import cadastro_de_usuario


@given('um usuário')
def insert_user_in_context(context):
    context.user = {
        key: value for key, value in context.table
    }


@when('efetuo o cadastro')
def call_registry(context):
    cadastro_de_usuario(context.user)


@then('o usuário "{user}" deve constar na base de dados')
@then('o usuário "{user}" {cond} deve constar na base de dados')
def check_user_on_database(context, user, cond=None):
    if cond:
        assert not context.db.user_query(user), f"Usuário {user} registrado"
    else:
        assert context.db.user_query(user), f"Usuário {user} não registrado"
