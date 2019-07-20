from typing import Dict
from itertools import count


class DataBase:
    """Banco de dados "emulado"."""
    counter = count(start=1)
    db = []

    def insert(self, value):
        """Insere um valor no banco de dados."""
        value['id'] = next(self.counter)
        self.db.append(value)

    def user_query(self, user: str):
        query = [registro for registro in self.db if registro['nome'] == user]
        return query if query else []

    def clear_database(self):
        self.db = []


db = DataBase()


def validador(user: Dict[str, str]):
    return user.get('nome', None)


def cadastro_de_usuario(usuario: Dict):
    if validador(usuario):
        db.insert(usuario)
        return True
    return False
