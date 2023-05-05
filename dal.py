from model import Pessoa
class PessoaDal:
    @classmethod
    def salvar(cls, pessoa : Pessoa):
        with open('pessoas.txt', 'w') as arq:
            arq.write(f'{pessoa.nome} {pessoa.idade} {pessoa.cpf}')
    @classmethod
    def ler(cls):
        nome = 'Gustavo'
        idade = '20'
        cpf = 20210302130
        return Pessoa(nome, idade, cpf)
