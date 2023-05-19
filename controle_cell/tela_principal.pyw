from tkinter import *
from tkinter import ttk

cor0 = "#191b2b" #fundo
cor1 = "#0c8ffa" #azul claro
cor2 = "#ffffff" #branco
cor3 = "#0c24fa" #azul escuro
cor4 = "#262942" #fundo mais claro


def tela_principal():
    global janela
    janela.destroy()
    janela = Tk()
    janela.title("Calculo de Frete")
    janela.geometry("800x600")
    janela.configure(bg=cor0)
    janela.resizable(width=False,height=False)

    #_________abre sempre no centro da tela____________
    # Define as coordenadas para o canto superior esquerdo
    x = 555
    y = 80
    # Define a posição da janela
    janela.geometry(f"+{x}+{y}")


    #_______________separação padrao de tela______________________
    frame_cima = Frame(janela, width=800, height=60, bg=cor0)
    frame_cima.place(x=0,y=0)

    frame_baixo = Frame(janela, width=800, height=300, bg=cor0)
    frame_baixo.place(x=0,y=60)

    #_______________________telas______________________________
    nome_cima = Label(frame_cima,width=36, height=0, text="CONTROLE DE CELULARES", fg=cor2, bg=cor0, font="calibri 32 bold")
    nome_cima.place(x=0,y=0)

    botao_cadastrar = Button(frame_baixo, text="CADASTRAR UM\nNOVO NUMERO",width=20, height=2, fg=cor2, bg=cor3, font="calibri 23 bold", command=tela_cadastrar)
    botao_cadastrar.grid(row=2, column=1, padx=49, pady=100)

    botao_alterar = Button(frame_baixo, text="ALTERAR NUMERO\nEXISTENTE",width=20, height=2, fg=cor2, bg=cor3, font="calibri 23 bold")
    botao_alterar.grid(row=2, column=2, padx=10, pady=100)

    frame_exportar = Frame(janela, width=800, height=290, bg=cor0)
    frame_exportar.place(x=0,y=360)

    botao_exportar = Button(frame_exportar, text="EXPORTAR DADOS EXISTENTES ",width=35, height=1, fg=cor2, bg=cor3, font="calibri 23 bold")
    botao_exportar.place(x=115,y=50)

    janela.mainloop()

def tela_cadastrar():
    global janela
    janela.destroy()
    janela = Tk()
    janela.title("Calculo de Frete")
    janela.geometry("800x600")
    janela.configure(bg=cor0)
    janela.resizable(width=False,height=False)

    #_________abre sempre no centro da tela____________
    # Define as coordenadas para o canto superior esquerdo
    x = 555
    y = 80
    # Define a posição da janela
    janela.geometry(f"+{x}+{y}")


    #_______________separação padrao de tela______________________
    frame_cima = Frame(janela, width=800, height=60, bg=cor0)
    frame_cima.place(x=0,y=0)

    frame_baixo = Frame(janela, width=800, height=300, bg=cor0)
    frame_baixo.place(x=0,y=60)

    #_______________________telas______________________________
    texto_nome = Label(frame_baixo, text="COLOQUE O NOME DA PESSOA:", fg=cor1, bg=cor0, font="calibri 20 bold")
    texto_nome.grid(row=0, column=0, padx=50, pady=10)

    entrada_nome = Entry(frame_baixo, fg=cor2, justify=CENTER, bg=cor4, font="calibri 20 bold")
    entrada_nome.grid(row=0, column=1, padx=0, pady=10)

    texto_numero = Label(frame_baixo, text="COLOQUE O NUMERO DA PESSOA:", fg=cor1, bg=cor0, font="calibri 20 bold")
    texto_numero.grid(row=2, column=0, padx=50, pady=0)

    formato_numero = Label(frame_baixo, text="(00) 00000-0000", fg=cor1, bg=cor0, font="calibri 10 bold")
    formato_numero.grid(row=3, column=1, padx=0, pady=0)

    entrada_numero = Entry(frame_baixo, fg=cor2, justify=CENTER, bg=cor4, font="calibri 20 bold")
    entrada_numero.grid(row=2, column=1, padx=0, pady=0)

    frame_cadastrar = Frame(janela, width=800, height=290, bg=cor0)
    frame_cadastrar.place(x=0,y=360)

    botao_cadastrar = Button(frame_cadastrar, text="CADASTRAR UM NOMO NUMERO ",width=35, height=1, fg=cor2, bg=cor3, font="calibri 23 bold")
    botao_cadastrar.place(x=115,y=50)
    volta = PhotoImage(file="volta.png")
    botao_voltar = Button(frame_cima, image=volta ,width=50, height=50, bg=cor3, command=tela_principal) #botao voltar
    botao_voltar.place(x=0,y=0)

    janela.mainloop()
























#=========================================================================== tela principal descartavel ==============================================
janela = Tk()
janela.title("Calculo de Frete")
janela.geometry("800x600")
janela.configure(bg=cor0)
janela.resizable(width=False,height=False)

#_________abre sempre no centro da tela____________
# Define as coordenadas para o canto superior esquerdo
x = 555
y = 80
# Define a posição da janela
janela.geometry(f"+{x}+{y}")


#_______________separação padrao de tela______________________
frame_cima = Frame(janela, width=800, height=60, bg=cor0)
frame_cima.place(x=0,y=0)

frame_baixo = Frame(janela, width=800, height=300, bg=cor0)
frame_baixo.place(x=0,y=60)

#_______________________telas______________________________

nome_cima = Label(frame_cima,width=36, height=0, text="CONTROLE DE CELULARES", fg=cor2, bg=cor0, font="calibri 32 bold")
nome_cima.place(x=0,y=0)

botao_cadastrar = Button(frame_baixo, text="CADASTRAR UM\nNOVO NUMERO",width=20, height=2, fg=cor2, bg=cor3, font="calibri 23 bold", command=tela_cadastrar)
botao_cadastrar.grid(row=2, column=1, padx=49, pady=100)

botao_alterar = Button(frame_baixo, text="ALTERAR NUMERO\nEXISTENTE",width=20, height=2, fg=cor2, bg=cor3, font="calibri 23 bold")
botao_alterar.grid(row=2, column=2, padx=10, pady=100)

frame_exportar = Frame(janela, width=800, height=290, bg=cor0)
frame_exportar.place(x=0,y=360)

botao_exportar = Button(frame_exportar, text="EXPORTAR DADOS EXISTENTES ",width=35, height=1, fg=cor2, bg=cor3, font="calibri 23 bold")
botao_exportar.place(x=115,y=50)

janela.mainloop()