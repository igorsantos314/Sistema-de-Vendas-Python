from tkinter import *
from classDataBase import bd

class interfaceProduct(Frame):

    def __init__(self):

        defaultFont = 'Arial 12'

        #objeto de banco de dados
        self.dataBase = bd()

        self.window = Tk()
        self.window.geometry('300x200')
        self.window.title('Product Register')

        #labels information
        lblName = Label(text='Nome do Produto:', font=defaultFont)
        lblName.pack(pady=5)

        self.etName = Entry(font=defaultFont)
        self.etName.pack(pady=5)

        lblCode = Label(text='Codigo do Produto:', font=defaultFont)
        lblCode.pack(pady=5)

        self.etCode = Entry(font=defaultFont)
        self.etCode.pack(pady=5)

        lblPurchasePrice = Label(text='Valor R$:', font=defaultFont)
        lblPurchasePrice.pack(pady=5)

        self.etPurchasePrice = Entry(font=defaultFont)
        self.etPurchasePrice.pack(pady=5)

        #Menu
        myMenu = Menu(self.window, tearoff=0)
        fileMenu = Menu(myMenu)

        fileMenu.add_command(label='Save Product', command=self.setProduct)
        fileMenu.add_command(label='Clear', command=self.clearEts)
        myMenu.add_cascade(label='File', menu=fileMenu)

        self.window.config(menu=myMenu)
        self.window.mainloop()

    #gets
    def getEtName(self):
        return self.etName.get().upper()

    def getEtCode(self):
        return self.etCode.get()

    def getEtPurchasePrice(self):
        return self.etPurchasePrice.get()
        
    #cadastrar produto
    def setProduct(self):

        self.dataBase.registerProduct(self.getEtCode(), self.getEtName(), self.getEtPurchasePrice())
        #self.dataBase.registerProduct("TECLADO MULTILASER", '1234567891011', 5, 120.25, 150.50, 30.25)

        #limpar campos
        self.clearEts()

    #limpar campos
    def clearEts(self):
        self.etName.delete(0, END)
        self.etCode.delete(0, END)
        self.etPurchasePrice.delete(0, END)

interfaceProduct()