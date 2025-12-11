from tkinter import *
import sys
from database import Funcs
# cores                # ff ff 00 = 2 total de vermelho + 2 total de verde = amarelo
# RGB #ff0000          # 00 00 00
                       # R  G  B
# Red #fff000
# Gren  
# Blue
class Janela_Login(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("310x330")
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')
        self.db_funcs = Funcs()
        self.db_funcs.criar_tables()
        self.login()
        """
        PROBLEMA ERA NÂO CONSEGUIR FAZER A CONEXÂO DEVIDA
        SUBSTITUÍ:
        Funcs.criar_tables
        COMO FAZER:
            Crie uma instância da classe Funcs
        self.db_funcs = Funcs() 
        
            Chamar o método de instância
        self.db_funcs.criar_tables() 
        
        self.login()
        """
    def cadastrar(self):
        Janela_Login.withdraw(self)
        win = Janela_Cadastro()
    def fechar_tudo(self):
        """Fecha todas as janelas e encerra o programa."""
        self.destroy()
        sys.exit(0)
    def login(self):
        """Identifica o fechamento(x)"""
        self.protocol("WM_DELETE_WINDOW", self.fechar_tudo)
        login = Label(self, text="LOGIN", font="bold 35", pady=10)
        login.place(x=5, y=0)
        email_label = Label(self, anchor=NE, text=f"Email ", font="16")
        email_label.place(x=5, y=100)
        Label(self, text='*', font="16", fg="#ff0000").place(x=55, y=100)
        email_entry = Entry(self, width="40", relief="solid")
        email_entry.place(x=5, y=130)
        senha_label = Label(self, anchor=NE, text="Senha ", font="16")
        senha_label.place(x=5, y=160)
        Label(self, text='*', font="16", fg="#ff0000").place(x=55, y=160)
        senha_entry = Entry(self, width="40", relief="solid")
        senha_entry.place(x=5, y=190)
        self.linha_divisoria()
        # Interações de login/Cadastro
        botao = Button(self, text="ENTRAR", bg="#6a6666", width="15")
        botao.place(x=5, y=230)
        botao_cadastro = Button(self, text="Não tem login?", bg="#ffffff", bd=0, activeforeground="#ffffff", width="15", command=self.cadastrar)
        botao_cadastro.place(x=130, y=230)
    def linha_divisoria(self):
        frame_cima = Frame(self, width=350, height=5, bg="#50504d", relief="flat")
        frame_cima.place(x=5, y=60)
class Janela_Cadastro(Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro")
        self.geometry("310x330")
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')
        self.cadastro()
    def fechar_tudo(self):
        """Fecha todas as janelas e encerra o programa."""
        self.destroy()
        sys.exit(0)
    def cadastro(self):
        """Identifica o fechamento(x)"""
        self.protocol("WM_DELETE_WINDOW", self.fechar_tudo)
        cadastro = Label(self, text="CADASTRO", font="bold 35")
        cadastro.place(x=5, y=5)
        # Dividindo a tela
        frame_cima = Frame(self, width=350, height=5, bg="#4e0000", relief="flat")
        frame_cima.place(x=5, y=65)
        #nome
        nome = Label(self, anchor=NE, text="Nome ", font="16")
        nome.place(x=5, y=100)
        Label(self, text='*', font="16", fg="#ff0000").place(x=55, y=100)
        campo_nome = Entry(self, width="40", relief="solid")
        campo_nome.place(x=5, y=130)
        # Email
        email = Label(self, anchor=NE, text="Email ", font="16")
        email.place(x=5, y=155)
        Label(self, text='*', font="16", fg="#ff0000").place(x=55, y=155)
        campo_email = Entry(self, width="40", relief="solid")
        campo_email.place(x=5, y=185)
        # Senha
        Senha2 = Label(self, anchor=NE, text="Senha ", font="16")
        Senha2.place(x=5, y=210)
        Label(self, text='*', font="16", fg="#ff0000").place(x=55, y=210)
        campo_senha = Entry(self, width="40", relief="solid")
        campo_senha.place(x=5, y=230)
        # Botão de cadastro
        
        # Botão para ir para a tela de login
        botao_Login = Button(self, text="já tem login?", bg="#ffffff", bd=0, activeforeground="#ffffff", width="15", command=self.Logar)
        botao_Login.place(x=170, y=250)
    def Logar(self):
        Janela_Cadastro.destroy(self)
        Janela_Login().deiconify()
if __name__ == "__main__":
    win = Janela_Login()
    win.mainloop()