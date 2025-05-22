import pandas as pd
import numpy as np

def gerar_dados(num):
    return pd.DataFrame({
        "ID": np.arange(1, num + 1),
        "Código (SKU)": [f"SKU{np.random.randint(10000, 99999)}" for _ in range(num)],
        "Descrição": [f"Produto {i}" for i in range(1, num + 1)],
        "Unidade": np.random.choice(["UN", "CX", "PC"], num),
        "Classificação fiscal": np.random.randint(10000000, 99999999, num),
        "Origem": np.random.choice(["Nacional", "Importado"], num),
        "Preço": np.round(np.random.uniform(10, 500, num), 2),
        "Valor IPI fixo": np.round(np.random.uniform(0, 50, num), 2),
        "Situação": np.random.choice(["Ativo", "Inativo"], num),
        "Estoque": np.random.randint(0, 1000, num),
        "Preço de custo": np.round(np.random.uniform(5, 400, num), 2),
        "Cód do Fornecedor": np.random.randint(1000, 9999, num),
        "Fornecedor": [f"Fornecedor {i}" for i in range(1, num + 1)],
        "Localização": [f"A{i}" for i in range(1, num + 1)],
        "Estoque máximo": np.random.randint(500, 2000, num),
        "Estoque mínimo": np.random.randint(10, 100, num),
        "Peso líquido (Kg)": np.round(np.random.uniform(0.1, 10, num), 2),
        "Peso bruto (Kg)": np.round(np.random.uniform(0.2, 12, num), 2),
        "GTIN/EAN": [str(np.random.randint(10**11, 10**12 - 1, dtype=np.int64)) for _ in range(num)],
        "GTIN/EAN tributável": [str(np.random.randint(10**11, 10**12 - 1, dtype=np.int64)) for _ in range(num)],
        "Categoria": np.random.choice(["Beleza", "Saúde", "Bem-estar"], num),
        "Marca": np.random.choice(["Marca A", "Marca B", "Marca C"], num),
        "Garantia": np.random.randint(1, 24, num),
        "Sob encomenda": np.random.choice(["Sim", "Não"], num),
        "Preço promocional": np.round(np.random.uniform(5, 450, num), 2),
        "Dias para preparação": np.random.randint(1, 10, num),
        "Controlar lotes": np.random.choice(["Sim", "Não"], num),
        "Unidade por caixa": np.random.randint(1, 50, num),
        "Markup": np.round(np.random.uniform(1.2, 2.5, num), 2),
        "Permitir inclusão nas vendas": np.random.choice(["Sim", "Não"], num)
    })

# Criar três planilhas com 500 produtos cada
df1, df2, df3 = gerar_dados(500), gerar_dados(500), gerar_dados(500)

# Salvar em um arquivo Excel
output_path = "produtos_aleatorios.xlsx"
with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    df1.to_excel(writer, sheet_name="Produtos_1", index=False)
    df2.to_excel(writer, sheet_name="Produtos_2", index=False)
    df3.to_excel(writer, sheet_name="Produtos_3", index=False)

print(f"Arquivo gerado: {output_path}")
