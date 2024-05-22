import customtkinter as ctk
from db.database import Database

class CadastroVeiculo(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastro de Veículos")
        self.geometry("800x600")
        self.resizable(False, False)

        self.frameTitulo = ctk.CTkFrame(self, width=800, height=100, corner_radius= 0)
        self.frameTitulo.pack(fill='both', expand=False)
        self.frameTitulo.pack_propagate(False)
 
        self.frameItens = ctk.CTkFrame(self, width=800, height=500, corner_radius=0)
        self.frameItens.pack(fill='both', expand=False)
        self.frameItens.pack_propagate(False)
 
        self.labelTitulo = ctk.CTkLabel(self.frameTitulo, text='Cadastrar Veículo', font=('Opens Sans', 26, 'bold'))
        self.labelTitulo.pack(side='bottom')
 
        self.labelPlaca = ctk.CTkLabel(self.frameItens, text='Placa', font=('Opens Sans', 16))
        self.labelPlaca.pack(pady=10)
        self.entryPlaca = ctk.CTkEntry(self.frameItens, font=('Opens Sans', 16))
        self.entryPlaca.pack(pady=5)
 
        self.labelMarca = ctk.CTkLabel(self.frameItens, text='Marca', font=('Opens Sans', 16))
        self.labelMarca.pack(pady=10)
        self.entryMarca = ctk.CTkEntry(self.frameItens, font=('Opens Sans', 16))
        self.entryMarca.pack(pady=5)
 
        self.labelModelo = ctk.CTkLabel(self.frameItens, text='Modelo', font=('Opens Sans', 16))
        self.labelModelo.pack(pady=10)
        self.entryModelo = ctk.CTkEntry(self.frameItens, font=('Opens Sans', 16))
        self.entryModelo.pack(pady=5)
 
        self.labelAno = ctk.CTkLabel(self.frameItens, text='Ano', font=('Opens Sans', 16))
        self.labelAno.pack(pady=10)
        self.entryAno = ctk.CTkEntry(self.frameItens, font=('Opens Sans', 16))
        self.entryAno.pack(pady=5)

        self.btnCadastrar = ctk.CTkButton(self.frameItens, text='Cadastrar', font=('Open Sans', 16), command=self.cadastrar_veiculo)
        self.btnCadastrar.pack(pady=30)

    def cadastrar_veiculo(self):
        placa = self.entryPlaca.get()
        marca = self.entryMarca.get()
        modelo = self.entryModelo.get()
        ano = self.entryAno.get()

        if placa and marca and modelo and ano:
            db = Database('db/locadora.db')
            db.connect()
            query = f"INSERT INTO veiculos (placa, marca, modelo, ano) VALUES ('{placa}', '{marca}', '{modelo}', '{ano}')"
            msg_ok =  "Veiculo cadastrado com sucesso"
            msg_error = "Erro ao cadastrar veículo"
            db.execute_query(query, msg_ok, msg_error)
            db.disconect()
            self.entryPlaca.delete(0, 'end')
            self.entryMarca.delete(0, 'end')
            self.entryModelo.delete(0, 'end')
            self.entryAno.delete(0, 'end')