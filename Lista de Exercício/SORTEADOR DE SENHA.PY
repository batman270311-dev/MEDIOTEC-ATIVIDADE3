import random
import string

quantidade = int(input("\nQuantidade de caracteres: "))
caracteres = string.ascii_letters + string.digits
senha = ""

for i in range(quantidade):
    senha += random.choice(caracteres)

print("Senha gerada:", senha)