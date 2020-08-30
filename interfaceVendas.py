from tkinter import *

class interfaceSales(Frame):

    def __init__(self):
        
        self.window = Tk()
        self.window.geometry('1000x800')
        self.window.title('Sales')

        #variavel de codigo de barras
        self.var = StringVar()
        self.var.trace("w", self.on_write)

        #labels information
        self.lblSalesSector = Label(text='SETOR DE VENDAS', width=500, height=1, font='Arial 25 bold', fg='white', bg='DarkRed')
        self.lblSalesSector.pack()

        self.banner = Label(text='', width=500, height=1, font='Arial 25 bold', fg='white', bg='DarkRed')
        self.banner.place(x=0, y=750)

        self.lblBarCod = Label(text='Bar Code:', font='Arial 15 bold')
        self.lblBarCod.place(x=10, y=70)

        self.lblTotal = Label(text='TOTAL: ', fg='black', bg='DarkRed', font='Arial 18 bold')
        self.lblTotal.place(x=680, y=750)

        self.lblAmount = Label(text='TOTAL AMOUNT: ', fg='black', bg='DarkRed', font='Arial 18 bold')
        self.lblAmount.place(x=335, y=750)

        self.lblProducts = Label(text='PRODUCTS ALL', font='Arial 18 bold', bg='DarkRed', fg='white', height=1, width=35)
        self.lblProducts.place(x=445, y=104)

        self.lblProductsInformation = Label(text='Product Information', font='Arial 12 bold')
        self.lblProductsInformation.place(x=10, y=155)

        self.paintingInformation = Label(text='', font='Arial 18 bold', bg='DarkRed', fg='white', width=28, height=14)
        self.paintingInformation.place(x=10, y=179)

        #all products
        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = Listbox(self.window, height=34, width=57, yscrollcommand=self.scrollbar.set, font='Courier 10', bg='LemonChiffon')
        self.listbox.place(x=480, y=160)

        #variable
        self.lblTotalVariable = Label(text='00,00', fg='white', bg='DarkRed', font='Arial 18 bold')
        self.lblTotalVariable.place(x=780, y=750)

        self.lblAmountVariable = Label(text='0', fg='white', bg='DarkRed', font='Arial 18 bold')
        self.lblAmountVariable.place(x=550, y=750)

        self.etCodProd = Entry(self.window, font='Arial 25 bold', fg='white', bg='DarkRed', textvariable=self.var)
        self.etCodProd.place(x=10, y=100)

        #informações do produto
        self.lblNameProd = Label(text='', font='Courier 25 bold', bg='darkred', fg='white')
        self.lblNameProd.place(x=70, y=280)

        self.lblAmountProd = Label(text='', font='Courier 25 bold', bg='darkred', fg='white')
        self.lblAmountProd.place(x=150, y=340)

        #entrar com quantidade
        self.lblShowAmount = Label(text='Amount:', font='Courier 20 bold')
        self.lblShowAmount.place(x=20, y=600)

        self.entryAmountProd = Entry(font='Courier 15 bold', bg='darkred', fg='white')
        self.entryAmountProd.place(x=150, y=605)

        #focar no cogio de barras
        self.etCodProd.focus()

        #sequencia de dados 
        self.listbox.insert("end", 'CODE           PROD.         VAL UNT.  QUANT  VAL TOTAL')

        #teste de inserção
        for i in range(2):
            self.listbox.insert('end', '1234567891012  TECLADO MULTI 150.25    2      300.50')

        self.listbox.ItemIndex = 49;

        #aguadar o enter do usuario
        self.window.bind("<Return>", self.keyPressed)
        self.window.bind("<KeyPress-s>", self.keyPressed)

        self.scrollbar.config(command=self.listbox.get)
        self.window.mainloop()

    def getAmountProd(self):
        amount = self.entryAmountProd.get()

        #quando não a valor retorn 1
        if amount == '':
            return 1

        #caso haja retorna o valor
        return amount

    def on_write(self, *args):
        #pega o codigo de barras
        s = self.var.get()

        #verifica se é igual a 13
        if len(s) == 13:
            #limpa e foca o campo quantidade
            self.etCodProd.delete(0, END)
            self.entryAmountProd.focus()
    
    #trata o pressionamento de uma tecla
    def keyPressed(self, event):
        l = event.keysym
        
        #enter
        if l == 'Return':
            print('QUANT: {}'.format(self.getAmountProd()))
            self.etCodProd.focus()
            
        else:
            print('FINISH SALE')

interfaceSales()