def calcular_salario(cargo: str) -> float:
    """
    Calcula o salário com base no cargo utilizando estruturas de decisão (if/elif/else).
    Retorna o salário em reais.
    """
    cargo = cargo.strip().title()  # Normaliza o cargo (ex: "gerente" -> "Gerente")
    
    if cargo == "Diretor":
        return 30000.0
    elif cargo == "Gerente":
        return 20000.0
    elif cargo == "Coordenador":
        return 12000.0
    elif cargo == "Analista":
        return 8000.0
    elif cargo == "Assistente":
        return 4000.0
    elif cargo == "Auxiliar":
        return 2000.0
    else:
        # Valor padrão caso o cargo não seja reconhecido
        print(f"Aviso: Cargo '{cargo}' não encontrado. Salário definido como R$ 0,00.")
        return 0.0


def main():
    # Lista de colaboradores já cadastrados (pré-definida no código)
    colaboradores = [
        {"nome": "João Silva", "cargo": "Diretor"},
        {"nome": "Maria Souza", "cargo": "Gerente"},
        {"nome": "Pedro Santos", "cargo": "Coordenador"},
        {"nome": "Ana Costa", "cargo": "Analista"},
        {"nome": "Carlos Oliveira", "cargo": "Assistente"},
        {"nome": "Fernanda Lima", "cargo": "Auxiliar"},
        {"nome": "Lucas Pereira", "cargo": "Analista"},
        {"nome": "Juliana Rocha", "cargo": "Gerente"},
        {"nome": "Marcos Almeida", "cargo": "Assistente"},
        {"nome": "Beatriz Martins", "cargo": "Auxiliar"},
    ]
    
    # Calcula o salário de cada colaborador e adiciona ao dicionário
    for colab in colaboradores:
        colab["salario"] = calcular_salario(colab["cargo"])
    
    # ====================== EXIBIÇÃO DA TABELA ======================
    print("=" * 70)
    print(" " * 25 + "FOLHA DE PAGAMENTO")
    print("=" * 70)
    print(f"{'Nome':<25} {'Cargo':<15} {'Salário':>15}")
    print("-" * 70)
    
    for colab in colaboradores:
        # Formata o salário no padrão brasileiro (R$ 30.000,00)
        salario_formatado = f"R$ {colab['salario']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"{colab['nome']:<25} {colab['cargo']:<15} {salario_formatado:>15}")
    
    print("-" * 70)
    
    # ====================== CÁLCULOS GERAIS ======================
    quantidade_colaboradores = len(colaboradores)
    soma_total = sum(colab["salario"] for colab in colaboradores)
    media_salarial = soma_total / quantidade_colaboradores if quantidade_colaboradores > 0 else 0
    
    # Formatação dos valores totais
    total_formatado = f"R$ {soma_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    media_formatada = f"R$ {media_salarial:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    print(f"Quantidade total de colaboradores: {quantidade_colaboradores}")
    print(f"Soma total da folha salarial:     {total_formatado}")
    print(f"Média salarial dos colaboradores: {media_formatada}")
    print("=" * 70)


# Ponto de entrada do programa
if __name__ == "__main__":
    main()