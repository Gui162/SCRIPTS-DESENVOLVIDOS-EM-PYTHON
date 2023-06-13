import pyautogui
from time import sleep

#identificação de imagem 
def position():
    pos = pyautogui.locateCenterOnScreen("identificacao_img\multi.jpg", confidence= 0.60) #procura a imagem na tela e faz se tiver 90% de certeza vira true se nao retorna NONE
    if pos != None:
        print("encontrou multiplo")
        pyautogui.press("enter")
        sleep(0.1)
        return True
#se nao achar a imagem continua
    else:
        print("sem multiplo")
        pyautogui.write("1")
        sleep(0.01)
        pyautogui.press("down")
        sleep(0.02)
    return False
def loop():
    while True:
        position()

sleep(5)
loop()