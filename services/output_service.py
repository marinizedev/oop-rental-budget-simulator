def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
def mostrar_resultado(orcamento):

    print("\n=== RESULTADO ===")

    print("Valor aluguel mensal:",
        formatar_real(orcamento["aluguel"]))
    
    print("Parcela contrato:",
        formatar_real(orcamento["parcela_contrato"]))
    
    print("Total anual:",
        formatar_real(orcamento["total_anual"]))