import sqlite3
import os

class bd:

    def __init__(self):
        caminhoAtual = os.getcwd()

        self.conection = sqlite3.connect('{}\\SalesSystem-master\\SalesDataBase.db'.format(caminhoAtual))
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


    def createTableSale(self):

        command = 'Create table sales ( bar_code int, nome varchar(30), quantidade int, valor double, total double, data date )'

        self.cur.execute(command)
        self.conection.commit()

BancoDados = bd()
#BancoDados.createTableSale()

a = '1234567891012'

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

