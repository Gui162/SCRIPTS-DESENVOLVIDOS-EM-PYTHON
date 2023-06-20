import pyautogui
from time import sleep



corredor = 2
coluna = int(1)
while corredor<=22:
    print("començando")
    sleep(1)
    print("9")
    sleep(1)
    print("8")
    sleep(1)
    
    while coluna<=10:
        pyautogui.moveTo(x=99,y=134)  #incluir novo
        pyautogui.click()
        sleep(0.4)
        pyautogui.moveTo(x=154,y=199) #campo descricao
        pyautogui.click()
        sleep(0.4)
        pyautogui.write(f"CORREDOR {corredor}/{coluna}")
        coluna= coluna + 1
        sleep(0.4)
        pyautogui.hotkey('ctrl', 's')
        sleep(1.5)
    corredor = corredor + 1
    coluna = 1