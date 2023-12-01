import customtkinter as ctk
from tkinter import *
from datetime import datetime
from tkinter import messagebox
from tkinter import ttk
from backend import *
from backend import BackEnd

#Config da janela inicial
class FrontEnd():
#Config tela inicial
    def config_janela(self):
        self.geometry("700x400")
        self.title("E-STOQUE")
        self.resizable(False,False)
        self.iconbitmap('imagens/img3.ico')
#Config tela login
    def tela_login(self):
        #Inserindo imagens
        self.img = PhotoImage(file="imagens/img1.png")
        self.img = self.img.subsample(6,6)
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=1, column=0, padx=10)
        #Titulo
        self.title_label = ctk.CTkLabel(self, text="Bem vindo ao E-STOQUE!", font=("Century Gothic bold", 18))
        self.title_label.grid(row=0, column=0, pady=10, padx=10)
        #frame de login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350,y=10)
        #componentes do frame
        self.lb_tittle = ctk.CTkLabel(self.frame_login, text="Faça seu login", font=("Century Gothic bold", 22))
        self.lb_tittle.grid(row=0, column=0, padx=10, pady=10)

        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Seu nome de usuário", font=("Century Gothic bold", 16), corner_radius=15)
        self.username_login_entry.grid(row=1,column=0,pady=10,padx=10)

        self.senha_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Senha", font=("Century Gothic bold", 16), corner_radius=15, show="*")
        self.senha_login_entry.grid(row=2,column=0,pady=10,padx=10)

        self.but_login_login = ctk.CTkButton(self.frame_login, width=300, text="Fazer Login", font=("Century Gothic bold", 16), corner_radius=15, command=self.verifica_login)
        self.but_login_login.grid(row=4,column=0,pady=10,padx=10)
        #Butão cadastro
        self.span = ctk.CTkLabel(self.frame_login, text="Não possui conta?", font=("Century Gothic", 14))
        self.span.grid(row=5, column=0, pady=10, padx=10)

        self.but_cadastro = ctk.CTkButton(self.frame_login, width=300, text="Fazer Cadastro", font=("Century Gothic bold", 16), corner_radius=15, fg_color="green",hover_color="#050", command=self.tela_de_cadastro)
        self.but_cadastro.grid(row=6,column=0,pady=10,padx=10)  
#Config tela de cadastro 
    def tela_de_cadastro(self):
        #REMOVENDO LOGIN
        self.frame_login.place_forget()
        #frame cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350,y=10)
        #titulo
        self.lb_tittle = ctk.CTkLabel(self.frame_cadastro, text="Faça seu Cadastro", font=("Century Gothic bold", 22))
        self.lb_tittle.grid(row=0, column=0, padx=10, pady=10)
        #componentes cadastro
        self.username_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Seu nome de usuário", font=("Century Gothic bold", 16), corner_radius=15)
        self.username_cadastro_entry.grid(row=1,column=0,pady=5,padx=10)

        self.email_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Email de usuário", font=("Century Gothic bold", 16), corner_radius=15)
        self.email_cadastro_entry.grid(row=2,column=0,pady=5,padx=10)

        self.senha_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Senha", font=("Century Gothic bold", 16), corner_radius=15, show="*")
        self.senha_cadastro_entry.grid(row=3,column=0,pady=5,padx=10)

        self.confirma_senha_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Confirmar a senha", font=("Century Gothic bold", 16), corner_radius=15, show="*")
        self.confirma_senha_entry.grid(row=4,column=0,pady=5,padx=10)
        #BUTTONS
        self.but_cadastrar = ctk.CTkButton(self.frame_cadastro, width=300, text="Realizar Cadastro", font=("Century Gothic bold", 14), corner_radius=15, fg_color="green", hover_color="#050", command=self.cadastrar_usuario)
        self.but_cadastrar.grid(row=6,column=0,pady=10,padx=10)

        self.but_voltar = ctk.CTkButton(self.frame_cadastro, width=300, text="Volta ao login", font=("Century Gothic bold", 14), corner_radius=15, fg_color="#444",hover_color="#333", command=self.tela_login)
        self.but_voltar.grid(row=7,column=0,pady=10,padx=10)
#Limpeza de entradas   
    def limpa_entry_cadastro(self):
        self.username_cadastro_entry.delete(0, END)
        self.email_cadastro_entry.delete(0, END)
        self.senha_cadastro_entry.delete(0, END)
        self.confirma_senha_entry.delete(0, END) 
    
    def limpa_entry_login(self):
        self.username_login_entry.delete(0, END)
        self.senha_login_entry.delete(0,END)
#Config da janela inicial de menu
    def config_janelaMENU(self):
        #Dimensão
        self.geometry("700x400")
        
        self.resizable(False,False)
        #Inserindo imagens
        self.img = PhotoImage(file="imagens/img1.png")
        self.img = self.img.subsample(6,6)
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=1, column=0, padx=10)
        #Titulo
        self.title_label = ctk.CTkLabel(self, text="Bem vindo ao E-STOQUE!", font=("Century Gothic bold", 18))
        self.title_label.grid(row=0, column=0, pady=10, padx=10)
        #FRAME DE OPÇÕES DO MENU
        self.frame_MENU = ctk.CTkFrame(self, width=350, height=380)
        self.frame_MENU.place(x=350,y=10)

        self.lb_tittle = ctk.CTkLabel(self.frame_MENU, text="Selecione a opção que desejar.", font=("Century Gothic bold", 20))
        self.lb_tittle.grid(row=0, column=0, padx=10, pady=15)
        #BUTTONS
        self.but_gerenciarProdutos = ctk.CTkButton(self.frame_MENU, width=300, text="Gerenciar Produtos", font=("Century Gothic bold", 14), corner_radius=15,  command=self.gerenciar_produto)
        self.but_gerenciarProdutos.grid(row=1,column=0,pady=15,padx=10) 

        self.but_gerenciarEstoque = ctk.CTkButton(self.frame_MENU, width=300, text="Gerenciar Estoque", font=("Century Gothic bold", 14), corner_radius=15,  command=self.gerenciar_estoque)
        self.but_gerenciarEstoque.grid(row=2,column=0,pady=15,padx=10) 

        self.but_gerenciarProdução = ctk.CTkButton(self.frame_MENU, width=300, text="Gerenciar Produção", font=("Century Gothic bold", 14), corner_radius=15, command=self.gerenciar_producao)
        self.but_gerenciarProdução.grid(row=3,column=0,pady=15,padx=10) 

        self.but_gerenciarFornecedores = ctk.CTkButton(self.frame_MENU, width=300, text="Gerenciar Fornecedores", font=("Century Gothic bold", 14), corner_radius=15, command=self.gerenciar_fornecedores)
        self.but_gerenciarFornecedores.grid(row=4,column=0,pady=15,padx=10) 

        self.but_sair = ctk.CTkButton(self.frame_MENU, width=300, text="Sair do sistema", font=("Century Gothic bold", 14), corner_radius=15, fg_color="#444",hover_color="#333", command=self.sair_do_sistema)
        self.but_sair.grid(row=5,column=0,pady=15,padx=10)

        self.data_hora_label = ctk.CTkLabel(self.frame_MENU, font=("Century Gothic", 14))
        self.data_hora_label.grid(row=6, column=0, pady=10, padx=10)
#Data e hora Menu Inicial
    def atualiza_hora(self):
        agora = datetime.now()
        data_hora = agora.strftime("%d/%m/%Y, %H:%M:%S")
        self.data_hora_label.configure(text="Data e hora atual: " + data_hora)
        self.after(1000, self.atualiza_hora)  # Atualiza a hora a cada 1000 milissegundos (ou seja, 1 segundo)
#Config dos botões do menu
    def gerenciar_produto(self):
        self.withdraw()
        backend = BackEnd()
        self.gerenciar_produto = GerenciarProduto(self, self, backend)
    
    def gerenciar_estoque(self):
        self.withdraw()
        backend = BackEnd()
        self.gerenciar_estoque = GerenciarEstoque(self, self, backend)

    def gerenciar_producao(self):
        self.withdraw()
        backend = BackEnd()
        self.gerenciar_producao = GerenciarProducao(self, self, backend)
        
    def gerenciar_fornecedores(self):
        self.withdraw()
        backend = BackEnd()
        self.gerenciar_fornecedores = GerenciarFornecedor(self, self, backend)
    #Botão voltar ao menu
    def voltar_ao_menu(self):
        self.deiconify()
    #Botão sair do sistema
    def sair_do_sistema(self):
        self.destroy()

class GerenciarProduto():
    def __init__(self, novaJanela, frontend, backend):
        self.frontend = frontend
        self.backend = backend
        novaJanela = ctk.CTkToplevel()
        novaJanela.title("E-STOQUE")
        novaJanela.geometry("856x645")
        novaJanela.iconbitmap('imagens/img3.ico')
        novaJanela.deiconify()
        novaJanela.frame_PRODUTO = ctk.CTkFrame(master=novaJanela, width=176, height=650, corner_radius=0)
        novaJanela.frame_PRODUTO.pack_propagate(0)
        novaJanela.frame_PRODUTO.pack (fill="y", anchor="w", side="left")
        novaJanela.img = PhotoImage(file="imagens/img3.png")
        novaJanela.lb_img = ctk.CTkLabel(novaJanela.frame_PRODUTO, text=None, image=novaJanela.img).pack(anchor="center", ipady=5, pady=(50, 0))
        #BUTTONS FRAME ESQUERDA
        novaJanela.botão_cadastrar = ctk.CTkButton(master=novaJanela.frame_PRODUTO, text="Adicionar Produto", font=("Century Gothic bold", 14), fg_color="green",hover_color="#050", anchor="w", command=self.adicionar_produto).pack(anchor="center", ipady=5, pady=(60, 0))
        novaJanela.botão_editar = ctk.CTkButton(master=novaJanela.frame_PRODUTO, text="Editar Produto", font=("Century Gothic bold", 14),  fg_color="green",hover_color="#050",anchor="w",command=self.editar_produto).pack(anchor="center", ipady=5, pady=(16, 0))
        novaJanela.botão_deletar = ctk.CTkButton(master=novaJanela.frame_PRODUTO, text="Deletar Produto", font=("Century Gothic bold", 14),  fg_color="green",hover_color="#050",anchor="w",command=self.deletar_produto).pack(anchor="center", ipady=5, pady=(16, 0))
        novaJanela.botão_inventario = ctk.CTkButton(master=novaJanela.frame_PRODUTO, text="Consultar Inventário", font=("Century Gothic bold", 14),  fg_color="green",hover_color="#050",anchor="w",command=self.consultar_inventario).pack(anchor="center", ipady=5, pady=(16, 0))
        novaJanela.botão_voltarMenu = ctk.CTkButton(master=novaJanela.frame_PRODUTO, width=150, text="Voltar ao Menu", font=("Century Gothic bold", 14), corner_radius=10, fg_color="#444",hover_color="#333", command=self.voltar_ao_menu).pack(side="bottom", pady=15)
        #FRAME DIREITA INICIAL
        novaJanela.title_frame = ctk.CTkFrame(master=novaJanela, fg_color="transparent")
        novaJanela.title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))
        ctk.CTkLabel(master=novaJanela.title_frame, text="Controle de Produtos\nSelecione a opção que deseja.", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center")
        novaJanela.img2 = PhotoImage(file="imagens/img2.png")
        novaJanela.img2 = novaJanela.img2.subsample(4,4)
        novaJanela.lb_img2 = ctk.CTkLabel(master=novaJanela.title_frame, text=None, image=novaJanela.img2).pack(anchor="center")
    
    def adicionar_produto(self):
        JanelaADD = ctk.CTkToplevel()
        JanelaADD.title("E-STOQUE")
        JanelaADD.geometry("700x400")
        JanelaADD.iconbitmap('imagens/img3.ico')
        JanelaADD.attributes('-topmost', True) 
        JanelaADD.add_frame = ctk.CTkFrame(master=JanelaADD)
        JanelaADD.add_frame.pack(anchor="n", fill='both', expand=True)
        ctk.CTkLabel(master=JanelaADD.add_frame, text="Cadastrar novo produto.", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center")
        JanelaADD.codigo_entry = ctk.CTkEntry(JanelaADD.add_frame, width=300, placeholder_text="Código do Produto", font=("Century Gothic bold", 16), corner_radius=15)
        JanelaADD.codigo_entry.pack(pady=15)  
        JanelaADD.descricao_entry = ctk.CTkEntry(JanelaADD.add_frame, width=300, placeholder_text="Descrição", font=("Century Gothic bold", 16), corner_radius=15)
        JanelaADD.descricao_entry.pack(pady=15)  
        JanelaADD.un_comercial_entry = ctk.CTkEntry(JanelaADD.add_frame, width=300, placeholder_text="Unidade Comercial", font=("Century Gothic bold", 16), corner_radius=15)
        JanelaADD.un_comercial_entry.pack(pady=15)  
        JanelaADD.valor_unitario_entry = ctk.CTkEntry(JanelaADD.add_frame, width=300, placeholder_text="Valor Unitário", font=("Century Gothic bold", 16), corner_radius=15)
        JanelaADD.valor_unitario_entry.pack(pady=15)  

        JanelaADD.botao_salvar = ctk.CTkButton(JanelaADD.add_frame, text="Salvar", font=("Century Gothic bold", 16), fg_color="green", corner_radius=15, command=lambda: self.backend.adicionarproduto(JanelaADD))
        JanelaADD.botao_salvar.pack(side="bottom", pady=30)  

    def editar_produto(self):
        JanelaEDIT = ctk.CTkToplevel()
        JanelaEDIT.title("E-STOQUE")
        JanelaEDIT.geometry("700x400")
        JanelaEDIT.iconbitmap('imagens/img3.ico')
        JanelaEDIT.attributes('-topmost', True) 
        JanelaEDIT.edit_frame = ctk.CTkFrame(master=JanelaEDIT)
        JanelaEDIT.edit_frame.pack(anchor="n", fill='both', expand=True)
        ctk.CTkLabel(master=JanelaEDIT.edit_frame, text="Editar produto existente.\nPara editar algum produto, insira o código e as novas informações.", font=("Arial Black", 16), text_color="#87ceeb").pack(anchor="center")
        JanelaEDIT.codigo_entry = ctk.CTkEntry(JanelaEDIT.edit_frame, width=300, placeholder_text="Código do Produto", font=("Century Gothic bold", 16), corner_radius=15)
        JanelaEDIT.codigo_entry.pack(pady=15)  
        JanelaEDIT.descricao_entry = ctk.CTkEntry(JanelaEDIT.edit_frame, width=300, placeholder_text="Descrição", font=("Century Gothic bold", 16), corner_radius=15)
        JanelaEDIT.descricao_entry.pack(pady=15)  
        JanelaEDIT.un_comercial_entry = ctk.CTkEntry(JanelaEDIT.edit_frame, width=300, placeholder_text="Unidade Comercial", font=("Century Gothic bold", 16), corner_radius=15)
        JanelaEDIT.un_comercial_entry.pack(pady=15)  
        JanelaEDIT.valor_unitario_entry = ctk.CTkEntry(JanelaEDIT.edit_frame, width=300, placeholder_text="Valor Unitário", font=("Century Gothic bold", 16), corner_radius=15)
        JanelaEDIT.valor_unitario_entry.pack(pady=15)  

        JanelaEDIT.botao_salvar = ctk.CTkButton(JanelaEDIT.edit_frame, text="Atualizar", font=("Century Gothic bold", 16),corner_radius=15, command=lambda: self.backend.editarproduto(JanelaEDIT))
        JanelaEDIT.botao_salvar.pack(side="bottom", pady=30)  
    
    def deletar_produto(self):
        JanelaDEL = ctk.CTkToplevel()
        JanelaDEL.title("E-STOQUE")
        JanelaDEL.geometry("700x400")
        JanelaDEL.iconbitmap('imagens/img3.ico')
        JanelaDEL.attributes('-topmost', True) 
        JanelaDEL.del_frame = ctk.CTkFrame(master=JanelaDEL)
        JanelaDEL.del_frame.pack(anchor="n", fill='both', expand=True)
        ctk.CTkLabel(master=JanelaDEL.del_frame, text="Deletar produto existente.\nInsira o código do produto que deseja excluir", font=("Arial Black", 16), text_color="#f40a13").pack(anchor="center")
        JanelaDEL.codigo_entry = ctk.CTkEntry(JanelaDEL.del_frame, width=300, placeholder_text="Código do Produto", font=("Century Gothic bold", 16), corner_radius=15)
        JanelaDEL.codigo_entry.pack(pady=15)  

        JanelaDEL.botao_deletar = ctk.CTkButton(JanelaDEL.del_frame, text="Deletar", font=("Century Gothic bold", 16), fg_color="#f40a13", corner_radius=15, command=lambda: self.backend.deletarproduto(JanelaDEL))
        JanelaDEL.botao_deletar.pack(side="bottom", pady=30)  
    
    def consultar_inventario(self):
        todos_produtos = self.backend.consultar_produtos()
        JanelaInventario = ctk.CTkToplevel()
        JanelaInventario.title("E-STOQUE")
        JanelaInventario.geometry("700x400")
        JanelaInventario.iconbitmap('imagens/img3.ico')
        JanelaInventario.attributes('-topmost', True) 
        JanelaInventario.Inventario_frame = ctk.CTkFrame(master=JanelaInventario)
        JanelaInventario.Inventario_frame.pack(anchor="n", fill='both', expand=True)
        ctk.CTkLabel(master=JanelaInventario.Inventario_frame, text="Listagem de Produtos Cadastrados.", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center")

        # Cria a tabela
        style = ttk.Style()
        style.configure("Treeview", background="silver", foreground="black", fieldbackground="silver")
        style.configure("Treeview.Heading", background="gray", foreground="black")

        # Cria um frame para conter a tabela e a barra de rolagem
        frame_tabela = ttk.Frame(JanelaInventario.Inventario_frame)
        frame_tabela.pack(fill='both', expand=True)

        # Cria a barra de rolagem
        scrollbar = Scrollbar(frame_tabela)
        scrollbar.pack(side='right', fill='y')

        tabela = ttk.Treeview(frame_tabela, columns=("COD", "DESCRICAO", "UNCOMERCIAL", "VALORUNIT"), show='headings', yscrollcommand=scrollbar.set)
        tabela.column("COD", width=100)
        tabela.column("DESCRICAO", width=200)
        tabela.column("UNCOMERCIAL", width=200)
        tabela.column("VALORUNIT", width=100)
        tabela.heading("COD", text="Código")
        tabela.heading("DESCRICAO", text="Descrição")
        tabela.heading("UNCOMERCIAL", text="Unidade Comercial")
        tabela.heading("VALORUNIT", text="Valor Unitário")
        tabela.pack(side='left', fill='both', expand=True)

        # Conecta a barra de rolagem à tabela
        scrollbar.config(command=tabela.yview)

        if todos_produtos:
            for produto in todos_produtos:
                tabela.insert('', 'end', values=produto)
        else:
            print("Nenhum produto encontrado no inventário.")
    
    def voltar_ao_menu(self):
        self.frontend.voltar_ao_menu()

class GerenciarEstoque():
    def __init__(self, novaJanela, frontend, backend):
        self.frontend = frontend
        self.backend = backend
        novaJanela = ctk.CTkToplevel()
        novaJanela.title("E-STOQUE")
        novaJanela.geometry("856x645")
        novaJanela.iconbitmap('imagens/img3.ico')
        novaJanela.frame_PRODUTO = ctk.CTkFrame(master=novaJanela, width=176, height=650, corner_radius=0)
        novaJanela.frame_PRODUTO.pack_propagate(0)
        novaJanela.frame_PRODUTO.pack (fill="y", anchor="w", side="left")
        novaJanela.img7 = PhotoImage(file="imagens/img7.png")
        novaJanela.img7 = novaJanela.img7.subsample(5,5)
        novaJanela.lb_img = ctk.CTkLabel(novaJanela.frame_PRODUTO, text=None, image=novaJanela.img7).pack(anchor="center", ipady=5, pady=(50, 0))
        #BUTTONS FRAME ESQUERDA
        novaJanela.botão_add_estoque = ctk.CTkButton(master=novaJanela.frame_PRODUTO, text="Adicionar Estoque", font=("Century Gothic bold", 14), fg_color="#c64a08",hover_color="#a23d07", anchor="w", command=self.adicionar_estoque).pack(anchor="center", ipady=5, pady=(60, 0))
        novaJanela.botão_atualizar = ctk.CTkButton(master=novaJanela.frame_PRODUTO, text="Atualizar Estoque", font=("Century Gothic bold", 14),  fg_color="#c64a08",hover_color="#a23d07",anchor="w",command=self.atualizar_estoque).pack(anchor="center", ipady=5, pady=(16, 0))
        novaJanela.botão_consultar = ctk.CTkButton(master=novaJanela.frame_PRODUTO, text="Consultar Estoque", font=("Century Gothic bold", 14),  fg_color="#c64a08",hover_color="#a23d07",anchor="w",command=self.consultar_estoque).pack(anchor="center", ipady=5, pady=(16, 0))
        novaJanela.botão_voltarMenu = ctk.CTkButton(master=novaJanela.frame_PRODUTO, width=150, text="Voltar ao Menu", font=("Century Gothic bold", 14), corner_radius=10, fg_color="#444",hover_color="#333", command=self.voltar_ao_menu).pack(side="bottom", pady=15)
        #FRAME DIREITA INICIAL
        novaJanela.title_frame = ctk.CTkFrame(master=novaJanela, fg_color="transparent")
        novaJanela.title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))
        ctk.CTkLabel(master=novaJanela.title_frame, text="Controle de Estoque\nSelecione a opção que deseja.", font=("Arial Black", 25), text_color="#c64a08").pack(anchor="center")
        novaJanela.img2 = PhotoImage(file="imagens/img2.png")
        novaJanela.img2 = novaJanela.img2.subsample(4,4)
        novaJanela.lb_img2 = ctk.CTkLabel(master=novaJanela.title_frame, text=None, image=novaJanela.img2).pack(anchor="center")
    
    def adicionar_estoque(self):
        todos_produtos = self.backend.consultar_produtos()
        JanelaEstoque = ctk.CTkToplevel()
        JanelaEstoque.title("E-STOQUE")
        JanelaEstoque.geometry("700x400")
        JanelaEstoque.iconbitmap('imagens/img3.ico')
        JanelaEstoque.attributes('-topmost', True) 
        JanelaEstoque.add_frame = ctk.CTkFrame(master=JanelaEstoque)
        JanelaEstoque.add_frame.pack(anchor="n", fill='both', expand=True)
        ctk.CTkLabel(master=JanelaEstoque.add_frame, text="Adicionar novo estoque.", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center")

        # Lógica para buscar o código e a descrição do produto selecionado
        opcoes_produtos = [f"{produto[0]} - {produto[1]}" for produto in todos_produtos]

        JanelaEstoque.produto_combobox = ttk.Combobox(JanelaEstoque.add_frame, values=opcoes_produtos)
        JanelaEstoque.produto_combobox.pack(pady=15)

        JanelaEstoque.codigo_produto_entry = ctk.CTkEntry(JanelaEstoque.add_frame, width=300, placeholder_text="Código do Produto", font=("Century Gothic bold", 16), corner_radius=15)
        JanelaEstoque.codigo_produto_entry.pack(pady=15)
        #Atualizar os campos durante a escolha do produto no combobox
        def atualizar_codigo_produto(event):
            item_selecionado = JanelaEstoque.produto_combobox.get()
            codigo_produto = item_selecionado.split(' - ')[0]
            JanelaEstoque.codigo_produto_entry.delete(0, 'end')
            JanelaEstoque.codigo_produto_entry.insert(0, codigo_produto)

        JanelaEstoque.produto_combobox.bind('<<ComboboxSelected>>', atualizar_codigo_produto)
        JanelaEstoque.quantidade_entry = ctk.CTkEntry(JanelaEstoque.add_frame, width=300, placeholder_text="Quantidade", font=("Century Gothic bold", 16), corner_radius=15)
        JanelaEstoque.quantidade_entry.pack(pady=15) 

        JanelaEstoque.botao_salvar = ctk.CTkButton(JanelaEstoque.add_frame, text="Salvar", font=("Century Gothic bold", 16), fg_color="green", corner_radius=15, command=lambda: self.salvar_estoque(JanelaEstoque))
        JanelaEstoque.botao_salvar.pack(side="bottom", pady=30)

    def salvar_estoque(self, JanelaEstoque):
        # Obter o item selecionado
        item_selecionado = JanelaEstoque.produto_combobox.get()
        # Receber o código e a descrição do produto do item selecionado
        codigo_produto, descricao_produto = item_selecionado.split(' - ')

        quantidade = JanelaEstoque.quantidade_entry.get()

        if codigo_produto == "" or quantidade == "" or descricao_produto == "":
            messagebox.showerror(title="E-STOQUE", message="ERRO!\nPreencha todos os campos corretamente!")
        else:
            resultado = self.backend.adicionarestoque(codigo_produto, descricao_produto, quantidade)
            if "ERRO" in resultado:
                messagebox.showerror(title="E-STOQUE", message=resultado)
            else:
                messagebox.showinfo(title="E-STOQUE", message=resultado)
                JanelaEstoque.destroy()

    def atualizar_estoque(self):
        JanelaUPD = ctk.CTkToplevel()
        JanelaUPD.title("E-STOQUE")
        JanelaUPD.geometry("700x400")
        JanelaUPD.iconbitmap('imagens/img3.ico')
        JanelaUPD.attributes('-topmost', True) 
        JanelaUPD.upd_frame = ctk.CTkFrame(master=JanelaUPD)
        JanelaUPD.upd_frame.pack(anchor="n", fill='both', expand=True)
        ctk.CTkLabel(master=JanelaUPD.upd_frame, text="Atualizar estoque.", font=("Arial Black", 25), text_color="#87ceeb").pack(anchor="center")

        JanelaUPD.codigo_produto_entry = ctk.CTkEntry(JanelaUPD.upd_frame, width=300, placeholder_text="Código do Produto", font=("Century Gothic bold", 16), corner_radius=15)
        JanelaUPD.codigo_produto_entry.pack(pady=15)

        JanelaUPD.quantidade_entry = ctk.CTkEntry(JanelaUPD.upd_frame, width=300, placeholder_text="Nova Quantidade", font=("Century Gothic bold", 16), corner_radius=15)
        JanelaUPD.quantidade_entry.pack(pady=15)

        JanelaUPD.botao_salvar = ctk.CTkButton(JanelaUPD.upd_frame, text="Atualizar", font=("Century Gothic bold", 16), corner_radius=15, command=lambda: self.backend.atualizarestoque(JanelaUPD))
        JanelaUPD.botao_salvar.pack(side="bottom", pady=30)
    
    def consultar_estoque(self):
        todos_estoques = self.backend.consultar_estoque()
        def on_select(event):
            for item in tabela.selection():
                item_text = tabela.item(item, "values")
                
                # Cria uma nova janela para as informações completas do estoque
                info_completa = ctk.CTkToplevel(JanelaEstoque)
                info_completa.title("Informações completas do estoque")
                info_completa.geometry("700x400")  # Ajuste o tamanho conforme necessário
                info_completa.attributes('-topmost', True)  # Faz a janela sobrepor todas as outras
                
                # Adiciona widgets Label para exibir as informações do estoque
                ctk.CTkLabel(info_completa, text=f"Código do Produto: {item_text[0]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"Descrição: {item_text[1]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"Quantidade: {item_text[2]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"Valor Total: {item_text[3]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"Data/Hora: {item_text[4]}", font=("Arial", 18, "bold")).pack()

        JanelaEstoque = ctk.CTkToplevel()
        JanelaEstoque.title("E-STOQUE")
        JanelaEstoque.geometry("1280x400")
        JanelaEstoque.iconbitmap('imagens/img3.ico')
        JanelaEstoque.attributes('-topmost', True) 
        JanelaEstoque.Estoque_frame = ctk.CTkFrame(master=JanelaEstoque)
        JanelaEstoque.Estoque_frame.pack(anchor="n", fill='both', expand=True)
        ctk.CTkLabel(master=JanelaEstoque.Estoque_frame, text="Histórico de Estoque", font=("Arial Black", 25), text_color="#87ceeb").pack(anchor="center")

        # Cria a tabela
        style = ttk.Style()
        style.configure("Treeview", background="#000033", foreground="white", fieldbackground="#000033")
        style.configure("Treeview.Heading", background="#000066", foreground="black")

        # Cria um frame para conter a tabela e a barra de rolagem
        frame_tabela = ttk.Frame(JanelaEstoque.Estoque_frame)
        frame_tabela.pack(fill='both', expand=True)

        # Cria a barra de rolagem
        scrollbar = Scrollbar(frame_tabela)
        scrollbar.pack(side='right', fill='y')

        tabela = ttk.Treeview(frame_tabela, columns=("CODIGO_PRODUTO", "DESCRICAO" ,"QUANTIDADE", "VALOR_TOTAL", "DATA_HORA"), show='headings', yscrollcommand=scrollbar.set)
        tabela.column("CODIGO_PRODUTO", width=100)
        tabela.column("DESCRICAO", width=100)
        tabela.column("QUANTIDADE", width=100)
        tabela.column("VALOR_TOTAL", width=100)
        tabela.column("DATA_HORA", width=200)
        tabela.heading("CODIGO_PRODUTO", text="Código do Produto")
        tabela.heading("DESCRICAO", text="Descrição")
        tabela.heading("QUANTIDADE", text="Quantidade")
        tabela.heading("VALOR_TOTAL", text="Valor Total")
        tabela.heading("DATA_HORA", text="Data/Hora")
        tabela.pack(side='left', fill='both', expand=True)

        # Conecta a barra de rolagem à tabela
        scrollbar.config(command=tabela.yview)

        # Adiciona o evento de clique à tabela
        tabela.bind('<<TreeviewSelect>>', on_select)

        for row in todos_estoques:
            # Reordena os valores em 'row' para corresponder à ordem das colunas na tabela
            row = (row[0], row[1], row[2], row[3], row[4])
            tabela.insert('', 'end', values=row)

    def voltar_ao_menu(self):
        self.frontend.voltar_ao_menu()

class GerenciarProducao():
    def __init__(self, novaJanela, frontend, backend):
        self.frontend = frontend
        self.backend = backend
        novaJanela = ctk.CTkToplevel()
        novaJanela.title("E-STOQUE")
        novaJanela.geometry("856x645")
        novaJanela.iconbitmap('imagens/img3.ico')
        novaJanela.frame_PRODUTO = ctk.CTkFrame(master=novaJanela, width=176, height=650, corner_radius=0)
        novaJanela.frame_PRODUTO.pack_propagate(0)
        novaJanela.frame_PRODUTO.pack (fill="y", anchor="w", side="left")
        novaJanela.img5 = PhotoImage(file="imagens/img5.png")
        novaJanela.img5 = novaJanela.img5.subsample(5,5)
        novaJanela.lb_img = ctk.CTkLabel(novaJanela.frame_PRODUTO, text=None, image=novaJanela.img5).pack(anchor="center", ipady=5, pady=(50, 0))
        #BUTTONS FRAME ESQUERDA
        novaJanela.botão_registrar = ctk.CTkButton(master=novaJanela.frame_PRODUTO, width=150,text="Registrar Produção", font=("Century Gothic bold", 14), anchor="center", command=self.registrar_producao).pack(anchor="center", ipady=5, pady=(60, 0))
        novaJanela.botão_alterar = ctk.CTkButton(master=novaJanela.frame_PRODUTO, width=150,text="Alterar Status de\nandamento", font=("Century Gothic bold", 14),anchor="center",command=self.alterar_status).pack(anchor="center", ipady=5, pady=(16, 0))
        novaJanela.botão_consultar = ctk.CTkButton(master=novaJanela.frame_PRODUTO, width=150,text="Consultar Produções", font=("Century Gothic bold", 14),anchor="center",command=self.consultar_producao).pack(anchor="center", ipady=5, pady=(16, 0))
        novaJanela.botão_voltarMenu = ctk.CTkButton(master=novaJanela.frame_PRODUTO, width=150, text="Voltar ao Menu", font=("Century Gothic bold", 14), corner_radius=10, fg_color="#444",hover_color="#333", command=self.voltar_ao_menu).pack(side="bottom", pady=15)
        #FRAME DIREITA INICIAL
        novaJanela.title_frame = ctk.CTkFrame(master=novaJanela, fg_color="transparent")
        novaJanela.title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))
        ctk.CTkLabel(master=novaJanela.title_frame, text="Controle de produção.\nSelecione a opção desejada.", font=("Arial Black", 25), text_color="#87ceeb").pack(anchor="center")
        novaJanela.img2 = PhotoImage(file="imagens/img2.png")
        novaJanela.img2 = novaJanela.img2.subsample(4,4)
        novaJanela.lb_img2 = ctk.CTkLabel(master=novaJanela.title_frame, text=None, image=novaJanela.img2).pack(anchor="center")
     #Config do conteúdo dentro das abas de gerenciar produção
    
    def registrar_producao(self):
        Janela_RegistrarProd = ctk.CTkToplevel()
        Janela_RegistrarProd.title("E-STOQUE")
        Janela_RegistrarProd.geometry("900x600")
        Janela_RegistrarProd.iconbitmap('imagens/img3.ico')
        Janela_RegistrarProd.attributes('-topmost', True) 
        Janela_RegistrarProd.add_frame = ctk.CTkFrame(master=Janela_RegistrarProd)
        Janela_RegistrarProd.add_frame.pack(anchor="n", fill='both', expand=True)

        ctk.CTkLabel(master=Janela_RegistrarProd.add_frame, text="Registrar nova produção", font=("Arial Black", 20), text_color="#87ceeb").pack(anchor="center")
        Janela_RegistrarProd.codigo_entry = ctk.CTkEntry(Janela_RegistrarProd.add_frame, width=400, placeholder_text="Código de registro da produção. EX: 125", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_RegistrarProd.codigo_entry.pack(pady=15)  

        Janela_RegistrarProd.data_inicio = ctk.CTkEntry(Janela_RegistrarProd.add_frame, width=400, placeholder_text="Data de inicio - DD/MM/AAAA", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_RegistrarProd.data_inicio.pack(pady=15)

        Janela_RegistrarProd.produto_produzido = ctk.CTkEntry(Janela_RegistrarProd.add_frame, width=400, placeholder_text="Produto ou material produzido", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_RegistrarProd.produto_produzido.pack(pady=15)  

        Janela_RegistrarProd.descricao_prod = ctk.CTkTextbox(Janela_RegistrarProd.add_frame, width=400, height=150, font=("Century Gothic bold", 16), corner_radius=15)
        Janela_RegistrarProd.descricao_prod.insert('1.0', "Descrição breve sobre a produção")
        Janela_RegistrarProd.descricao_prod.pack(pady=15)

        ctk.CTkLabel(master=Janela_RegistrarProd.add_frame, text="Status da produção", font=("Arial Black", 16), text_color="#87ceeb").pack(anchor="center")
        status_options = ["Iniciando", "Em andamento", "Finalizado"]
        Janela_RegistrarProd.status_combobox = ctk.CTkComboBox(Janela_RegistrarProd.add_frame, values=status_options, font=("Century Gothic bold", 16))
        Janela_RegistrarProd.status_combobox.pack(pady=15)

        Janela_RegistrarProd.botao_salvar = ctk.CTkButton(Janela_RegistrarProd.add_frame, text="Salvar", font=("Century Gothic bold", 16), fg_color="green", corner_radius=15, command=lambda: self.backend.registrarproducao(Janela_RegistrarProd))
        Janela_RegistrarProd.botao_salvar.pack(side="bottom", pady=30)  
    
    def alterar_status(self):
        Janela_AtualizarProd = ctk.CTkToplevel()
        Janela_AtualizarProd.title("E-STOQUE")
        Janela_AtualizarProd.geometry("500x400")
        Janela_AtualizarProd.iconbitmap('imagens/img3.ico')
        Janela_AtualizarProd.attributes('-topmost', True) 
        Janela_AtualizarProd.add_frame = ctk.CTkFrame(master=Janela_AtualizarProd)
        Janela_AtualizarProd.add_frame.pack(anchor="n", fill='both', expand=True)

        ctk.CTkLabel(master=Janela_AtualizarProd.add_frame, text="Atualizar produção", font=("Arial Black", 20), text_color="#87ceeb").pack(anchor="center")
        Janela_AtualizarProd.codigo_entry = ctk.CTkEntry(Janela_AtualizarProd.add_frame, width=400, placeholder_text="Código de registro da produção. EX: 125", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_AtualizarProd.codigo_entry.pack(pady=15)  

        ctk.CTkLabel(master=Janela_AtualizarProd.add_frame, text="Status da produção", font=("Arial Black", 16), text_color="#87ceeb").pack(anchor="center")
        status_options = ["Iniciando", "Em andamento", "Finalizado"]
        Janela_AtualizarProd.status_combobox = ctk.CTkComboBox(Janela_AtualizarProd.add_frame, values=status_options, font=("Century Gothic bold", 16))
        Janela_AtualizarProd.status_combobox.pack(pady=15) 

        Janela_AtualizarProd.descricao_entry = ctk.CTkEntry(Janela_AtualizarProd.add_frame, width=400, placeholder_text="Adicione mais detalhes sobre a produção", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_AtualizarProd.descricao_entry.pack(pady=15)
        
        Janela_AtualizarProd.botao_salvar = ctk.CTkButton(Janela_AtualizarProd.add_frame, text="Salvar", font=("Century Gothic bold", 16), fg_color="green", corner_radius=15, command=lambda: self.backend.atualizarproducao(Janela_AtualizarProd))
        Janela_AtualizarProd.botao_salvar.pack(side="bottom", pady=30) 
    
    def consultar_producao(self):
        todas_producoes = self.backend.consultar_producao()
        def on_select(event):
            for item in tabela.selection():
                item_text = tabela.item(item, "values")
                
                # Cria uma nova janela para as informações completas da produção
                info_completa = ctk.CTkToplevel(JanelaProducao)
                info_completa.title("Informações completas da produção")
                info_completa.geometry("700x400")  # Ajuste o tamanho conforme necessário
                info_completa.attributes('-topmost', True)  # Faz a janela sobrepor todas as outras
                
                # Adiciona widgets Label para exibir as informações da produção
                ctk.CTkLabel(info_completa, text=f"Código: {item_text[0]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"Data de Início: {item_text[1]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"Produto Produzido: {item_text[2]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"Descrição: {item_text[3]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"Status: {item_text[4]}", font=("Arial", 18, "bold")).pack()


        JanelaProducao = ctk.CTkToplevel()
        JanelaProducao.title("E-STOQUE")
        JanelaProducao.geometry("1280x400")
        JanelaProducao.iconbitmap('imagens/img3.ico')
        JanelaProducao.attributes('-topmost', True) 
        JanelaProducao.Producao_frame = ctk.CTkFrame(master=JanelaProducao)
        JanelaProducao.Producao_frame.pack(anchor="n", fill='both', expand=True)
        ctk.CTkLabel(master=JanelaProducao.Producao_frame, text="Histórico de Produções", font=("Arial Black", 25), text_color="#87ceeb").pack(anchor="center")

        # Cria a tabela
        style = ttk.Style()
        style.configure("Treeview", background="#000033", foreground="white", fieldbackground="#000033")
        style.configure("Treeview.Heading", background="#000066", foreground="black")

        # Cria um frame para conter a tabela e a barra de rolagem
        frame_tabela = ttk.Frame(JanelaProducao.Producao_frame)
        frame_tabela.pack(fill='both', expand=True)

        # Cria a barra de rolagem
        scrollbar = Scrollbar(frame_tabela)
        scrollbar.pack(side='right', fill='y')

        tabela = ttk.Treeview(frame_tabela, columns=("CODIGO", "DATA_INICIO", "PRODUTO_PROD", "DESCRICAO", "STATUS"), show='headings', yscrollcommand=scrollbar.set)
        tabela.column("CODIGO", width=100)
        tabela.column("DATA_INICIO", width=100)
        tabela.column("PRODUTO_PROD", width=200)
        tabela.column("DESCRICAO", width=200)
        tabela.column("STATUS", width=100)
        tabela.heading("CODIGO", text="Código")
        tabela.heading("DATA_INICIO", text="Data de Início")
        tabela.heading("PRODUTO_PROD", text="Produto Produzido")
        tabela.heading("DESCRICAO", text="Descrição")
        tabela.heading("STATUS", text="Status")
        tabela.pack(side='left', fill='both', expand=True)

        # Conecta a barra de rolagem à tabela
        scrollbar.config(command=tabela.yview)

        # Adiciona o evento de clique à tabela
        tabela.bind('<<TreeviewSelect>>', on_select)

        if todas_producoes:
            for producao in todas_producoes:
                tabela.insert('', 'end', values=producao)
        else:
            print("Nenhuma produção encontrada.")
    
    def voltar_ao_menu(self):
        self.frontend.voltar_ao_menu()

class GerenciarFornecedor():
    def __init__(self, novaJanela, frontend, backend):
        self.frontend = frontend
        self.backend = backend
        novaJanela = ctk.CTkToplevel()
        novaJanela.title("E-STOQUE")
        novaJanela.geometry("856x645")
        novaJanela.iconbitmap('imagens/img3.ico')
        novaJanela.frame_PRODUTO = ctk.CTkFrame(master=novaJanela, width=176, height=650, corner_radius=0)
        novaJanela.frame_PRODUTO.pack_propagate(0)
        novaJanela.frame_PRODUTO.pack (fill="y", anchor="w", side="left")
        novaJanela.img6 = PhotoImage(file="imagens/img6.png")
        novaJanela.img6 = novaJanela.img6.subsample(5,5)
        novaJanela.lb_img = ctk.CTkLabel(novaJanela.frame_PRODUTO, text=None, image=novaJanela.img6).pack(anchor="center", ipady=5, pady=(50, 0))
        #BUTTONS FRAME ESQUERDA
        novaJanela.botão_cadastrar = ctk.CTkButton(master=novaJanela.frame_PRODUTO, width=150,text="Registrar fornecedor", font=("Century Gothic bold", 14), fg_color="#698bb7",hover_color="#536f94",anchor="center", command=self.adicionar_fornecedor).pack(anchor="center", ipady=5, pady=(60, 0))
        novaJanela.botão_editar = ctk.CTkButton(master=novaJanela.frame_PRODUTO, width=150,text="Atualizar informação", font=("Century Gothic bold", 14),fg_color="#698bb7",hover_color="#536f94",anchor="center",command=self.atualizar_fornecedor).pack(anchor="center", ipady=5, pady=(16, 0))
        novaJanela.botão_apagar = ctk.CTkButton(master=novaJanela.frame_PRODUTO, width=150,text="Apagar fornecedor", font=("Century Gothic bold", 14),fg_color="#698bb7",hover_color="#536f94",anchor="center",command=self.apagar_fornecedor).pack(anchor="center", ipady=5, pady=(16, 0))
        novaJanela.botão_consulta = ctk.CTkButton(master=novaJanela.frame_PRODUTO, width=150,text="Listar fornecedores", font=("Century Gothic bold", 14),fg_color="#698bb7",hover_color="#536f94",anchor="center",command=self.consultar_fornecedores).pack(anchor="center", ipady=5, pady=(16, 0))
        novaJanela.botão_voltarMenu = ctk.CTkButton(master=novaJanela.frame_PRODUTO, width=150, text="Voltar ao Menu", font=("Century Gothic bold", 14), corner_radius=10, fg_color="#444",hover_color="#333", command=self.voltar_ao_menu).pack(side="bottom", pady=15)
        #FRAME DIREITA INICIAL
        novaJanela.title_frame = ctk.CTkFrame(master=novaJanela, fg_color="transparent")
        novaJanela.title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))
        ctk.CTkLabel(master=novaJanela.title_frame, text="Controle de fornecedores.\nSelecione a opção desejada.", font=("Arial Black", 25), text_color="#5f8ac1").pack(anchor="center")
        novaJanela.img2 = PhotoImage(file="imagens/img2.png")
        novaJanela.img2 = novaJanela.img2.subsample(4,4)
        novaJanela.lb_img2 = ctk.CTkLabel(master=novaJanela.title_frame, text=None, image=novaJanela.img2).pack(anchor="center")
    #Config do conteúdo dentro das abas de gerenciar fornecedor
    def adicionar_fornecedor(self):
        Janela_addfornecedor = ctk.CTkToplevel()
        Janela_addfornecedor.title("E-STOQUE")
        Janela_addfornecedor.geometry("700x400")
        Janela_addfornecedor.iconbitmap('imagens/img3.ico')
        Janela_addfornecedor.attributes('-topmost', True) 
        Janela_addfornecedor.add_frame = ctk.CTkFrame(master=Janela_addfornecedor)
        Janela_addfornecedor.add_frame.pack(anchor="n", fill='both', expand=True)
        ctk.CTkLabel(master=Janela_addfornecedor.add_frame, text="Cadastrar novo fornecedor.", font=("Arial Black", 25), text_color="#5f8ac1").pack(anchor="center")

        #Frame para gerenciar as colunas e linhas
        grid_frame = ctk.CTkFrame(Janela_addfornecedor.add_frame)
        grid_frame.pack()

        # Colunas e linhas
        Janela_addfornecedor.razao_social_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="Razão Social", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_addfornecedor.razao_social_entry.grid(row=0, column=0, padx=5, pady=5)
        Janela_addfornecedor.cnpj_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="CNPJ", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_addfornecedor.cnpj_entry.grid(row=1, column=0, padx=5, pady=5)
        Janela_addfornecedor.endereco_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="Endereço", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_addfornecedor.endereco_entry.grid(row=2, column=0, padx=5, pady=5)

        Janela_addfornecedor.telefone_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="Telefone", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_addfornecedor.telefone_entry.grid(row=0, column=1, padx=5, pady=5)
        Janela_addfornecedor.cep_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="CEP", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_addfornecedor.cep_entry.grid(row=1, column=1, padx=5, pady=5)
        Janela_addfornecedor.produtos_fornecidos_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="Produtos Fornecidos", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_addfornecedor.produtos_fornecidos_entry.grid(row=3, column=1, padx=5, pady=5)
        
        Janela_addfornecedor.cidade_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="Cidade", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_addfornecedor.cidade_entry.grid(row=3, column=0, padx=5, pady=5)
        Janela_addfornecedor.uf_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="UF", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_addfornecedor.uf_entry.grid(row=2, column=1, padx=5, pady=5)

        Janela_addfornecedor.botao_salvar = ctk.CTkButton(Janela_addfornecedor.add_frame, text="Salvar", font=("Century Gothic bold", 16), corner_radius=15, command=lambda: self.backend.adicionarfornecedor(Janela_addfornecedor))
        Janela_addfornecedor.botao_salvar.pack(side="bottom", pady=30)
    
    def atualizar_fornecedor(self):
        Janela_attfornecedor = ctk.CTkToplevel()
        Janela_attfornecedor.title("E-STOQUE")
        Janela_attfornecedor.geometry("700x400")
        Janela_attfornecedor.iconbitmap('imagens/img3.ico')
        Janela_attfornecedor.attributes('-topmost', True) 
        Janela_attfornecedor.add_frame = ctk.CTkFrame(master=Janela_attfornecedor)
        Janela_attfornecedor.add_frame.pack(anchor="n", fill='both', expand=True)
        ctk.CTkLabel(master=Janela_attfornecedor.add_frame, text="Atualizar informações de fornecedor:\nInsira o CNPJ e as informações do fornecedor com os devidos ajustes", font=("Arial Black", 16), text_color="#5f8ac1").pack(anchor="center")

        #Frame para gerenciar as colunas e linhas
        grid_frame = ctk.CTkFrame(Janela_attfornecedor.add_frame)
        grid_frame.pack()

        # Colunas e linhas
        Janela_attfornecedor.razao_social_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="Razão Social", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_attfornecedor.razao_social_entry.grid(row=1, column=0, padx=5, pady=5)
        Janela_attfornecedor.cnpj_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="CNPJ", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_attfornecedor.cnpj_entry.grid(row=0, column=0, padx=5, pady=5)
        Janela_attfornecedor.endereco_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="Endereço", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_attfornecedor.endereco_entry.grid(row=2, column=0, padx=5, pady=5)

        Janela_attfornecedor.telefone_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="Telefone", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_attfornecedor.telefone_entry.grid(row=0, column=1, padx=5, pady=5)
        Janela_attfornecedor.cep_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="CEP", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_attfornecedor.cep_entry.grid(row=1, column=1, padx=5, pady=5)
        Janela_attfornecedor.produtos_fornecidos_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="Produtos Fornecidos", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_attfornecedor.produtos_fornecidos_entry.grid(row=2, column=1, padx=5, pady=5)
        
        Janela_attfornecedor.cidade_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="Cidade", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_attfornecedor.cidade_entry.grid(row=3, column=0, padx=5, pady=5)
        Janela_attfornecedor.uf_entry = ctk.CTkEntry(grid_frame, width=300, placeholder_text="UF", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_attfornecedor.uf_entry.grid(row=3, column=1, padx=5, pady=5)

        Janela_attfornecedor.botao_atualizar = ctk.CTkButton(Janela_attfornecedor.add_frame, text="atualizar", font=("Century Gothic bold", 16), corner_radius=15, command=lambda: self.backend.atualizarfornecedor(Janela_attfornecedor))
        Janela_attfornecedor.botao_atualizar.pack(side="bottom", pady=30)

    def apagar_fornecedor(self):
        Janela_ApagarFornecedor = ctk.CTkToplevel()
        Janela_ApagarFornecedor.title("E-STOQUE")
        Janela_ApagarFornecedor.geometry("350x300")
        Janela_ApagarFornecedor.iconbitmap('imagens/img3.ico')
        Janela_ApagarFornecedor.attributes('-topmost', True) 
        Janela_ApagarFornecedor.del_frame = ctk.CTkFrame(master=Janela_ApagarFornecedor)
        Janela_ApagarFornecedor.del_frame.pack(anchor="n", fill='both', expand=True)
        ctk.CTkLabel(master=Janela_ApagarFornecedor.del_frame, text="Apagar fornecedor do sistema:\n Insira o CNPJ e confirme a ação.", font=("Arial Black", 16), text_color="#5f8ac1").pack(anchor="center")
        Janela_ApagarFornecedor.cnpj_entry = ctk.CTkEntry(Janela_ApagarFornecedor.del_frame, width=300, placeholder_text="CNPJ do fornecedor", font=("Century Gothic bold", 16), corner_radius=15)
        Janela_ApagarFornecedor.cnpj_entry.pack(pady=15)  

        Janela_ApagarFornecedor.botao_deletar = ctk.CTkButton(Janela_ApagarFornecedor.del_frame, text="Apagar", font=("Century Gothic bold", 16), corner_radius=15, command=lambda: self.backend.deletarfornecedor(Janela_ApagarFornecedor))
        Janela_ApagarFornecedor.botao_deletar.pack(side="bottom", anchor="center",pady=30)  
    
    def consultar_fornecedores(self):
        todos_fornecedores = self.backend.consultar_fornecedores()
        def on_select(event):
            for item in tabela.selection():
                item_text = tabela.item(item, "values")
                
                # Cria uma nova janela para as informações completas do fornecedor
                info_completa = ctk.CTkToplevel(JanelaFornecedores)
                info_completa.title("Informações completas do fornecedor")
                info_completa.geometry("700x400")  # Ajuste o tamanho conforme necessário
                info_completa.attributes('-topmost', True)  # Faz a janela sobrepor todas as outras
                
                # Adiciona widgets Label para exibir as informações do fornecedor
                ctk.CTkLabel(info_completa, text=f"CNPJ: {item_text[0]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"Razão Social: {item_text[1]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"Endereço: {item_text[2]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"Telefone: {item_text[3]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"CEP: {item_text[4]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"Produtos Fornecidos: {item_text[5]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"Cidade: {item_text[6]}", font=("Arial", 18, "bold")).pack()
                ctk.CTkLabel(info_completa, text=f"UF: {item_text[7]}", font=("Arial", 18, "bold")).pack()


        JanelaFornecedores = ctk.CTkToplevel()
        JanelaFornecedores.title("E-STOQUE")
        JanelaFornecedores.geometry("1280x400")
        JanelaFornecedores.iconbitmap('imagens/img3.ico')
        JanelaFornecedores.attributes('-topmost', True) 
        JanelaFornecedores.Fornecedores_frame = ctk.CTkFrame(master=JanelaFornecedores)
        JanelaFornecedores.Fornecedores_frame.pack(anchor="n", fill='both', expand=True)
        ctk.CTkLabel(master=JanelaFornecedores.Fornecedores_frame, text="Histórico de Fornecedores", font=("Arial Black", 25), text_color="#87ceeb").pack(anchor="center")

        # Cria a tabela
        style = ttk.Style()
        style.configure("Treeview", background="#000033", foreground="white", fieldbackground="#000033")
        style.configure("Treeview.Heading", background="#000066", foreground="black")

        # Cria um frame para conter a tabela e a barra de rolagem
        frame_tabela = ttk.Frame(JanelaFornecedores.Fornecedores_frame)
        frame_tabela.pack(fill='both', expand=True)

        # Cria a barra de rolagem
        scrollbar = Scrollbar(frame_tabela)
        scrollbar.pack(side='right', fill='y')

        tabela = ttk.Treeview(frame_tabela, columns=("CNPJ", "Razao_Social", "Endereco", "Telefone", "CEP", "Produtos_Fornecidos", "Cidade", "UF"), show='headings', yscrollcommand=scrollbar.set)
        tabela.column("CNPJ", width=100)
        tabela.column("Razao_Social", width=200)
        tabela.column("Endereco", width=200)
        tabela.column("Telefone", width=100)
        tabela.column("CEP", width=100)
        tabela.column("Produtos_Fornecidos", width=200)
        tabela.column("Cidade", width=100)
        tabela.column("UF", width=50)
        tabela.heading("CNPJ", text="CNPJ")
        tabela.heading("Razao_Social", text="Razão Social")
        tabela.heading("Endereco", text="Endereço")
        tabela.heading("Telefone", text="Telefone")
        tabela.heading("CEP", text="CEP")
        tabela.heading("Produtos_Fornecidos", text="Produtos Fornecidos")
        tabela.heading("Cidade", text="Cidade")
        tabela.heading("UF", text="UF")
        tabela.pack(side='left', fill='both', expand=True)

        # Conecta a barra de rolagem à tabela
        scrollbar.config(command=tabela.yview)

        # Adiciona o evento de clique à tabela
        tabela.bind('<<TreeviewSelect>>', on_select)

        if todos_fornecedores:
            for fornecedor in todos_fornecedores:
                tabela.insert('', 'end', values=fornecedor)
        else:
            print("Nenhum fornecedor encontrado.")
    
    def voltar_ao_menu(self):
        self.frontend.voltar_ao_menu()
