import sqlite3

class bd:

    def __init__(self):
        self.conection = sqlite3.connect('C:\\Users\\Igor\Documents\\Sistema de Vendas\\SalesSystem-master\\SalesDataBaseTemp.db')
        self.cur = self.conection.cursor()

    def registerProduct(self, barCode, name, purchasePrice):
        #inserir dados do produto na tabela
        product = 'INSERT INTO products (bar_code, nome, valor) VALUES({}, "{}", {})'.format(barCode, name, purchasePrice)
        
        self.cur.execute(product)
        self.conection.commit()



BancoDados = bd()
#BancoDados.createTable()

    """
    def excluirTable(self):
        
        t = 'drop table product'

        self.cur.execute(t)
        self.conection.commit()

    def createTable(self):

        command = 'Create table products ( bar_code int primary_key, nome varchar(30), valor double)'

        self.cur.execute(command)
        self.conection.commit()"""

