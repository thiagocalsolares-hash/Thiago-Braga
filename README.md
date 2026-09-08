altura = float(input("Informe sua altura para o calculo de IMC:"))
peso = float(input("Informe seu peso para o calculo de IMC:"))
 
altura_quadrado = altura ** 2 # eleva a altura ao quadrado
 
imc = peso / altura_quadrado # calcula o IMC da pessoa
 
print(f"{imc:.2f}")
 
if imc < 18.5:
    print("Abaixo do peso ideal")
elif imc < 25.00:
    print("Peso ideal")
elif imc < 30.00:
    print("sobrepeso")
else:
    print("Obesidade")
