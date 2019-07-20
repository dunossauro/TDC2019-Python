# Testar integração sempre vale a pena

Palestra ministrada no TDC-2019 na trilha de python

[codigo](./app)
[testes unitários](./testes/unitarios)
[testes de integração](./testes/integracao)

[slides](./slides.pdf)


## Como rodar os testes?

### Unitários

```sh
python -m pytest testes/unitarios/testes_exemplo_1.py
```

### Integração

#### behave (BDD)
```sh
behave testes/integracao/features/cadastro.feature
```

#### pytest
```sh
python -m pytest testes/integracao/testes_exemplo_2.py
```
