from tkinter import *
from tkinter import ttk
from random import randint

cor0 = "#9e1114" #fundo
cor1 = "#a10025" #rosa
cor2 = "#ffffff" #braco
cor3 = "#54008c" #roxo


janela = Tk()
janela.title("te amo, amor")
janela.geometry("900x600")
janela.configure(bg=cor0)
janela.resizable(width=False,height=False)

sim_x = 300
sim_y = 200

def sim():
    botao_sim.place(x=randint(0, 700), y= randint(0, 400))

def nao():
    nome_baixo = Label(frame_baixo, width=41, height=0, text="A entao ta bao entao bilu", anchor="center", fg=cor2, bg=cor0, font="calibri 32 bold")
    nome_baixo.place(x=0,y=50)

frame_cima = Frame(janela, width=900, height=200, bg=cor0)
frame_cima.place(x=0,y=0)

frame_baixo = Frame(janela, width=900, height=700, bg=cor0)
frame_baixo.place(x=0,y=60)

nome_cima = Label(frame_cima, width=41, height=0, text="QUER CASAR COMIGO ??", anchor="center", fg=cor2, bg=cor0, font="calibri 32 bold")
nome_cima.place(x=0,y=0)


botao_sim = Button(frame_baixo, text="  SIM  ",command=sim, fg=cor1, bg=cor2, font="calibri 30 bold")
botao_sim.place(x=sim_x,y=sim_y)

botao_nao = Button(frame_baixo, text="  NÃO  ",command=nao, fg=cor1, bg=cor2, font="calibri 30 bold")
botao_nao.place(x=470,y=200)


janela.mainloop()