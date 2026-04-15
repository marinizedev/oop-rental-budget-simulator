from models.imovel import Imovel
from config import VALOR_ESTUDIO, VALOR_ESTUDIO_2_VAGAS, VALOR_ESTUDIO_VAGA_EXTRA


class Estudio(Imovel):

    def __init__(self, vagas):
        super().__init__(VALOR_ESTUDIO)
        self.vagas = vagas


    def calcular_valor(self):

        valor = self.valor_base

        if self.vagas >= 2:
            valor += VALOR_ESTUDIO_2_VAGAS

            if self.vagas > 2:
                valor += (self.vagas - 2) * VALOR_ESTUDIO_VAGA_EXTRA

        elif self.vagas > 0:
            valor += VALOR_ESTUDIO_2_VAGAS
            
        return valor