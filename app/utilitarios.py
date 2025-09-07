import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_estudante(estudante):
    print(f"ID: {estudante['_id']}")
    print(f" Nome: {estudante.get('nome', 'N/A')}")
    print(f" Idade: {estudante.get('idade', 'N/A')}")
    print(f" Sexo: {estudante.get('sexo', 'N/A')}")
    print(f" Cidade: {estudante.get('cidade', 'N/A')}")
    print(f" Curso: {estudante.get('curso', 'N/A')}")
    print("-" * 30)
