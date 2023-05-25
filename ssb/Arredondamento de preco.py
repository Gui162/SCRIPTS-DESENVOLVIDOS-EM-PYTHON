import pyautogui
from time import sleep
from math import trunc
from re import sub  #subistitui os caracteres q eu quero no caso ta removendo
numeros = []
remover = "[R$:]"
while True:
    entrada = input("Por favor, digite um número (ou 'fim' para encerrar): ").replace(',','.')
    num = sub(remover, "", entrada)

    if num == "FIM" or num == "fim" or num == "fin" or num == "FIM" or num == "fim":
        break

    try:
        num = float(num)
        num_inteiro = trunc(num)
        flutuante = num - num_inteiro

        if flutuante >= 0.59:
            flutuante = 0.9
            arredondado = flutuante+ num_inteiro
        else:
            flutuante = 0.5
            arredondado = flutuante+ num_inteiro
    except ValueError:
        print("--------------------------------------------------------------_--------------")
        print(f'Voce inseriu "{num}" que nao é um numero e Tambem nao é comando para encerrar')
        print("--------------------------------------------------------------_--------------")
        continue

    numeros.append(arredondado)

print("\n")
print("\n")
print("---------------------------------------------------------------------------------")
print("voce ja arredondou todos os valores!! voce quer inserir eles automaticamente ??")
print("---------------------------------------------------------------------------------")
inserir = input("Escreva (SIM) para colocar os preços automaticos \nEscreva (NAO) apena ter a lista de preços com virgula \nRESPOSTA: ")
if inserir == "SIM" or inserir == "sim" or inserir == "sin" or inserir == "(SIM)":
    print("o programa vai começar em 5 segungos")
    sleep(1)
    print("4")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    print("começou")

    for valores in numeros:
        numero_str = str(valores)

        # Copia o número para a área de transferência
        pyautogui.write(numero_str)

        # Pressiona a tecla "seta para baixo" para mover para a próxima linha da lista
        pyautogui.press('down')

else:
    numeros_string = ",".join(str(num) for num in numeros)
    print(numeros_string)

sleep(9999999)

