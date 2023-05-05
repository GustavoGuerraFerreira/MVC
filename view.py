from controller import PessoaController
while True:
    decisao = int(input('\nDigite 1 para salvar uma pessoa\nDigite 2 para ver a pessoa salva\nDigite 3 para sair\nResposta: '))
    if decisao == 1:
       nome = input("\nDigite o nome da pessoa: ")
       idade = int(input("Digite a idade da pessoa: "))
       cpf = int(input("Digite o cpf da pessoa: "))
       if PessoaController.cadastrar(nome, idade, cpf):
           print('\nUsuário cadastrado com sucesso')
       else:
           print('\n***********Digite valores validos***********')
    elif decisao == 2:
        print('aqui 2')
    if decisao == 3:
        break