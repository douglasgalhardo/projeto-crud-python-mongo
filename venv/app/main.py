from app.banco_de_dados import conectar_db
from app.crud import create_estudante, read_estudante, update_estudante, delete_estudante
from app.utilitarios import limpar_tela


def main():
    collection = conectar_db()
    if collection is None:
        return
    while True:
        limpar_tela()
        print("===== Gerenciador de Alunos (CRUD MongoDB) =====")
        print("1. Adicionar Aluno (Create)")
        print("2. Consultar Alunos (Read)")
        print("3. Atualizar Aluno (Update)")
        print("4. Deletar Aluno (Delete)")
        print("5. Sair")
        print("=" * 50)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            create_estudante(collection)
        elif escolha == '2':
            read_estudante(collection)
        elif escolha == '3':
            update_estudante(collection)
        elif escolha == '4':
            delete_estudante(collection)
        elif escolha == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. \nTente novamente!")
            input("\nPressione enter para continuar...")


if __name__ == "__main__":
    main()
