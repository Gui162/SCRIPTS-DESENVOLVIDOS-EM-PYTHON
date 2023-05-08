from tkinter import *
from tkinter import ttk

#cores
cor0 = "#ffffff" #branca / white
cor1 = "#444466" #preta / black
cor2 = "#9042f5" #roxo


janela = Tk()
janela.title("")
janela.geometry("500x295")
janela.configure(bg="white")

# ---------------- dividindo a janela em duas partes -----------

frame_cima = Frame(janela, width=500, height=50, bg=cor0, pady=0, padx=0, relief="flat")
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=180, bg=cor0, pady=0, padx=0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# ---------------- configurando frame cima -----------

app_nome = Label(frame_cima, text="Calculadora de IMC", width=23, height=1, padx=0, relief="flat", anchor="center", font=("Ivy 16 bold"), bg= cor0, fg=cor1)
app_nome.place(x=0,y=0)

app_linha = Label(frame_cima, text="", width=600, height=1, padx=0, relief="flat", anchor="center", font=("Ivy 1 bold"), bg= cor1, fg=cor1)
app_linha.place(x=0,y=40)

#______________________backend___________________

def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get())

    imc = peso / (altura**2)

    resultado = imc

    if resultado <= 18.5:
        l_resultado_texto["text"] = "O seu IMC é: Abaixo do Peso"
        
    elif resultado >= 18.5 and resultado <= 25:
        l_resultado_texto["text"] = "O seu IMC é Normal"

    elif resultado >= 25 and resultado <= 30:
        l_resultado_texto["text"] = "O seu IMC é Sobrepeso"

    else:
        l_resultado_texto["text"] = "O seu IMC é Obesidade"
    l_resultado["text"] = "{:.2f}".format(resultado)

# ---------------- configurando frame baixo -----------

#peso
l_peso = Label(frame_baixo, text="INSIRA SEU PESO", width=23, height=1, padx=0, relief="flat", anchor="center", font=("Ivy 10 bold"), bg= cor0, fg=cor1)
l_peso.grid(row=0, column=0, sticky=NSEW, padx=3, pady=10)

e_peso = Entry(frame_baixo,width=10 ,relief="solid", font=("Ivy 11 bold"), justify="center",)
e_peso.grid(row=0, column=1, sticky=NSEW, padx=3, pady=10)


#altura
l_altura = Label(frame_baixo, text="INSIRA SUA ALTURA", width=23, height=1, padx=0, relief="flat", anchor="center", font=("Ivy 10 bold"), bg= cor0, fg=cor1)
l_altura.grid(row=1, column=0, sticky=NSEW, padx=3, pady=10)

e_altura = Entry(frame_baixo,width=10 ,relief="solid", font=("Ivy 11 bold"), justify="center",)
e_altura.grid(row=1, column=1, sticky=NSEW, padx=3, pady=10)

#resultado
l_resultado = Label(frame_baixo, text="------", width=5, height=1, padx=6, pady=12, relief="flat", anchor="center", font=("Ivy 20 bold"), bg= cor2, fg=cor0)
l_resultado.place(x=350,y=10)

l_resultado_texto = Label(frame_baixo, text="", width=37, height=1, padx=6, pady=15, relief="flat", anchor="center", font=("Ivy 12 bold"), bg= cor0, fg=cor1)
l_resultado_texto.place(x=71,y=85)

#botao

b_calcular = Button(frame_baixo, command=calcular, text=("Calcular"), width=34, height=1, padx=0, pady=0, relief="raised", overrelief=SOLID, anchor="center",font="Ivy 15 bold", bg=cor2, fg=cor0)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=45, columnspan=20)






janela.mainloop()

