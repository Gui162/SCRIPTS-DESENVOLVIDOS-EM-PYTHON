import pyautogui

# Obtém a posição atual do mouse
posicao = pyautogui.position()

# Acessa as coordenadas x e y da posição
x = posicao.x
y = posicao.y

# Imprime as coordenadas x e y
print(f"A posição atual do mouse é: x = {x}, y = {y}")


pyautogui.moveTo(x=141,y=253)