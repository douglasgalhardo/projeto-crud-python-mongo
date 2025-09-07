from bson.objectid import ObjectId
from app.utilitarios import limpar_tela, print_estudante

# CREATE
def create_estudante(collection):
    limpar_tela()
    print("--- Adicionar um novo aluno. ---")

    try:
        nome = input("nome: ")
        while True:
            try:
                idade = int(input("idade: "))
                break
            except ValueError:
                print("Idade inválida! Por favor, insira um número.")
        sexo = input("sexo: ")
        cidade = input("cidade: ")
        curso = input("curso: ")

        documentar = {
            "nome": nome, "idade": idade, "sexo": sexo,
            "cidade": cidade, "curso": curso
        }

        resultar = collection.insert_one(documentar)
        print(
            f"\nAluno '{nome}' criado com sucesso! ID: {resultar.inserted_id}")
    except Exception as e:
        print(f"\nErro ao criar aluno: {e}")
    input(f"\nPressione enter para continuar...")

# READ

def read_estudante(Collection):
    limpar_tela()
    print("--- Consultar alunos ---")
    print("1. Listar todos os alunos")
    print("2. Filtrar por um campo")
    escolha = input("Escolha uma opção: ")

    filter_query = {}
    if escolha == '2':
        print("\nCampos disponíveis: nome, idade, sexo, cidade e Curso")
        campo = input("Digite o nome do campo para filtrar: ").lower()
        valor = input(f"Digite o valor para '{campo}': ")

        if campo == 'idade':
            try:
                valor = int(valor)
            except ValueError:
                print("Valor de idade inválido.")

        filter_query = {campo: valor}

    try:
        resultados = Collection.find(filter_query)
        estudantes = list(resultados)

        limpar_tela()
        print("--- Resultados da busca ---")
        if not estudantes:
            print("Nenhum aluno encontrado.")
        else:
            print(f"Encontrado(s) {len(estudantes)} aluno(s):\n")
            for estudante in estudantes:
                print_estudante(estudante)
    except Exception as e:
        print(f"\nErro ao consultar alunos: {e}")
    input("\nPressione enter para continuar...")


# Update
def update_estudante(collection):
    limpar_tela()
    print("--- Atualizar aluno ---")
    estudante_id = input("Digite o ID do aluno que deseja atualizar: ")

    try:
        objetic_id = ObjectId(estudante_id)
        estudante = collection.find_one({"_id": objetic_id})

        if not estudante:
            print("Nenhum aluno foi encontrado com este ID.")
        else:
            print("\nAluno encontrado:")
            print_estudante(estudante)
            print("Qual campo deseja atualizar: (nome, idade, sexo, cidade ou curso)")
            campo = input("Campo: ").lower()
            if campo in estudante:
                novo_valor = input(f"Digite o novo valor para '{campo}': ")
                if campo == "idade":
                    novo_valor = int(novo_valor)

                collection.update_one({"_id": objetic_id}, {
                                      "$set": {campo: novo_valor}})
                print("\nAluno atualizado com sucesso!")
            else:
                print("Campo inválido.")
    except Exception as e:
        print(f"\nErro ao atualizar o aluno: {e}")
    input("\nPressione enter para continuar...")

# Delete

def delete_estudante(collection):
    limpar_tela()
    print("--- Deletar aluno ---")
    estudante_id = input("Digite o ID do aluno que deseja deletar: ")

    try:
        object_id = ObjectId(estudante_id)
        estudante_para_deletar = collection.find_one({"_id": object_id})

        if not estudante_para_deletar:
            print("Nenhum aluno encontrado com este ID.")
        else:
            print("\nTem certeza que deseja deletar o seguinte aluno?")
            print_estudante(estudante_para_deletar)
            confirmacao = input("Digite 's' para confirmar: ").lower()

            if confirmacao == 's':
                resultar = collection.delete_one({"_id": object_id})
                if resultar.deleted_count > 0:
                    print("\nAluno deletado com sucesso!")
            else:
                print("\nOperação cancelada.")
    except Exception as e:
        print(f"\nErro ao deletar o aluno(a): {e}")
    input("\nPressione enter para continuar...")
