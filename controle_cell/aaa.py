botao_cadastrar = Button(frame_baixo, text="CADASTRAR UM\nNOVO NUMERO",width=20, height=2, fg=cor2, bg=cor3, font="calibri 23 bold", command=tela_cadastrar)
botao_cadastrar.grid(row=2, column=1, padx=49, pady=100)

botao_alterar = Button(frame_baixo, text="ALTERAR NUMERO\nEXISTENTE",width=20, height=2, fg=cor2, bg=cor3, font="calibri 23 bold")
botao_alterar.grid(row=2, column=2, padx=10, pady=100)

frame_exportar = Frame(janela, width=800, height=290, bg=cor0)
frame_exportar.place(x=0,y=360)

botao_exportar = Button(frame_exportar, text="EXPORTAR DADOS EXISTENTES ",width=35, height=1, fg=cor2, bg=cor3, font="calibri 23 bold")
botao_exportar.place(x=115,y=50)

def tela_cadastrar():
    # Desliga a tela principal
    texto_nome = Label(frame_baixo, text="COLOQUE O NOME DA PESSOA:", fg=cor1, bg=cor0, font="calibri 20 bold")
    texto_nome.grid(row=0, column=0, padx=50, pady=10)
    
    # Resto do código
    # ...

tela_principal()

janela.mainloop()
