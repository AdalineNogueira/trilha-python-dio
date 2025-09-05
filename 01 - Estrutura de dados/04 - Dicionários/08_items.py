contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
            "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
            "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
            "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
            }

#contatos.items() -> Retorna uma lista de tuplas (chave, valor) dos valores do dicionário
resultado = contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
print(resultado)
