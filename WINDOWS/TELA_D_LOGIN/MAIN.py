from tkinter import *
from tkinter import messagebox
from database import Usuario, db

co1 = "white"
co2 = "gray"
co = "black"

def conectar_banco():
    try:
        db.connect()
        db.create_tables([Usuario], safe=True)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")

def cadastrar_usuario(janela_cadastro, campo_email, campo_senha,campo_nome):
    try:
        nome = campo_nome.get()
        email = campo_email.get()
        senha = campo_senha.get()

        # Verificar se o email já está cadastrado
        if Usuario.select().where(Usuario.email == email).exists():
            messagebox.showwarning("Cadastro", "Email já cadastrado")
            return

        # Verificar se o campo de email está vazio
        if not email.strip():
            messagebox.showerror("Erro", "Email não pode estar em branco")
            return
        if not senha.strip():
            messagebox.showerror("Erro", "Senha não pode estar em branco")
            return
        if not nome.strip():
            messagebox.showerror("Erro", "Nome não pode estar em branco")
            return
        
        # Criar novo usuário e salvar no banco de dados
        usuario = Usuario(nome=nome, email=email, senha=senha)
        usuario.save()
        
        # Exibir mensagem de sucesso
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
        print(f"Usuário cadastrado: {usuario.email}, {usuario.senha}, {usuario.nome}")

        # Limpar campos após o cadastro
        campo_nome.delete(0, END)
        campo_email.delete(0, END)
        campo_senha.delete(0, END)
        
        # Fechar janela de cadastro e retornar para a tela de login
        janela_cadastro.destroy()
        tela.deiconify()  # Voltar para a tela de login
        
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")

def cadastro():
    tela.withdraw()  # Oculta a janela principal de login
    tela2 = Toplevel()
    tela2.geometry("310x330")
    tela2.title("CADASTRO")
    texto2 = Label(tela2, text="CADASTRO", anchor=NW, font="bold 35", pady=10)
    texto2.place(x=5, y=5)

    tela2.resizable(width=FALSE, height=FALSE)
    # Dividindo a tela
    frame_cima2 = Frame(tela2, width=350, height=5, bg=co2, relief="flat")
    frame_cima2.place(x=5, y=65)
    #nome
    nome = Label(tela2, anchor=NE, text="Nome ", font="16")
    nome.place(x=5, y=100)
    obg5 = Label(tela2, anchor=NE, text="*", bg="red", font="16")
    obg5.place(x=50, y=100)
    campo_nome = Entry(tela2, width="40", relief="solid")
    campo_nome.place(x=5, y=130)
    # Email
    email2 = Label(tela2, anchor=NE, text="Email ", font="16")
    email2.place(x=5, y=155)
    obg3 = Label(tela2, anchor=NE, text="*", bg="red", font="16")
    obg3.place(x=50, y=155)
    campo_email = Entry(tela2, width="40", relief="solid")
    campo_email.place(x=5, y=185)
    # Senha
    Senha2 = Label(tela2, anchor=NE, text="Senha ", font="16")
    Senha2.place(x=5, y=210)
    obg4 = Label(tela2, anchor=NE, text="*", bg="red", font="16")
    obg4.place(x=55, y=210)
    campo_senha = Entry(tela2, width="40", relief="solid")
    campo_senha.place(x=5, y=230)
    # Botão de cadastro
    botao_ca = Button(tela2, text="Cadastrar", bg=co2, width="15", command=lambda: cadastrar_usuario(tela2, campo_email, campo_senha,campo_nome))
    botao_ca.place(x=5, y=280)
    # Botão para ir para a tela de login
    botao_login = Button(tela2, text="Tem Login?", bg=co1, bd=0, activeforeground=co1, width="15", command=lambda: voltar(tela2))
    botao_login.place(x=130, y=280)

def voltar(janela):
    janela.destroy()
    tela.deiconify()

def realizar_login():
    email = campo1.get()
    senha = campo2.get()

    try:
        usuario = Usuario.get(Usuario.email == email, Usuario.senha == senha)
        messagebox.showinfo("Login", f"Bem-vindo, {usuario.nome}!")
        # Aqui você pode adicionar a lógica para o que acontece após o login
        
    except Usuario.DoesNotExist:
        messagebox.showerror("Erro", "Credenciais inválidas. Verifique seu email e senha.")

# Janela principal de login
tela = Tk()
tela.geometry("310x330")
tela.title("LOGIN")
texto1 = Label(tela, text="LOGIN", anchor=NW, font="bold 35", pady=10)
texto1.place(x=5, y=5)

tela.resizable(width=FALSE, height=FALSE)
# Dividindo a tela
frame_cima = Frame(tela, width=350, height=5, bg=co2, relief="flat")
frame_cima.place(x=5, y=65)

# Email
email = Label(tela, anchor=NE, text="Email ", font="16")
email.place(x=5, y=100)
obg = Label(tela, anchor=NE, text="*", bg="red", font="16")
obg.place(x=50, y=100)
campo1 = Entry(tela, width="40", relief="solid")
campo1.place(x=5, y=130)
# Senha
Senha = Label(tela, anchor=NE, text="Senha ", font="16")
Senha.place(x=5, y=160)
obg2 = Label(tela, anchor=NE, text="*", bg="red", font="16")
obg2.place(x=55, y=160)
campo2 = Entry(tela, width="40", relief="solid")
campo2.place(x=5, y=190)

# Botão de login
botao = Button(tela, text="ENTRAR", bg=co2, width="15", command=realizar_login)
botao.place(x=5, y=230)

# Botão para ir para a tela de cadastro
botao_cadastro = Button(tela, text="Não tem login?", bg=co1, bd=0, activeforeground=co1, width="15", command=cadastro)
botao_cadastro.place(x=130, y=230)

# Conectando ao banco de dados
conectar_banco()

tela.mainloop()
