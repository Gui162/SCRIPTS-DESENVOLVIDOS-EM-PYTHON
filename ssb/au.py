import pyautogui
from time import sleep

#identificação de imagem 
def position():
    pos = pyautogui.locateCenterOnScreen("mult.jpg", confidence= 0.9) #procura a imagem na tela e faz se tiver 90% de certeza vira true se nao retorna NONE
    if pos != None:
        print("encontrou multiplo")
        sleep(0.1)
        return True
#se nao achar a imagem continua
    else:
        print("sem multiplo")
        pyautogui.write("1")
        pyautogui.press("down")
    return False
def loop():
    while True:
        position()


loop()