from services.calculadora import Contrato

class OrcamentoService:

    def gerar_orcamento(self, imovel, parcelas):

        valor_aluguel = imovel.calcular_valor()

        contrato = Contrato(parcelas)
        parcela_contrato = contrato.calcular_parcela()

        total_anual = valor_aluguel * 12
        total_mensal = valor_aluguel + parcela_contrato
        return {
            "aluguel": valor_aluguel,
            "parcela_contrato": parcela_contrato,
            "parcelas": parcelas,
            "total_anual": total_anual,
            "total_mensal": total_mensal
            }