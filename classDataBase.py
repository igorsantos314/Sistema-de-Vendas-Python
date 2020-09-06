import sqlite3
import os

class bd:

    def __init__(self):
        caminhoAtual = os.getcwd()

        self.conection = sqlite3.connect('{}\\SalesDataBase.db'.format(caminhoAtual))
        self.cur = self.conection.cursor()

    def registerProduct(self, barCode, name, purchasePrice):
        #inserir dados do produto na tabela
        product = 'INSERT INTO products (bar_code, nome, valor) VALUES({}, "{}", {})'.format(barCode, name, purchasePrice)
        
        self.cur.execute(product)
        self.conection.commit()

    def registerSale(self, barCode, nome, quant, valor, total, data):
        #INSERIR DADOS NA TABELA DE VENDAS
        sale = 'INSERT INTO sales (bar_code, nome, quantidade, valor, total, data) VALUES({}, "{}", {}, {}, {}, {})'.format(barCode, nome, quant, valor, total, data)
        
        self.cur.execute(sale)
        self.conection.commit()

    def getProduct(self, barCode):
        
        show = "SELECT * FROM products WHERE bar_code = {}".format(barCode)
        self.cur.execute(show)

        product = self.cur.fetchall()

        return product

    def getProductsSales(self, data):

        #RETORNA LISTA DE PRODUTOS VENDIDOS POR DATA
        show = "SELECT * FROM sales WHERE data = {}".format(data)
        self.cur.execute(show)

        listProduct = self.cur.fetchall()

        return listProduct

    def getAllProducts(self):

        #RETORNA LISTA DE PRODUTOS 
        show = "SELECT * FROM products"
        self.cur.execute(show)

        listProduct = self.cur.fetchall()

        return listProduct

    def changeCod(self, barCodeOld, barCodeNew):

        show = ('UPDATE products SET bar_code = {} WHERE bar_code= {}'.format(barCodeNew, barCodeOld))
        self.cur.execute(show)

        #CONSOLIDAR NA BASE DE DADOS
        self.conection.commit()

    def changeName(self, barCode, name):

        show = ('UPDATE products SET nome = "{}" WHERE bar_code= {}'.format(name, barCode))
        self.cur.execute(show)

        #CONSOLIDAR NA BASE DE DADOS
        self.conection.commit()
    
    def changeValue(self, barCode, value):

        show = ('UPDATE products SET valor = {} WHERE bar_code= {}'.format(value, barCode))
        self.cur.execute(show)

        #CONSOLIDAR NA BASE DE DADOS
        self.conection.commit()

    def createTableSale(self):

        command = 'Create table sales ( bar_code int, nome varchar(30), quantidade int, valor double, total double, data date )'

        self.cur.execute(command)
        self.conection.commit()

    def verifyProduct(self, barCode):

        try:
            show = "SELECT * FROM products WHERE bar_code = {}".format(barCode)
            self.cur.execute(show)

            if self.cur.fetchall() == []:
                return False
            
            return True
        
        except:
            pass


BancoDados = bd()
#BancoDados.changeCod(8888888888888, 123)
#BancoDados.changeName(123, 'CARTEIRA')
#BancoDados.changeValue(123, 12.5)
#BancoDados.createTableSale()

"""
    def excluirTable(self):
        
        t = 'drop table product'

        self.cur.execute(t)
        self.conection.commit()

    def createTable(self):

        command = 'Create table products ( bar_code int primary_key, nome varchar(30), valor double)'

        self.cur.execute(command)
        self.conection.commit()
        
    """

