# language:pt

Funcionalidade: Cadastro de usuário

Cenário: Usuário válido na base de dados
  Dado um usuário
   | chave      | valor   |
   | nome       | Luciano |
   | sobrenome  | Ramalho |
  Quando efetuo o cadastro
  Então o usuário "Luciano" deve constar na base de dados

Cenário: Usuário inválido na base de dados
  Dado um usuário
   | chave      | valor |
   # | nome       | Bruno |
   | sobrenome  | Rocha |
  Quando efetuo o cadastro
  Então o usuário "Bruno" não deve constar na base de dados
