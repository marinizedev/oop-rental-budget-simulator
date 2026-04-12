from models.apartamento import Apartamento
from models.casa import Casa
from models.estudio import Estudio

def input_boolean(mensagem):

    while True:

        valor = input(mensagem).strip().lower()

        if valor in ["s", "sim"]:
            return True
        
        elif valor in ["n", "nao", "não"]:
            return False
        
        print("Digite 's' para sim ou 'n' para não.")

def criar_imovel():

    print("=== GERADOR DE ORÇAMENTO ===\n")

    print("Escolha o tipo de imóvel:")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estudio")

    while True:

        tipo = input("Digite o número da opção: ").strip()

    
        if tipo in ["1", "2", "3"]:
            break

        print("Opção inválida. Tente novamente.")

    if tipo == "1":
            
            while True:
                try:

                    quartos = int(input("Quantidade de quartos (1 ou 2): "))

                    if quartos in [1, 2]:
                         break
                    
                    print("Digite apenas 1 ou 2.")

                except ValueError:
                    print("Digite um número válido.")

            vaga = input_boolean("Deseja vaga de garagem? (s/n): ")

            tem_crianca = input_boolean("Possui crianças? (s/n): ")

            return Apartamento(quartos, vaga, tem_crianca)

    elif tipo == "2":
            
            while True:
                 
                try:

                    quartos = int(input("Quantidade de quartos (1 ou 2): "))

                    if quartos in [1, 2]:
                        break

                    print("Digite apenas 1 ou 2.")

                except ValueError:
                     print("Digite um número válido.")

            vaga = input_boolean("Deseja vaga de garagem? (s/n): ")

            return Casa(quartos, vaga)

    elif tipo == "3":
            
            while True:
                try:

                    vagas = int(input("Quantidade de vagas de estacionamento: "))

                    if vagas >= 0:
                         break
                    
                    print("Digite 0 ou mais.")

                except ValueError:
                     print("Digite um número válido.")

            return Estudio(vagas)

def pegar_parcelas():

    while True:
         
        try:

            parcelas = int(input("Em quantas parcelas deseja pagar o contrato? (1 a 5): "))

            if 1 <= parcelas <= 5:
                return parcelas
            
            print("Digite um valor entre 1 e 5.")

        except ValueError:
             print("Digite um número válido.")