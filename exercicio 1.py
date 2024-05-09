print ("BEM VINDO")
n1 = int(input("DIGITE UM NUMERO POSITIVO: "))
if n1 < 0:
    print("O NUMERO NAO É POSITIVO" )

fatorial = 1
for i in range(1, n1 + 1):
    fatorial *= i
    print ("O número fatorial de",n1, "é",fatorial)
    