import sqlite3
import os

Diretorio_principal = os.path.dirname(__file__)
Diretorio_Log = os.path.join(Diretorio_principal, "LOG")
class Funcs():
    def limpar_clientes(self):
        pass
    def conectar_db(self):
        #conectar ou cria o banco de dados
        self.conn = sqlite3.connect(os.path.join(Diretorio_Log,'LoginDataBase.db'))
        self.cursor = self.conn.cursor()
    def _tabela_existe(self, table_name):
        """Verifica se uma tabela existe consultando sqlite_master."""
        self.conectar_db()
        
        #consulta a tabela mestra do SQLite
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        
        #se fetchone() retornar algo, a tabela existe
        existe = self.cursor.fetchone() is not None
        
        self.desconectar_db()
        return existe
    def desconectar_db(self):
        self.conn.close()
    def criar_tables(self):
        
        #se a tabela já existe, não executa o restante do código
        if self._tabela_existe('clientes'):
            print("Tabela 'clientes' já existe. Conexão e criação ignoradas.")
            return # Sai do método
            
        #o código abaixo só será executado se a tabela 'clientes' *não* existir.
        self.conectar_db(); print("Conectando ao Banco de Dados.....")
        
        #removi o "IF NOT EXISTS" do SQL, pois já fazemos a checagem em Python.
        self.cursor.execute("""
            CREATE TABLE clientes (
                cod INTEGER PRIMARY KEY, 
                nome_cliente CHAR(40) NOT NULL,
                email_cliente CHAR(100) NOT NULL,
                senha_cliente CHAR(20) NOT NULL
            );
        """)
        
        self.conn.commit(); print("Banco De Dados Criado!!")

        self.desconectar_db()
