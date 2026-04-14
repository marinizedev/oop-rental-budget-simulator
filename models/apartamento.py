from models.imovel import Imovel
from config import VALOR_APARTAMENTO, ACRESCIMO_APT_2Q, VALOR_VAGA, DESCONTO_APT_SEM_CRIANCA

class Apartamento(Imovel):

    def __init__(self, quartos, vaga, tem_crianca):
        super().__init__(VALOR_APARTAMENTO)
        self.quartos = quartos
        self.vaga = vaga
        self.tem_crianca = tem_crianca


    def calcular_valor(self):

        valor = self.valor_base

        if self.quartos == 2:
            valor += ACRESCIMO_APT_2Q

        if self.vaga:
            valor += VALOR_VAGA

        if not self.tem_crianca:
            valor *= (1 - DESCONTO_APT_SEM_CRIANCA)

        return valor
