from flask import Flask, render_template, request

from services.orcamento_service import OrcamentoService
from services.exportador_csv import gerar_csv
from services.output_service import formatar_real

from models.apartamento import Apartamento
from models.casa import Casa
from models.estudio import Estudio

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():

    tipo = request.form.get("tipo")
    parcelas = int(request.form.get("parcelas"))

    service = OrcamentoService()

    if tipo == "apartamento":

        quartos = int(request.form.get("quartos", 1))
        vaga = request.form.get("vaga") == "sim"
        tem_crianca = request.form.get("tem_crianca") == "sim"

        imovel = Apartamento(quartos, vaga, tem_crianca)

    elif tipo == "casa":

        quartos = int(request.form.get("quartos", 1))
        vaga = request.form.get("vaga") == "sim"

        imovel = Casa(quartos, vaga)

    elif tipo == "estudio":

        vagas = int(request.form.get("vagas", 0))

        imovel = Estudio(vagas)

    else:
        return "Tipo inválido"
    
    orcamento = service.gerar_orcamento(imovel, parcelas)

    orcamento_formatado = {
        "aluguel": formatar_real(orcamento["aluguel"]),
        "parcela_contrato": formatar_real(orcamento["parcela_contrato"]),
        "total_anual": formatar_real(orcamento["total_anual"])
    }
    
    gerar_csv(
        orcamento["aluguel"],
        orcamento["parcela_contrato"],
        orcamento["parcelas"],
        tipo,
        orcamento["total_anual"]
    )

    return render_template("index.html", orcamento=orcamento_formatado)

if __name__ == "__main__":
    app.run()