from app.exemplo import cadastro_de_usuario


def test_cadastro_usuario_sem_sucesso(db):
    assert not cadastro_de_usuario(
        {'Batatinha': 'Frita'}
    )
    assert db.db == []


def test_cadastro_usuario_checando_usuario_no_banco(db):
    user = {'nome': 'Batara'}
    cadastro_de_usuario(user)
    assert db.user_query(user['nome'])
