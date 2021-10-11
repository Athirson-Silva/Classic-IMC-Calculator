height= float (input("Insira sua altura  em metros: "))
weight= float (input("Insira seu peso em kilos: "))

imc = weight/(height*height)

print(f"Seu IMC é: {imc:.2f}")

if(imc<10):
    classificacao="Desnutrição Grau V"
elif(imc<=12.9):
    classificacao="Desnutrição Grau IV"
elif(imc<=15.9):
    classificacao="Desnutrição Grau III"
elif(imc<=16.9):
    classificacao="Desnutrição Grau II"
elif(imc<=18.4):
    classificacao="Desnutrição Grau I"
elif(imc<=24.9):
    classificacao="Normal"
elif(imc<=29.9):
    classificacao="Pré-obesidade"
elif(imc<=34.5):
    classificacao="Obesidade Grau I"
elif(imc<=39.9):
    classificacao="Obesidade Grau II"
else:
    classificacao="Obesidade Grau III"

print(f"E seu estado nutricional é: {classificacao}")
