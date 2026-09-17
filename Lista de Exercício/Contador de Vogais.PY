frase = input("\nDigite uma frase: ")
total = 0

for letra in frase.lower():
    if letra in "aeiou":
        total += 1

print(f"Total de vogais: {total}")