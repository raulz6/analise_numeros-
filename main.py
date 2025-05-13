def analisar_lista(lista):
    quantidade = len(lista)
    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / quantidade

    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]

    resultado = {
        "Quantidade": quantidade,
        "Maior": maior,
        "Menor": menor,
        "Média": media,
        "Pares": len(pares),
        "Ímpares": len(impares)
    }

    return resultado