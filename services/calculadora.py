from config import VALOR_CONTRATO

class Contrato:

    def __init__(self, parcelas):

        if parcelas < 1 or parcelas > 5:
            raise ValueError("Parcelas devem estar entre 1 e 5.")
        
        self.valor_total = VALOR_CONTRATO
        self.parcelas = parcelas

    def calcular_parcela(self):
        return self.valor_total / self.parcelas