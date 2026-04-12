from models.imovel import Imovel
from config import VALOR_CASA, ACRESCIMO_CASA_2Q, VALOR_VAGA


class Casa(Imovel):

    def __init__(self, quartos, vaga):
        super().__init__(VALOR_CASA)
        self.quartos = quartos
        self.vaga = vaga


    def calcular_valor(self):

        valor = self.valor_base

        if self.quartos == 2:
            valor += ACRESCIMO_CASA_2Q

        if self.vaga:
            valor += VALOR_VAGA

        return valor