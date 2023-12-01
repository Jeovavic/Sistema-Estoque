import customtkinter as ctk
from tkinter import *
from frontend import *
from backend import *

class App(ctk.CTk, BackEnd,FrontEnd):
    def __init__(self):
        super().__init__()
        self.config_janela()
        self.tela_login()
        self.cria_tabela()
        
if __name__=="__main__":
    app = App()
    app.mainloop()
