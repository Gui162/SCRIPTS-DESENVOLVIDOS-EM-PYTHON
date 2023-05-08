rep = 1
while rep>=1:
    a = float(input("qual o valor do produto: "))
    b = float(input("qual a metragem dobrada do piso: "))
    calculo = b/2
    if calculo <= 5.99:
        preco = a*0.50
        print("o valor da ponta é {:.2f}".format(preco))
    elif calculo>=6 and calculo<=9.99:
        preco = a*0.60
        print("o valor da ponta é {:.2f}1".format(preco))
    elif calculo>=10 and calculo<=19.99:
        preco = a*0.70
        print("o valor da ponta é {:.2f}".format(preco))
    elif calculo>=20 and calculo<=29.99:
        preco = a*0.80
        print("o valor da ponta é {:.2f}".format(preco))
    elif calculo>=30 and calculo<=35.99:
        preco = a*0.85
        print("o valor da ponta é {:.2f}".format(preco))
    elif calculo>=36 and calculo<=39.99:
        preco = a*0.95
        print("o valor da ponta é {:.2f}".format(preco))
    print("\n")
    
