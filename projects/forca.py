import random

def jogo_da_forca():
    palavras = ["python", "programacao", "computador", "desenvolvimento"]
    palavra = random.choice(palavras)
    letras_descobertas = ["_"] * len(palavra)
    tentativas = 6
    letras_usadas = []

    print("=== JOGO DA FORCA ===")
    
    while tentativas > 0 and "_" in letras_descobertas:
        print(f"\nPalavra: {''.join(letras_descobertas)}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras usadas: {', '.join(letras_usadas)}")

        letra = input("Digite uma letra: ").lower()

        if letra in letras_usadas:
            print("Você já usou essa letra!")
            continue
        
        letras_usadas.append(letra)

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
            print("Acertou!")
        else:
            tentativas -= 1
            print("Errou!")
    
    if "_" not in letras_descobertas:
        print(f"\nParabéns! Você venceu! A palavra era: {palavra}")
    else:
        print(f"\nGame Over! A palavra era: {palavra}")

jogo_da_forca()