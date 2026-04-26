# 🌱 Sistema Fuzzy Mamdani para Controle de Irrigação

## 📌 Descrição do Projeto

Este projeto implementa um Sistema de Inferência Fuzzy (FIS) utilizando o método de Mamdani para controle de irrigação baseado em três variáveis de entrada:

- Umidade do solo
- Temperatura
- Luminosidade

A saída do sistema é a intensidade de irrigação (%), calculada por meio de inferência fuzzy e defuzzificação.

---

## 🧠 Conceito Utilizado

O sistema segue as etapas clássicas de um sistema fuzzy baseado em regras:

1. Fuzzificação
2. Aplicação das regras
3. Inferência fuzzy (Mamdani - max-min)
4. Agregação das saídas
5. Defuzzificação (centroide)

---

## 📂 Estrutura do Projeto

fuzzy_mamdani/
│
├── notebooks/
│   └── sistema_fuzzy_mamdani.ipynb
│
├── src/
│   ├── main.py
│   ├── sistema_fuzzy_mamdani.py
│   └── graficos.py
│
├── resultados/
│   └── graficos/
│
├── README.md
└── requirements.txt

---

## 🔧 Tecnologias Utilizadas

- Python 3.x
- NumPy
- Matplotlib

---

## 📥 Instalação

```bash
git clone <seu-repositorio>
cd fuzzy_mandani
pip install -r requirements.txt
```

---

## ▶️ Como Executar

```bash
python src/main.py
```

---

## 📊 Saídas do Sistema

- Gráficos das funções de pertinência
- Saída fuzzy agregada
- Valor final defuzzificado

Os resultados são salvos em:

resultados/graficos/

---

## 🧪 Testes

```python
testes = [
    (20, 35, 90),
    (55, 22, 50),
    (90, 15, 20)
]
```

---

## 🔍 Etapas do Sistema

### Fuzzificação
Transforma valores numéricos em graus de pertinência (0 a 1)

### Regras Fuzzy
SE umidade é baixa E temperatura é alta ENTÃO irrigação é alta

### Inferência
Uso de operador mínimo (AND)

### Agregação
Uso de operador máximo

### Defuzzificação
Centroide:
Saída = ∑(x * μ(x)) / ∑μ(x)

---


## 👨‍💻 Autor

João Francisco Teles da Silva
