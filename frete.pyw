from tkinter import *
from tkinter import ttk

cor0 = "#323835" #cinza fundo
cor1 = "#00ff80" #verde letra
cor2 = "#071a10" #verde linha
cor3 = "#367354" #cor botao


janela = Tk()
janela.title("Calculo de Frete")
janela.geometry("600x400")
janela.configure(bg="gray")
janela.resizable(width=False,height=False)


#----------------------------divisao tela-------------------------------

frame_cima = Frame(janela, width=600, height=60, bg=cor0)
frame_cima.place(x=0,y=0)

frame_baixo = Frame(janela, width=600, height=360, bg=cor0)
frame_baixo.place(x=0,y=60)

#----------------------titulo de cima--------------------------------

nome_cima = Label(frame_cima, width=42, height=2, text="CALCULADORA FRETE", fg=cor1, bg=cor0, font="calibri 20 bold")
nome_cima.place(x=0,y=0)

app_linha = Label(frame_cima, text="", width=600,padx=10, pady=1, height=0, bg=cor2, fg=cor1)
app_linha.place(x=0,y=57)

#--------------------back end-------------------------------------
valor_virgula = ""
peso_virgula = ""
def frete():
    valor_vigula = str(entrada_valor.get()).replace(',','.')
    valor = float(valor_vigula)
    peso_virgula = str(entrada_peso.get()).replace(',','.')
    peso = float(peso_virgula)
    calculo = "%.2f" %((peso/1000)*valor)
    calculo_virgula = str(calculo).replace('.',',')
    resultado["text"] = ("R$:"+calculo_virgula)

#---------------------configurando corpo---------------------------


valor_tonelada = Label(frame_baixo, text="COLOQUE O VALOR DA TONELADA", fg=cor1, bg=cor0, font="calibri 14 bold")
valor_tonelada.grid(row=0, column=0, padx=10, pady=10)

entrada_valor = Entry(frame_baixo, fg=cor1, bg=cor0, font="calibri 20 bold")
entrada_valor.grid(row=0, column=1, padx=10, pady=10)

valor_peso = Label(frame_baixo, text="COLOQUE O PESO DA NOTA", fg=cor1, bg=cor0, font="calibri 14 bold")
valor_peso.grid(row=2, column=0, padx=10, pady=10)

entrada_peso = Entry(frame_baixo, fg=cor1, bg=cor0, font="calibri 20 bold")
entrada_peso.grid(row=2, column=1, padx=10, pady=10)

#-------------------botao------------------

botao = Button(frame_baixo, text="CALCULAR", command=frete, fg=cor1, bg=cor3, font="calibri 30 bold")
botao.grid(row=3, column=1, padx=10, pady=90)

#-----------------resultado----------------

resultado = Label(frame_baixo, text="R$:00,00", fg=cor1, bg=cor0, font="calibri 30 bold")
resultado.grid(row=3, column=0, padx=10, pady=90)

janela.mainloop()