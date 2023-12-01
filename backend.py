import sqlite3
from tkinter import *
from datetime import datetime
from tkinter import messagebox
from frontend import *

class BackEnd():
#Backend Login - cadastrar
    def conecta_db(self):
        self.conn = sqlite3.connect("Sistema_cadastros.db")
        self.cursor = self.conn.cursor()
        print("Banco de dados conectado")
    def desconecta_db(self):
        self.conn.close()
        print("Banco de dados desconectado")
    def cria_tabela(self):
        self.conecta_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USERNAME TEXT NOT NULL,
                EMAIL TEXT NOT NULL,
                SENHA TEXT NOT NULL,
                Confirma_senha TEXT NOT NULL
            );
        """)
        self.conn.commit()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Produtos(
                COD INTEGER PRIMARY KEY,
                DESCRICAO TEXT NOT NULL,
                UNCOMERCIAL TEXT NOT NULL,
                VALORUNIT TEXT NOT NULL
            );
        """)
        self.conn.commit()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Producao(
            CODIGO INTEGER PRIMARY KEY,
            DATA_INICIO TEXT NOT NULL,
            PRODUTO_PROD TEXT NOT NULL,
            DESCRICAO TEXT NOT NULL,
            STATUS TEXT NOT NULL
        );
    """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Fornecedores(
            CNPJ PRIMARY KEY NOT NULL,
            Razao_Social TEXT NOT NULL,
            Endereco TEXT NOT NULL,
            Telefone TEXT NOT NULL,
            CEP TEXT NOT NULL,
            Produtos_Fornecidos TEXT NOT NULL,
            Cidade TEXT NOT NULL,
            UF TEXT NOT NULL
        );
    """)
        self.conn.commit()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estoque(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CODIGO_PRODUTO INTEGER NOT NULL,
            DESCRICAO TEXT NOT NULL,
            QUANTIDADE INTEGER NOT NULL,
            VALOR_TOTAL REAL NOT NULL,
            DATA_HORA TEXT NOT NULL,
            FOREIGN KEY(CODIGO_PRODUTO) REFERENCES Produtos(COD)
        );
    """)
        self.conn.commit()
        print("Tabelas criadas com sucesso")
    def cadastrar_usuario(self):
        self.username_cadastro = self.username_cadastro_entry.get()
        self.email_cadastro = self.email_cadastro_entry.get()
        self.senha_cadastro = self.senha_cadastro_entry.get()
        self.confirma_senha = self.confirma_senha_entry.get()

        self.conecta_db()
        
        self.cursor.execute("""
            INSERT INTO Usuarios(USERNAME, EMAIL, SENHA, Confirma_senha)
            Values(?,?,?,?)""", (self.username_cadastro, self.email_cadastro,self.senha_cadastro,self.confirma_senha))
        try:
            if(self.username_cadastro=="" or self.email_cadastro=="" or self.senha_cadastro=="" or self.confirma_senha==""):
                messagebox.showerror(title="Sistema de login", message="ERRO!\nPreencha todos os campos!")
            elif(len(self.username_cadastro) < 4):
                messagebox.showerror(title="Sistema de login", message="O nome de usuário precisa ter mais de quatro caracteres.")
            elif(len(self.senha_cadastro) < 6):
                messagebox.showerror(title="Sistema de login", message="A senha precisa ter pelo menos 6 caracteres.")
            elif(self.senha_cadastro != self.confirma_senha):
                messagebox.showerror(title="Sistema de login", message="As senhas não são iguais.")
            else:
                self.conn.commit()
                messagebox.showinfo(title="Sistema de login", message=f"Parabéns {self.username_cadastro}\nDados cadastrados com sucesso!")
                self.desconecta_db()
                self.limpa_entry_cadastro()
        except Exception as e:
            print(e)
            messagebox.showerror(title="Sistema", message="Erro no processamento do cadastro!\nTente novamente")
            self.desconecta_db()
    def verifica_login(self):
        self.username_login = self.username_login_entry.get()
        self.senha_login = self.senha_login_entry.get()
        
        self.conecta_db()

        self.cursor.execute("""SELECT * FROM Usuarios
        WHERE (USERNAME = ? AND SENHA = ?)""", (self.username_login, self.senha_login))
        #PERCORRER A TABELA
        self.verifica_dados = self.cursor.fetchone()

        try:
            if(self.username_login == "" or self.senha_login == ""):
                messagebox.showwarning(title="E-STOQUE", message="Preencha todos os campos solicitados!")
            elif(self.username_login in self.verifica_dados and self.senha_login in self.verifica_dados):
                self.config_janelaMENU()
                self.atualiza_hora()
                self.desconecta_db()
                self.limpa_entry_login()
        except Exception as e:
            print(e)
            messagebox.showerror(title="Sistema de login", message="ERRO!\nDados não encontrados no sistema.\nVerifique os dados ou realize o cadastro.")
            self.desconecta_db()

#Backend GERENCIAR PRODUTOS 
    def adicionarproduto(self, JanelaADD):
        self.cod_produto = JanelaADD.codigo_entry.get()
        self.descricao_produto = JanelaADD.descricao_entry.get()
        self.uncomercial_produto = JanelaADD.un_comercial_entry.get()
        self.valorunitario_produto = JanelaADD.valor_unitario_entry.get()

        if(self.cod_produto=="" or self.descricao_produto=="" or self.uncomercial_produto=="" or self.valorunitario_produto==""):
            messagebox.showerror(title="E-STOQUE", message="ERRO!\nPreencha todos os campos corretamente!")
        else:
            self.conecta_db()
            self.cursor.execute("SELECT * FROM Produtos WHERE COD=?", (self.cod_produto,))
            verificarcod = self.cursor.fetchone()
            if verificarcod is not None:
                messagebox.showerror(title="E-STOQUE", message="ERRO!\nO código do produto já existe!")
                self.desconecta_db()
            else:
                try:
                    self.cursor.execute("""
                        INSERT INTO Produtos(COD, DESCRICAO, UNCOMERCIAL, VALORUNIT)
                        Values(?,?,?,?)""", (self.cod_produto, self.descricao_produto,self.uncomercial_produto,self.valorunitario_produto))
                    self.conn.commit()
                    messagebox.showinfo(title="E-STOQUE", message="Dados cadastrados com sucesso!")
                    JanelaADD.destroy()
                except Exception as e:
                    print(e)
                    messagebox.showerror(title="E-STOQUE", message="Erro no processamento dos dados!\nTente novamente")
                finally:
                    self.desconecta_db()

    def editarproduto(self, JanelaEDIT):
        self.cod_produto = JanelaEDIT.codigo_entry.get()
        self.descricao_produto = JanelaEDIT.descricao_entry.get()
        self.uncomercial_produto = JanelaEDIT.un_comercial_entry.get()
        self.valorunitario_produto = JanelaEDIT.valor_unitario_entry.get()

        if(self.cod_produto=="" or self.descricao_produto=="" or self.uncomercial_produto=="" or self.valorunitario_produto==""):
            messagebox.showerror(title="E-STOQUE", message="ERRO!\nPreencha todos os campos corretamente!")
        else:
            self.conecta_db()
            self.cursor.execute("SELECT * FROM Produtos WHERE COD=?", (self.cod_produto,))
            verificacod = self.cursor.fetchone()
            if verificacod is None:
                messagebox.showerror(title="E-STOQUE", message="ERRO!\nO produto com o código fornecido não existe!\n Identifique o código em consultar inventário ou adicione o produto.")
                self.desconecta_db()
            else:
                try:
                    self.cursor.execute("""
                        UPDATE Produtos
                        SET DESCRICAO = ?, UNCOMERCIAL = ?, VALORUNIT = ?
                        WHERE COD = ?""", (self.descricao_produto, self.uncomercial_produto, self.valorunitario_produto, self.cod_produto))
                    self.conn.commit()
                    messagebox.showinfo(title="E-STOQUE", message="Dados atualizados com sucesso!")
                    JanelaEDIT.destroy()
                except Exception as e:
                    print(e)
                    messagebox.showerror(title="E-STOQUE", message="Erro no processamento dos dados!\nTente novamente")
                finally:
                    self.desconecta_db()
        
    def deletarproduto(self, JanelaDEL):
        self.cod_produto = JanelaDEL.codigo_entry.get()

        if(self.cod_produto==""):
            messagebox.showerror(title="E-STOQUE", message="ERRO!\nPreencha o campo do código do produto!")
        else:
            self.conecta_db()
            self.cursor.execute("SELECT * FROM Produtos WHERE COD=?", (self.cod_produto,))
            verificacod = self.cursor.fetchone()
            if verificacod is None:
                messagebox.showerror(title="E-STOQUE", message="ERRO!\nO produto com o código fornecido não existe!")
                self.desconecta_db()
            else:
                descricao_produto = verificacod[1]  # Supondo que a descrição do produto esteja na segunda coluna da tabela
                confirmar_delete = messagebox.askquestion ('E-STOQUE',f'Tem certeza de que deseja deletar o produto "{descricao_produto}" com código "{self.cod_produto}"?',icon = 'warning')
                if confirmar_delete == 'yes':
                    try:
                        self.cursor.execute("""
                            DELETE FROM Produtos
                            WHERE COD = ?""", (self.cod_produto,))
                        self.conn.commit()
                        messagebox.showinfo(title="E-STOQUE", message="Produto deletado com sucesso!")
                    except Exception as e:
                        print(e)
                        messagebox.showerror(title="E-STOQUE", message="Erro no processamento dos dados!\nTente novamente")
                    finally:
                        self.desconecta_db()

    def consultar_produtos(self):
        self.conecta_db()
        self.cursor.execute("SELECT * FROM Produtos")
        todos_produtos = self.cursor.fetchall()
        self.desconecta_db()
        return todos_produtos
#Backend GERENCIAR ESTOQUE
    def adicionarestoque(self, codigo_produto, descricao_produto, quantidade):
        self.conecta_db()
        self.cursor.execute("SELECT * FROM Produtos WHERE COD=?", (codigo_produto,))
        produto = self.cursor.fetchone()
        if produto is None:
            self.desconecta_db()
            return "ERRO!\nO produto não existe!"
        else:
            try:
                valor_unitario = produto[3].replace(',', '.')
                valor_total = int(quantidade) * float(valor_unitario)
                self.cursor.execute("""
                    INSERT INTO Estoque(CODIGO_PRODUTO, DESCRICAO, QUANTIDADE, VALOR_TOTAL, DATA_HORA)
                    Values(?,?,?,?,?)
                """, (codigo_produto, descricao_produto, quantidade, valor_total, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                self.conn.commit()
                return "Estoque adicionado com sucesso!"
            except Exception as e:
                print(e)
                return "Erro no processamento dos dados!\nTente novamente"
            finally:
                self.desconecta_db()

    def atualizarestoque(self, JanelaUPD):
        codigo_produto = JanelaUPD.codigo_produto_entry.get()
        nova_quantidade = JanelaUPD.quantidade_entry.get()

        if codigo_produto == "" or nova_quantidade == "":
            messagebox.showerror(title="E-STOQUE", message="ERRO!\nPreencha todos os campos corretamente!")
        else:
            self.conecta_db()
            self.cursor.execute("SELECT * FROM Produtos WHERE COD=?", (codigo_produto,))
            produto = self.cursor.fetchone()
            if produto is None:
                messagebox.showerror(title="E-STOQUE", message="ERRO!\nO produto não existe!")
                self.desconecta_db()
            else:
                try:
                    valor_unitario = produto[3].replace(',', '.')
                    valor_total = int(nova_quantidade) * float(valor_unitario)  # Multiplica a nova quantidade pelo valor unitário do produto
                    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Obtém a data e a hora atual

                    self.cursor.execute("""
                        UPDATE Estoque
                        SET QUANTIDADE = ?, VALOR_TOTAL = ?, DATA_HORA = ?
                        WHERE CODIGO_PRODUTO = ?
                    """, (nova_quantidade, valor_total, data_hora, codigo_produto))
                    self.conn.commit()
                    messagebox.showinfo(title="E-STOQUE", message="Estoque atualizado com sucesso!")
                    JanelaUPD.destroy()
                except Exception as e:
                    print(e)
                    messagebox.showerror(title="E-STOQUE", message="Erro no processamento dos dados!\nTente novamente")
                finally:
                    self.desconecta_db()

    def consultar_estoque(self):
        self.conecta_db()
        self.cursor.execute("SELECT CODIGO_PRODUTO, DESCRICAO,QUANTIDADE, VALOR_TOTAL, DATA_HORA FROM Estoque")
        todos_estoques = self.cursor.fetchall()
        self.desconecta_db()
        return todos_estoques
#Backend GERENCIAR PRODUÇÃO
    def registrarproducao(self, Janela_RegistrarProd):
        self.codigo = Janela_RegistrarProd.codigo_entry.get()
        self.data_inicio = Janela_RegistrarProd.data_inicio.get()
        self.produto_produzido = Janela_RegistrarProd.produto_produzido.get()
        self.descricao = Janela_RegistrarProd.descricao_prod.get("1.0", 'end-1c')
        self.status = Janela_RegistrarProd.status_combobox.get()

        if(self.codigo=="" or self.data_inicio=="" or self.produto_produzido=="" or self.descricao=="" or self.status==""):
            messagebox.showerror(title="E-STOQUE", message="ERRO!\nPreencha todos os campos corretamente!")
        else:
            self.conecta_db()
            self.cursor.execute("SELECT * FROM Producao WHERE CODIGO=?", (self.codigo,))
            verificar_codigo = self.cursor.fetchone()
            if verificar_codigo is not None:
                messagebox.showerror(title="E-STOQUE", message="ERRO!\nO código de registro da produção já existe!")
                self.desconecta_db()
            else:
                try:
                    self.cursor.execute("""
                        INSERT INTO Producao(CODIGO, DATA_INICIO, PRODUTO_PROD, DESCRICAO, STATUS)
                        Values(?,?,?,?,?)""", (self.codigo, self.data_inicio, self.produto_produzido, self.descricao, self.status))
                    self.conn.commit()
                    messagebox.showinfo(title="E-STOQUE", message="Dados de produção cadastrados com sucesso!")
                    Janela_RegistrarProd.destroy()
                except Exception as e:
                    print(e)
                    messagebox.showerror(title="E-STOQUE", message="Erro no processamento dos dados!\nTente novamente")
                finally:
                    self.desconecta_db()

    def atualizarproducao(self, Janela_AtualizarProd):
        self.codigo = Janela_AtualizarProd.codigo_entry.get()
        self.status = Janela_AtualizarProd.status_combobox.get()
        self.nova_descricao = Janela_AtualizarProd.descricao_entry.get()

        if(self.codigo=="" or self.status=="" or self.nova_descricao==""):
            messagebox.showerror(title="E-STOQUE", message="ERRO!\nPreencha todos os campos corretamente!")
        else:
            self.conecta_db()
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM Producao WHERE CODIGO=?", (self.codigo,))
            verificar_codigo = self.cursor.fetchone()
            if verificar_codigo is None:
                messagebox.showerror(title="E-STOQUE", message="ERRO!\nO código de registro da produção não existe!")
                self.desconecta_db()
            else:
                try:
                    descricao_atual = verificar_codigo['DESCRICAO']
                    descricao_atualizada = descricao_atual + "\n" + self.nova_descricao
                    self.cursor.execute("""
                        UPDATE Producao
                        SET STATUS = ?, DESCRICAO = ?
                        WHERE CODIGO = ?""", (self.status, descricao_atualizada, self.codigo))
                    self.conn.commit()
                    messagebox.showinfo(title="E-STOQUE", message="Status e descrição da produção atualizados com sucesso!")
                    Janela_AtualizarProd.destroy()
                except Exception as e:
                    print(e)
                    messagebox.showerror(title="E-STOQUE", message="Erro no processamento dos dados!\nTente novamente")
                finally:
                    self.desconecta_db()

    def consultar_producao(self):
        self.conecta_db()
        self.cursor.execute("SELECT * FROM Producao")
        todas_producoes = self.cursor.fetchall()
        self.desconecta_db()
        return todas_producoes
#Backend GERENCIAR FORNECEDORES
    def adicionarfornecedor(self, Janela_addfornecedor):
        self.razao_social = Janela_addfornecedor.razao_social_entry.get()
        self.cnpj = Janela_addfornecedor.cnpj_entry.get()
        self.endereco = Janela_addfornecedor.endereco_entry.get()
        self.telefone = Janela_addfornecedor.telefone_entry.get()
        self.cep = Janela_addfornecedor.cep_entry.get()
        self.produtos_fornecidos = Janela_addfornecedor.produtos_fornecidos_entry.get()
        self.cidade = Janela_addfornecedor.cidade_entry.get()
        self.uf = Janela_addfornecedor.uf_entry.get()

        if(self.razao_social=="" or self.cnpj=="" or self.endereco=="" or self.telefone=="" or self.cep=="" or self.produtos_fornecidos=="" or self.cidade=="" or self.uf==""):
            messagebox.showerror(title="E-STOQUE", message="ERRO!\nPreencha todos os campos corretamente!")
        else:
            self.conecta_db()
            self.cursor.execute("SELECT * FROM Fornecedores WHERE CNPJ=?", (self.cnpj,))
            verificar_cnpj = self.cursor.fetchone()
            if verificar_cnpj is not None:
                messagebox.showerror(title="E-STOQUE", message="ERRO!\nO CNPJ do fornecedor já existe!")
                self.desconecta_db()
            else:
                try:
                    self.cursor.execute("""
                        INSERT INTO Fornecedores(Razao_Social, CNPJ, Endereco, Telefone, CEP, Produtos_Fornecidos, Cidade, UF)
                        Values(?,?,?,?,?,?,?,?)""", (self.razao_social, self.cnpj, self.endereco, self.telefone, self.cep, self.produtos_fornecidos, self.cidade, self.uf))
                    self.conn.commit()
                    messagebox.showinfo(title="E-STOQUE", message="Dados do fornecedor cadastrados com sucesso!")
                    Janela_addfornecedor.destroy()
                except Exception as e:
                    print(e)
                    messagebox.showerror(title="E-STOQUE", message="Erro no processamento dos dados!\nTente novamente")
                finally:
                    self.desconecta_db()

    def atualizarfornecedor(self, Janela_attfornecedor):
        self.razao_social = Janela_attfornecedor.razao_social_entry.get()
        self.cnpj = Janela_attfornecedor.cnpj_entry.get()
        self.endereco = Janela_attfornecedor.endereco_entry.get()
        self.telefone = Janela_attfornecedor.telefone_entry.get()
        self.cep = Janela_attfornecedor.cep_entry.get()
        self.produtos_fornecidos = Janela_attfornecedor.produtos_fornecidos_entry.get()
        self.cidade = Janela_attfornecedor.cidade_entry.get()
        self.uf = Janela_attfornecedor.uf_entry.get()

        if(self.razao_social=="" or self.cnpj=="" or self.endereco=="" or self.telefone=="" or self.cep=="" or self.produtos_fornecidos=="" or self.cidade=="" or self.uf==""):
            messagebox.showerror(title="E-STOQUE", message="ERRO!\nPreencha todos os campos corretamente!")
        else:
            self.conecta_db()
            self.cursor.execute("SELECT * FROM Fornecedores WHERE CNPJ=?", (self.cnpj,))
            verificar_cnpj = self.cursor.fetchone()
            if verificar_cnpj is None:
                messagebox.showerror(title="E-STOQUE", message="ERRO!\nO fornecedor com o CNPJ fornecido não existe!")
                self.desconecta_db()
            else:
                try:
                    self.cursor.execute("""
                        UPDATE Fornecedores
                        SET Razao_Social = ?, Endereco = ?, Telefone = ?, CEP = ?, Produtos_Fornecidos = ?, Cidade = ?, UF = ?
                        WHERE CNPJ = ?""", (self.razao_social, self.endereco, self.telefone, self.cep, self.produtos_fornecidos, self.cidade, self.uf, self.cnpj))
                    self.conn.commit()
                    messagebox.showinfo(title="E-STOQUE", message="Dados do fornecedor atualizados com sucesso!")
                    Janela_attfornecedor.destroy()
                except Exception as e:
                    print(e)
                    messagebox.showerror(title="E-STOQUE", message="Erro no processamento dos dados!\nTente novamente")
                finally:
                    self.desconecta_db()
        
    def deletarfornecedor(self, Janela_ApagarFornecedor):
        self.cnpj = Janela_ApagarFornecedor.cnpj_entry.get()

        if(self.cnpj==""):
            messagebox.showerror(title="E-STOQUE", message="ERRO!\nPreencha o campo do CNPJ do fornecedor!")
        else:
            self.conecta_db()
            self.cursor.execute("SELECT * FROM Fornecedores WHERE CNPJ=?", (self.cnpj,))
            verificar_cnpj = self.cursor.fetchone()
            if verificar_cnpj is None:
                messagebox.showerror(title="E-STOQUE", message="ERRO!\nO fornecedor com o CNPJ fornecido não existe!")
                self.desconecta_db()
            else:
                razao_social = verificar_cnpj[1]  # Supondo que a razão social esteja na segunda coluna da tabela
                confirmar_delete = messagebox.askquestion ('E-STOQUE',f'Tem certeza de que deseja deletar o fornecedor "{razao_social}" com CNPJ "{self.cnpj}"?',icon = 'warning')
                if confirmar_delete == 'yes':
                    try:
                        self.cursor.execute("""
                            DELETE FROM Fornecedores
                            WHERE CNPJ = ?""", (self.cnpj,))
                        self.conn.commit()
                        messagebox.showinfo(title="E-STOQUE", message="Fornecedor deletado com sucesso!")
                    except Exception as e:
                        print(e)
                        messagebox.showerror(title="E-STOQUE", message="Erro no processamento dos dados!\nTente novamente")
                    finally:
                        self.desconecta_db()

    def consultar_fornecedores(self):
        self.conecta_db()
        self.cursor.execute("SELECT * FROM Fornecedores")
        todos_fornecedores = self.cursor.fetchall()
        self.desconecta_db()
        return todos_fornecedores
