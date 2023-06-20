import pyautogui
from time import sleep



corredor = 14
coluna = int(1)
sleep(2)
while coluna<=10:
    #pyautogui.moveTo(x=99,y=134)  #incluir novo
    #yautogui.click()
    #pyautogui.moveTo(x=154,y=199) #campo descricao
    #pyautogui.click()
    #sleep(0.2)
    pyautogui.write(f"CORREDOR {corredor}/{coluna}")
    coluna= coluna + 1
    sleep(0.2)
    # pyautogui.moveTo(x=137,y=227) #campo nao
    # pyautogui.click()
    # sleep(0.2)
    # pyautogui.moveTo(x=141,y=253) #move pra o sim
    # pyautogui.click()
    #pyautogui.hotkey('ctrl', 's')
    pyautogui.press("down")
    sleep(1)