from tkinter import *
from interfaceVendas import *
from interfaceCadastroProduto import *

class menuGeral:

    def __init__(self):

        self.windowMenu = Tk()
        self.windowMenu.title('SISMTEA DE VENDAS -- ISS')
        self.windowMenu.resizable(False, False)
        
        def callModule(wind):
            
            #DESTRUIR JANELA
            #self.windowMenu.destroy()

            if wind == 1:
                #CHAMAR CADASTRO DE PRODUTOS
                interfaceProduct()

            elif wind == 2:
                #CHAMAR VENDAS
                interfaceSales()

            elif wind == 3:
                #CHAMAR BALANÇO DE VENDAS
                pass
                
        lblTitle = Label(text='SISTEMA DE VENDAS -- ISS', font='Courier 25 bold', fg='red')
        lblTitle.pack(pady = 15)

        btRegister = Button(text='CADASTRAR PRODUTO', font='Courier 25 bold', width=25, command=lambda: callModule(1))
        btRegister.pack(pady=10)

        btRegister = Button(text='SETOR DE VENDAS', font='Courier 25 bold', width=25, command=lambda: callModule(2))
        btRegister.pack(pady=10)

        btRegister = Button(text='BALANÇO DE VENDAS', font='Courier 25 bold', width=25,  command=lambda: callModule(3))
        btRegister.pack(pady=10)

        self.windowMenu.mainloop()

menuGeral()