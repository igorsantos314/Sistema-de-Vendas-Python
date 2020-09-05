from tkinter import *
from classDataBase import bd

class listProducts:

    def __init__(self):

        #OBEJETO DE BANCO DE DADOS
        self.dataBase = bd()

        self.windowProducts = Tk()
        self.windowProducts.resizable(False, False)
        self.windowProducts.title('LISTA DE PRODUTOS -- ISS')

        self.listbox = Listbox(self.windowProducts, height=34, width=42, font='Courier 10', bg='LemonChiffon')
        self.listbox.pack()

        #INSERIR CABEÇALHO
        self.listbox.insert("end", 'CODE             PRODDUTO         VALOR')
        self.listbox.insert("end", '-----------------------------------------')

        #LISTAR PRODUTOS
        for p in self.dataBase.getAllProducts():
            
            data = self.formatProduct(p)
            self.listbox.insert('end', data)

        self.windowProducts.mainloop()

    def formatProduct(self, p):
        
        #FORMATAR A VISUALIZAR DOS DADOS
        code = '{}{}'.format(p[0], " " * (17 - len(str(p[0]))))
        nome = '{}{}'.format(p[1], " " * (17 - len(p[1])))
        valor = '{}'.format(p[2])

        #MONTA OS DADOS E RETORNA
        data = '{}{}{}'.format(code, nome, valor)

        return data

#listProducts()