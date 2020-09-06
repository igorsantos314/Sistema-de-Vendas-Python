from tkinter import *
from classDataBase import bd
from tkinter import messagebox

class interfaceProduct(Frame):

    def __init__(self):

        defaultFont = 'Arial 12'

        #OBEJETO DE BANCO DE DADOS
        self.dataBase = bd()

        self.window = Tk()
        self.window.resizable(False, False)
        self.window.title('Product Register')

        #labels information
        lblName = Label(self.window, text='Nome do Produto:', font=defaultFont)
        lblName.pack(pady=5)

        self.etName = Entry(self.window, font=defaultFont)
        self.etName.pack(pady=5)

        lblCode = Label(self.window, text='Codigo do Produto:', font=defaultFont)
        lblCode.pack(pady=5)

        self.etCode = Entry(self.window, font=defaultFont)
        self.etCode.pack(pady=5)

        lblPurchasePrice = Label(self.window, text='Valor R$:', font=defaultFont)
        lblPurchasePrice.pack(pady=5)

        self.etPurchasePrice = Entry(self.window, font=defaultFont)
        self.etPurchasePrice.pack(pady=5)
        
        btSalvar = Button(self.window, text='SALVAR PRODUTOS', font=defaultFont, width=25, height=2, command=self.setProduct)
        btSalvar.pack(pady=5)

        btLimpar = Button(self.window, text='LIMPAR', font=defaultFont, width=25, height=2, command=self.clearEts)
        btLimpar.pack(pady=5)

        btEditar = Button(self.window, text='EDITAR PRODUTOS', font=defaultFont, width=25, height=2, command='')
        btEditar.pack(pady=5)

        self.window.mainloop()

        # ----------------------------- JANELA FECHADA -----------------------------

        
    #gets
    def getEtName(self):
        return self.etName.get().upper()

    def getEtCode(self):
        return self.etCode.get()

    def getEtPurchasePrice(self):
        return self.etPurchasePrice.get()
        
    #cadastrar produto
    def setProduct(self):
        
        try:
            #VERIFICA SE PRODUTO EXISTE
            if self.dataBase.verifyProduct(self.getEtCode()) == False:
                nomeProd = self.getEtName()

                #TRATAR TAMANHO DA PALAVRA
                if len(nomeProd) > 14:
                    nomeProd = nomeProd[:14]

                self.dataBase.registerProduct(self.getEtCode(), nomeProd, self.getEtPurchasePrice().replace(',', '.'))
                messagebox.showinfo('','PRODUTO CADASTRADO COM SUCESSO !')

            else:
                messagebox.showerror('','PRODUTO JÁ ESTÁ CADASTRADO !')
        
        except:
            messagebox.showerror('NÃO FOI POSSÍVEL CADASTRAR ESTE PRODUTO','VERIFIQUE SE AS INFORMAÇÕES ESTÃO CORRETAS!')

        #limpar campos
        self.clearEts()    

    #limpar campos
    def clearEts(self):
        self.etName.delete(0, END)
        self.etCode.delete(0, END)
        self.etPurchasePrice.delete(0, END)

#interfaceProduct()