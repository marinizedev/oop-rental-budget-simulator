from services.input_service import criar_imovel, pegar_parcelas
from services.orcamento_service import OrcamentoService
from services.output_service import mostrar_resultado
from services.exportador_csv import gerar_csv

imovel = criar_imovel()

parcelas = pegar_parcelas()

service = OrcamentoService()

orcamento = service.gerar_orcamento(imovel, parcelas)

mostrar_resultado(orcamento)

tipo_imovel = imovel.__class__.__name__.lower()

gerar_csv(
    orcamento["aluguel"],
    orcamento["parcela_contrato"],
    orcamento["parcelas"],
    tipo_imovel,
    orcamento["total_anual"]

)

print("\nCSV gerado com sucesso!")