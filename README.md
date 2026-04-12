# Orçamento de Aluguel — Simulador Web com Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![Architecture](https://img.shields.io/badge/Architecture-OOP-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

Aplicação web desenvolvida em Python com foco em **orientação a objetos**, responsável por simular orçamentos de aluguel com base em regras de negócio reais de uma imobiliária.

O sistema permite ao usuário escolher o tipo de imóvel, personalizar características e obter automaticamente o valor mensal, parcelas contratuais e custo anual, além de gerar um relatório em CSV.

> Projeto desenvolvido como trabalho acadêmico da disciplina de Programação 
> Orientada a Objetos (ADS — UniFECAF), expandido com interface web via Flask 
> e comportamento dinâmico em JavaScript, indo além do escopo original exigido.

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
    - Lógica específica para estúdios (vagas diferenciadas)
- Cálculo do contrato imobiliário parcelado (até 5x)
- Geração de arquivo `.csv` com 12 meses de orçamento
- Interface web com formulário dinâmico (UX inteligente)
- Exibição de valores formatados em Real (R$)

---

### Tecnologias utilizadas

- Python
- Flask
- HTML
- CSS
- JavaScript
- Programação Orientada a Objetos (OOP)

---

### Estrutura do projeto

```bash
oop-rental-budget-simulator/
│
├── app.py
├── config.py
│
├── models/
│   ├── imovel.py
│   ├── apartamento.py
│   ├── casa.py
│   └── estudio.py
│
├── services/
│   ├── calculadora.py
│   ├── input_service.py
│   ├── orcamento_service.py
│   ├── output_service.py
│   └── exportador_csv.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
```

---

### Como executar o projeto

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
pip install flask
```

4. Executar aplicação

```bash
python app.py
```

5. Acessar no navegador

```bash
http://127.0.0.1:5000/
```

---

### Exemplo de saída

O sistema gera um arquivo `.csv` com:
- 12 meses de aluguel
- Parcelas do contrato distribuídas corretamente
- Total anual

---

### Diferenciais do projeto

- Separação clara de responsabilidades (arquitetura em camadas)
- Aplicação de regras de negócio reais
- Integração backend + frontend
- Interface com comportamento dinâmico (UX)
- Código estruturado com foco em escalabilidade

---

### Possíveis melhorias futuras

- Persistência em banco de dados
- API com FastAPI
- Interface mais avançada
- Deploy em ambiente web

---

### Autora
Marinize Santana