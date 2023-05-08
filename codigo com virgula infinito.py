import time
numeros = []
while True:
    num = input("Por favor, digite um número (ou 'fim' para encerrar): ")
    if num == "fim":
        break
    elif num == "FIM":
        break
    elif num == "FIN":
        break
    elif num == "fin":
        break
    elif num == "fiim":
        break
    numeros.append(num)
numeros_com_virgulas = [num + "," for num in numeros]
numeros_string = "".join(numeros_com_virgulas)
print(numeros_string)
time.sleep(500)
