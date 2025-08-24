#Esse é um projeto criado no ano de 2024 sendo o primero projeto de calculadora sem POO
from tkinter import *

co = 'white'
co1 = 'gray'
co2 = 'LightGray'
co3 = 'green'
co4 = 'LightGreen'

tela = "0"
def div():
    print("hello world")
    global tela
    # Adiciona o operador "x" à tela
    tela += "/"
    if len(tela) > 1:
        lista = [
            (280-len(tela*22),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)
    if len(tela) > 4:
        lista = [
            (280-len(tela*25),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)
    if len(tela) > 7:
        lista = [
            (280-len(tela*28),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)    
    mostrar.config(text=tela)
def vezes():
    print("hello world")
    global tela
    # Adiciona o operador "x" à tela
    tela += "*"
    if len(tela) > 1:
        lista = [
            (280-len(tela*22),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)
    if len(tela) > 4:
        lista = [
            (280-len(tela*25),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)
    if len(tela) > 7:
        lista = [
            (280-len(tela*28),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)    
    mostrar.config(text=tela)
def adição():
    print("hello world")
    global tela
    # Adiciona o operador "+" à tela
    tela += "+"
    if len(tela) > 1:
        lista = [
            (280-len(tela*22),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)
    if len(tela) > 4:
        lista = [
            (280-len(tela*25),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)
    if len(tela) > 7:
        lista = [
            (280-len(tela*28),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)    
    mostrar.config(text=tela)
def subtração():
    global tela
    # Adiciona o operador "+" à tela
    tela += "-"
    if len(tela) > 1:
        lista = [
            (280-len(tela*22),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)
    if len(tela) > 4:
        lista = [
            (280-len(tela*25),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)
    if len(tela) > 7:
        lista = [
            (280-len(tela*29),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)
    mostrar.config(text=tela)
def calcular():
    global tela
    try:
        # Avalia a expressão na tela e atualiza com o resultado
        resultado = eval(tela)
        tela = str(resultado)
        print(resultado)
        if int(resultado) < 1 > 0:
            mostrar.place(x=185, y=5)
        if int(resultado) > 1 < 9:
            mostrar.place(x=280, y=5)
        if int(resultado) > 9:
            mostrar.place(x=230, y=5) 
        if int(resultado) > 99:
            mostrar.place(x=225, y=5)
        if int(resultado) > 999:
            mostrar.place(x=195, y=5)
        mostrar.config(text=tela)
                
    except Exception as e:
        tela = "Erro"
        mostrar.config(text=tela)
        print(f"Erro ao calcular: {e}")

def limpar_tela():
    global tela
    tela = "0"
    mostrar.config(text=tela)
    mostrar.place(x=280, y=5)
def atualizar_tela(valor):
    global tela
    if tela == "0":
        tela = str(valor)  # Se for o primeiro dígito, substitui "0" pelo valor
        print(len(tela))
    else:
        tela += str(valor)  # Caso contrário, concatena o valor ao existente
        print(len(tela))
    mostrar.config(text=tela)  # Atualiza o texto do Label com o valor atualizado  # Apenas para verificar no console, você pode substituir por lógica de atualização da tela da calculadora
    if len(tela) > 1:
        lista = [
            (280-len(tela*22),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)
    if len(tela) > 4:
        lista = [
            (280-len(tela*25),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)
    if len(tela) > 7:
        lista = [
            (280-len(tela*28),5),
        ]
        for (x,y) in lista:
            mostrar.place(x=x, y=y)


def criar_botao(root, texto, x, y, bg, ac, comand):
    return Button(root, text=texto, font="Bold 13", width=7, height=2, bd=False, bg=bg, activebackground=ac, command=lambda: comand(texto))

root = Tk()
root.title('Calculadora')
root.geometry('320x354')
root.resizable(False, False)

mostrar = Label(root, text=tela, font="Bold 40")
mostrar.place(x=280, y=5)

CE = Button(root, text="CE", font="Bold 13", width=7, height=2, bd=False, bg=co2, activebackground=co,command=limpar_tela)
CE.place(x=10, y=80)

C = Button(root, text="C", font="Bold 13", width=7, height=2, bd=False, bg=co2, activebackground=co,command=limpar_tela)
C.place(x=85, y=80)

apagar = Button(root, text="del", font="Bold 13", width=7, height=2, bd=False, bg=co2, activebackground=co,command=limpar_tela)
apagar.place(x=160, y=80)

Mm = Button(root, text="-/+", font="Bold 13", width=7, height=2, bd=False, bg=co, activebackground=co1)
Mm.place(x=10, y=280)

virgula = Button(root, text=",", font="Bold 13", width=7, height=2, bd=False, bg=co, activebackground=co1)
virgula.place(x=160, y=280)

botao_num = [
    (7, 10, 130, co, co1),
    (8, 85, 130, co, co1),
    (9, 160, 130, co, co1),
    (4, 10, 180, co, co1),
    (5, 85, 180, co, co1),
    (6, 160, 180, co, co1),
    (1, 10, 230, co, co1),
    (2, 85, 230, co, co1),
    (3, 160, 230, co, co1),
    (0, 85, 280, co, co1),
    ("=", 235, 280, co3, co4),
    ("+", 235, 230, co2, co),
    ("-", 235, 180, co2, co),
    ("X", 235, 130, co2, co),
    ("/", 235, 80, co2, co)

]

# Função para lidar com o comando dos botões numéricos e de igual
def handle_button_click(valor):
    if isinstance(valor, int):  # Verifica se o valor é um número
        atualizar_tela(valor)
    elif valor == "=":
        # Implemente a lógica para realizar o cálculo quando "=" for pressionado
        calcular()
    elif valor == "+":
        adição()
    elif valor == "X":
        vezes()
    elif valor == "/":
        div()
    elif valor == "-":
        subtração()
    else:
        print(f"Botão não reconhecido: {valor}")

# Criar os botões numéricos e de igual
for (texto, x, y, bg, ac) in botao_num:
    if texto in {"+", "=", "-", "X", "/"}:
        Button(root, text=texto, font="Bold 13", width=7, height=2, bd=False, bg=bg, activebackground=ac,
               command=lambda t=texto: handle_button_click(t)).place(x=x, y=y)
    else:
        Button(root, text=texto, font="Bold 13", width=7, height=2, bd=False, bg=bg, activebackground=ac,
               command=lambda t=texto: handle_button_click(int(t))).place(x=x, y=y)


root.mainloop()
