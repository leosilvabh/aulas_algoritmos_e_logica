# Crie um programa que liste  
# os 10 primeiros pares
numero = int (input("digite o número fatorial"))
contador = 1
fatorial = 1
while contador <= numero: #while é enquanto
    fatorial = fatorial * contador
    contador += 1 # essa sintaxe é a mesma coisa que contador = contador + 1 
print (f"O fatorial de {numero} é: {fatorial}")