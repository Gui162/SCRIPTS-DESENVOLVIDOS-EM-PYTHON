import pyautogui as py
import pandas as pd
from time import sleep
from pyperclip import copy
dados = pd.read_excel("produtos_negrao_sao_sebastiao.xlsx")

codigo_float = dados["sku_ss"].iloc[0]
codigo = str(codigo_float).rstrip(".0")
nome = dados["nome_erp"].iloc[0]
altura = str((dados["altura"].iloc[0])/100)
comprimento = str((dados["comprimento"].iloc[0])/100)
largura = str((dados["largura"].iloc[0])/100)
peso = str(dados["peso"].iloc[0])
descricao = dados["descricao"].iloc[0]


#pesquisa do codigo
py.moveTo(x=1988, y=130)
py.click()
sleep(0.03)
py.moveTo(x=1986, y=208)
py.click()
sleep(1)
py.write(codigo)
sleep(0.01)
py.press("enter")
sleep(0.01)
py.moveTo(x=2000, y=233)
sleep(0.01)
py.doubleClick()
py.moveTo(x=2460, y=195)
sleep(0.6)
py.click()

#tamanhos
py.moveTo(x=2460, y=272)
py.click()
sleep(0.01)
py.write(comprimento)
sleep(0.01)
py.press("tab")
py.click()
py.write(largura)
sleep(0.001)
py.press("tab")
sleep(0.001)
py.write(altura)
sleep(0.01)

#peso
py.moveTo(x=2055, y=250)
py.click()
py.write(peso)
sleep(0.01)
py.press("tab")
sleep(0.001)
py.write(peso)
sleep(0.02)

#aba ecomerce
py.moveTo(x=2800, y=195)
sleep(0.01)
py.click()
sleep(0.02)
py.moveTo(x=2350, y=342)
py.click()
copy(nome)
py.hotkey('ctrl', 'v')
sleep(0.01)
py.moveTo(x=2350, y=730)
py.click()
sleep(0.01)
py.write(descricao)
sleep(0.01)