print (" BEM VINDO AO CONVERSOR DE NOTAS ")                                         
nota1 = float(input(" DIGITE A SUA PRIMEIRA NOTA: "))                # estava com 1 parenteses a menos
nota2 = float(input(" DIGITE A SUA SEGUNDA NOTA: "))               
nota3 = float(input(" DIGITE A SUA TERCEIRA NOTA: "))              
 
media = ( nota1 + nota2 + nota3) /3                
print("A sua média é: ", media)

if media >=7:                             # estava sem o ":"
    print ("VOCE FOI APROVADO")

else:                                    # estava sem o ":"
    print ("VOCE FOI REPROVADO")         # estava sem o parenteses final