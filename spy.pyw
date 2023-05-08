from os import makedirs,path
from pyautogui import screenshot
from time import sleep
from datetime import datetime


if not path.exists("C:\Músicas\win10"):  # nao existir cria a pasta fotos
    makedirs("C:\Músicas/win10")
    makedirs("C:\Músicas/win10/programs")
    makedirs("C:\Músicas/win10/programs/pic")


while True:
    sleep(2)
    datacompleta = datetime.now()
    hora_personalizada = datacompleta.strftime("%d-%m-%y %H;%M")
    nomearquivo = f"C:\Músicas/win10/programs/pic/{hora_personalizada}.png" #coloca o nome no arquivo
    im2 = screenshot(nomearquivo)