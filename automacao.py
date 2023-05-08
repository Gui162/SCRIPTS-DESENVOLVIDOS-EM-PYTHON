import pyautogui
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

# Aguarda 5 segundos para dar tempo de mudar para a janela correta
print("o programa vai começar em 5 segungos")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("começou")

for valores in numeros:
    numero_str = str(valores)

    # Copia o número para a área de transferência
    pyautogui.write(numero_str)

    # Pressiona a tecla "seta para baixo" para mover para a próxima linha da lista
    pyautogui.press('down')

time.sleep(9999)
