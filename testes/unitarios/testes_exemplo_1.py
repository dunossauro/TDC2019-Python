from app.exemplo import cadastro_de_usuario
from unittest.mock import patch


def test_cadastro_usuario_sem_duble():
    assert not cadastro_de_usuario(
        {'Batatinha': 'Frita'}
    )


def test_cadastro_usuario_com_duble():
    with patch('app.exemplo.validador') as validador:
        validador.return_value = False

        assert not cadastro_de_usuario(
            {'Batatinha': 'Frita'}
        )
