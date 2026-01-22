cadastros = []

while True:
    print('\n--- MENU ---')
    print('1 - Listar cadastros')
    print('2 - Adicionar cadastro')
    print('3 - Remover cadastro')
    print('4 - Sair')

    opcao = input('Escolha uma opção: ').strip()

    if opcao == '1':
        if cadastros:
            print('\nCadastros:')
            for i, nome in enumerate(cadastros, start=1):
                print(f'{i} - {nome}')
        else:
            print('\nNenhum cadastro encontrado.')

    elif opcao == '2':
        nome = input('Digite o nome para cadastrar: ').strip()
        if nome:
            cadastros.append(nome)
            print(f'{nome} cadastrado com sucesso!')
        else:
            print('Nome inválido.')

    elif opcao == '3':
        if cadastros:
            for i, nome in enumerate(cadastros, start=1):
                print(f'{i} - {nome}')
            try:
                remover = int(input('Digite o número do cadastro para remover: '))
                if 1 <= remover <= len(cadastros):
                    removido = cadastros.pop(remover - 1)
                    print(f'{removido} removido com sucesso!')
                else:
                    print('Número inválido.')
            except ValueError:
                print('Digite um número válido.')
        else:
            print('Não há cadastros para remover.')

    elif opcao == '4':
        print('Saindo do sistema...')
        break

    else:
        print('Opção inválida.')
Adiciona script principal em Python
