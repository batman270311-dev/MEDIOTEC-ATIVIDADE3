# EXERCÍCIO 1 - CALCULADORA DE IMC

nome = input("Nome: ")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / altura**2

print(f"\n{nome}, seu IMC é {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")