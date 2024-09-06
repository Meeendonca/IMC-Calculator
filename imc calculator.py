nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))
altura=float(input("Digite sua altura(em metros): "))
peso=float(input("Digite seu peso(em kg): "))
imc=peso/(altura**2)
if imc<18.5:
   classificacao="Abaixo do Peso"
elif imc<24.9:
   classificacao="Peso Normal"
elif imc<29.9:
   classificacao="Sobrepeso"
elif imc<34.9:
   classificacao="Obesidade grau 1"
elif imc<39.9:
   classificacao="Obesidade grau 2"
else:
   classificacao="Obesidade grau 3"
print(f"Nome:{nome}")
print(f"Idade:{idade}")
print(f"Altura:{altura}")
print(f"Peso:{peso}")
print(f"IMC:{imc:.2f}")
print(f"Classificação:{classificacao}")



