import os
from datetime import datetime

class printComprovante:
    
    def __init__(self, conteudo):
        
        self.infos = self.formatListConteudo(conteudo)
        self.caminho = "{}\\imprimir.txt".format(os.getcwd())

        #CREAR ARQ DE IMPRESSÃO
        self.createArqPrint()

        #IMPRIMIR
        self.comprovantePrint()

    def createArqPrint(self):

        #ESCRVE OS DADS NO ARQUIVO DE IMPRESSÃO
        arquivo = open(self.caminho, "w")
        arquivo.write(self.infos)

        arquivo.close()

    def formatListConteudo(self, conteudo):
        #COLOCAR DATA E HORA DA IMPRESSAO
        dh = datetime.now().strftime('%d/%m/%Y %H:%M')

        #PEGAR O VALOR TOTAL DA COMPRA E A QUANTIDADE
        valorCompra = sum([i[4] for i in conteudo])

        printComp = 'Mercadinho São Luiz\n-------------------\nData e Hora: {}\n-------------------\nTOTAL: R${:.2f}\n\n'.format(dh, valorCompra)

        #IMPRIMIR TUPLA DE PRODUTOS
        for i in conteudo:
            nome = '{}{}'.format(i[1], " " * (14 - len(str(i[1]))))
            valor = '{:.2f}{}'.format(i[3], " " * (8 - len(str(i[3]))))
            quant = '{}{}'.format(i[2], " " * (4 - len(str(i[2]))))
            total = '{:.2f}'.format(i[4])

            printComp += '{}{}{}{}\n'.format(nome, valor, quant, total)

        printComp += '\n\n ----> Obrigado e Volte Sempre ! <----'

        return printComp

    def comprovantePrint(self):
        #COMANDO DE IMPRESSÃO
        os.startfile(self.caminho, "print")
