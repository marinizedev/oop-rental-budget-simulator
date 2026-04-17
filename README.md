# Orçamento de Aluguel — Simulador Web com Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![Architecture](https://img.shields.io/badge/Architecture-OOP-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

Aplicação web desenvolvida em Python com foco em **orientação a objetos**, responsável por simular orçamentos de aluguel com base em regras de negócio reais de uma imobiliária.

O sistema permite ao usuário escolher o tipo de imóvel, personalizar características e obter automaticamente o valor do aluguel, parcelas contratuais, o total mensal do orçamento e o total anual, além de gerar um relatório em CSV.

> Projeto desenvolvido como trabalho acadêmico da disciplina de Programação 
> Orientada a Objetos (ADS — UniFECAF), expandido com interface web via Flask,
> comportamento dinâmico em JavaScript e deploy em produção, indo além do escopo original proposto.

---

### Acesse online

**[simulador-aluguel.onrender.com](https://simulador-aluguel.onrender.com)**

---

### Funcionalidades

- Simulação de aluguel para:
    - Apartamentos
    - Casas
    - Estúdios
- Regras de negócio aplicadas automaticamente:
    - Acréscimo por número de quartos
    - Inclusão de vaga de garagem
    - Desconto para apartamentos sem crianças
    - Lógica específica para estúdios (pacote mínimo de vagas e adicionais)
- Cálculo do contrato imobiliário parcelado (até 5x)
- Geração de arquivo `.csv` com 12 meses de orçamento
- Interface web com formulário dinâmico (UX inteligente)
- Exibição de:
    - Valor do aluguel
    - Parcela do contrato
    - Total mensal do orçamento
    - Total anual
- Execução alternativa via terminal (CLI)

---

### Tecnologias utilizadas

- Python
- Flask
- HTML
- CSS
- JavaScript
- Programação Orientada a Objetos (OOP)

---

### Arquitetura do projeto

O projeto foi estruturado em três camadas independentes e complementares:

**Camada 1 — Lógica de negócio (CLI)**
Núcleo da aplicação. Contém as entidades, regras de negócio, serviços e orquestrador via terminal. Funciona de forma completamente independente da interface web.

**Camada 2 — Interface web local (Flask)**
Camada de apresentação que expõe a lógica de negócio via navegador, com formulário dinâmico e UX inteligente. Executa localmente via HTTP.

**Camada 3 — Deploy em produção (Render)**
A mesma aplicação Flask disponibilizada na internet, oferecendo acesso público sem necessidade de instalação local.

---

### Estrutura do projeto

```bash
oop-rental-budget-simulator/
│
├── app.py                  # Orquestrador web — rotas Flask
├── config.py               # Constantes e configurações globais
├── Procfile                # Configuração de deploy para o Render
│
├── cli/
│   └── main.py             # Orquestrador CLI — execução via terminal
│
├── models/
│   ├── imovel.py           # Classe base
│   ├── apartamento.py      # Herança + regras específicas
│   ├── casa.py             # Herança + regras específicas
│   └── estudio.py          # Herança + regras específicas
│
├── services/
│   ├── calculadora.py      # Lógica de contrato e parcelas
│   ├── input_service.py    # Entradas do usuário (CLI)
│   ├── orcamento_service.py # Geração do orçamento
│   ├── output_service.py   # Formatação e exibição dos resultados
│   └── exportador_csv.py   # Geração do relatório CSV
│
├── templates/
│   └── index.html          # Interface web
│
└── static/
    └── style.css           # Estilização
```

---

### Como executar o projeto

#### Opção 1 — Interface web (local)

1. Clonar o repositório

```bash
git clone https://github.com/marinizedev/oop-rental-budget-simulator.git
cd oop-rental-budget-simulator
```

2. Criar ambiente virtual (opcional, recomendado)

```bash
python -m venv venv
```

Ativar:

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

3. Instalar dependências

```bash
pip install -r requirements.txt
```

> **Nota:** o arquivo `requirements.txt` foi ajustado manualmente para 
> garantir compatibilidade entre Windows e Linux, removendo dependências
> específicas de sistema operacional que causavam conflito no deploy. 

4. Executar aplicação

```bash
python app.py
```

5. Acessar no navegador

```bash
http://127.0.0.1:5000/
```

#### Opção 2 — Terminal (CLI)

```bash
python -m cli.main
```

---

### Exemplo de saída

O sistema gera um arquivo `.csv` com:

- 12 meses de orçamento
- Parcelas do contrato distribuídas corretamente
- Valor do aluguel mensal
- Total mensal do orçamento

---

### Diferenciais do projeto

- Separação clara de responsabilidades (arquitetura em camadas)
- Aplicação de regras de negócio reais
- Integração backend + frontend
- Interface com comportamento dinâmico (UX)
- Código estruturado com foco em escalabilidade
- Cálculo do impacto mensal real (aluguel + contrato)
- Duas formas de execução: web e CLI
- Deploy em produção com acesso público

---

### Possíveis melhorias futuras

- Persistência em banco de dados
- API com FastAPI
- Interface mais avançada

---

### Autora

Marinize Santana