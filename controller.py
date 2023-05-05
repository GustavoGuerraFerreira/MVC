from dal import PessoaDal
from model import Pessoa
class PessoaController:

    @classmethod
    def cadastrar(cls, nome, idade, cpf):
        if len(nome) > 3 and (idade >0 and idade < 100) and len(str(cpf))== 11:
            try:
                PessoaDal.salvar(Pessoa(nome, idade, cpf))
                return True
            except:
                return False
        else:
            print('Dados invalidos')
            return False



