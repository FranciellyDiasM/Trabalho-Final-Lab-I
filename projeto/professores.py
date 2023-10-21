# vetores de professores e turmas
professores = ["FRANCIELLY", "LUCAS LIMA"]
turmas = ["1DC", "2DC", "3DC"]

# tamanho da matriz
linhas = len(professores)
colunas = len(turmas)

# matriz
matriz = []

for i in range(linhas):
    linha = []

    for j in range(colunas):
        linha.append("")
        
    matriz.append(linha)

# Menu 
while True:
    print("\n------ Menu ------")
    print("1. Cadastrar a quantidade de alunos.")
    print("2. Pesquisar a quantidade de alunos do professor.")
    print("3. Alterar a quantidade de alunos.")
    print("4. Mostrar todos os dados.")
    print("5. Sair.")
    print()

    opcao = input("Escolha uma opção: ")
    print()

    # cadastrar a quantidade de alunos
    if opcao == "1":
        for i in range(linhas):
            for j in range(colunas):
                quantidadeAlunos = input(f"Digite a quantidade de alunos na turma {turmas[j]} do professor {professores[i]}: ")
                matriz[i][j] = quantidadeAlunos

        print("Dados cadastrados com sucesso!")

    # pesquisar

    elif opcao == "2":
        professor_pesquisa = input("Digite o nome do professor que deseja pesquisar: ").upper()
        turma_pesquisa = input("Digite a turma que deseja pesquisar: ").upper()  #deixa tudo em maiúsculo

        if professor_pesquisa in professores and turma_pesquisa in turmas:
            i = professores.index(professor_pesquisa) # index: posicao de um elemento dentro do vetor
            j = turmas.index(turma_pesquisa)
            print("Dados encontrados:")
            print(f"Professor: {professores[i]}")
            print(f"Turma: {turmas[j]}")
            print(f"Quantidade de alunos: {matriz[i][j]}")
        else: 
            print("Dados não encontrados.")

    # alterar a quantidade de alunos
    elif opcao == "3":
        professor_alterar = input("Digite o nome do professor que deseja alterar: ").upper()
        turma_alterar = input("Digite a turma que deseja alterar: ").upper()

        if professor_alterar in professores and turma_alterar in turmas:
            i = professores.index(professor_alterar)
            j = turmas.index(turma_alterar)

            nova_quantidade = input("Digite a nova quantidade de alunos: ")
            matriz[i][j] = nova_quantidade

            print("Dados alterados com sucesso!")
        else:
            print("Dados não encontrados.")

    # mostrar a matriz
    
    elif opcao == "4":
        print("PROFESSORES //      TURMAS      \\\ ")
        # nomes das turmas
        print("          ", end="  |  ")
        for i in range(colunas):
            turma = turmas[i]

            print(f"{turma:4}", end="|  ")
        print()

        for i in range(linhas):
            # nome do professor
            print(f"{professores[i]:6}", end="  |  ")

            for j in range(colunas):
                # quantidade de alunos
                print(f"{matriz[i][j]:4}", end="|  ")
            print()
    elif opcao == "5":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")