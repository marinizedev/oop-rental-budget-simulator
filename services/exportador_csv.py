import csv


def gerar_csv(valor_aluguel, parcela_contrato, qtd_parcelas, tipo_imovel):

    tipo_imovel = tipo_imovel.lower()
    nome_arquivo = f"orcamento_{tipo_imovel}.csv"

    with open(nome_arquivo, mode="w", newline="") as arquivo:

        writer = csv.writer(arquivo)

        writer.writerow([
            "mes",
            "valor_aluguel",
            "parcela_contrato",
            "total_mensal"
        ])

        for mes in range(1, 13):

            if mes <= qtd_parcelas:
                contrato = parcela_contrato
            else:
                contrato = 0

            total_mensal = valor_aluguel + contrato

            writer.writerow([
                mes,
                valor_aluguel,
                contrato,
                total_mensal
            ])