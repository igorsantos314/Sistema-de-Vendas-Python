from tkinter import *
from classDataBase import *
from tkinter import messagebox
from time import gmtime, strftime

from interfaceCadastroProduto import interfaceProduct
from interfaceContabilidade import cont
from interfaceListaProdutos import listProducts

class interfaceSales(Frame):

    def __init__(self):
        
        self.ConnectionBD = bd()

        #listaProdutosVendidos
        self.listaVenda = []

        self.window = Tk()
        self.window.geometry('1100x680')
        self.window.resizable(False, False)
        self.window.title('SETOR DE VENDAS -- ISS')

        #variavel de codigo de barras
        self.var = StringVar()
        self.var.trace("w", self.on_write)

        #labels information
        self.lblSalesSector = Label(self.window, text='SETOR DE VENDAS', width=500, height=1, font='Arial 25 bold', fg='white', bg='Maroon')
        self.lblSalesSector.pack()

        self.banner = Label(self.window, text='', width=500, height=1, font='Arial 25 bold', fg='white', bg='Maroon')
        self.banner.place(x=0, y=610)

        self.lblBarCod = Label(self.window, text='CÓDIGO DE BARRAS:', font='Arial 15 bold')
        self.lblBarCod.place(x=10, y=70)

        self.lblTotal = Label(self.window, text='TOTAL: ', fg='white', bg='Maroon', font='Arial 18 bold')
        self.lblTotal.place(x=680, y=615)

        self.lblAmount = Label(self.window, text='QUANT. PROD. : ', fg='white', bg='Maroon', font='Arial 18 bold')
        self.lblAmount.place(x=335, y=615)

        self.lblProducts = Label(self.window, text='LISTA DE PRODUTOS', font='Arial 18 bold', bg='Maroon', fg='white', height=1, width=38)
        self.lblProducts.place(x=480, y=104)

        self.lblProductsInformation = Label(self.window, text='Product Information', font='Arial 12 bold')
        self.lblProductsInformation.place(x=10, y=155)

        self.paintingInformation = Label(self.window, text='', font='Arial 18 bold', bg='Maroon', fg='white', width=28, height=12)
        self.paintingInformation.place(x=10, y=179)

        #all products
        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = Listbox(self.window, height=25, width=72, yscrollcommand=self.scrollbar.set, font='Courier 10', bg='LemonChiffon')
        self.listbox.place(x=480, y=160)

        #variable
        self.lblTotalVariable = Label(self.window, text='00.00', fg='LawnGreen', bg='Maroon', font='Arial 25 bold')
        self.lblTotalVariable.place(x=780, y=610)

        self.lblAmountVariable = Label(self.window, text='0', fg='LawnGreen', bg='Maroon', font='Arial 25 bold')
        self.lblAmountVariable.place(x=550, y=610)

        self.etCodProd = Entry(self.window, font='Arial 25 bold', fg='white', bg='Maroon', textvariable=self.var)
        self.etCodProd.place(x=10, y=100)

        #informações do produto
        self.lblNameProd = Label(self.window, text='', font='Courier 30 bold', bg='Maroon', fg='white')
        self.lblNameProd.place(x=70, y=280)

        self.lblValueProduct = Label(self.window, text='', font='Courier 30 bold', bg='Maroon', fg='white')
        self.lblValueProduct.place(x=70, y=340)

        #entrar com quantidade
        self.lblShowAmount = Label(self.window, text='QUANT :', font='Courier 20 bold')
        self.lblShowAmount.place(x=20, y=550)

        self.entryAmountProd = Entry(self.window, font='Courier 15 bold', bg='Maroon', fg='white')
        self.entryAmountProd.place(x=150, y=555)

        #focar no cogio de barras
        self.etCodProd.focus()

        #sequencia de dados 
        self.dadosBaseListBox()

        #teste de inserção
        #for i in range(2):
            #self.listbox.insert('end', '1234567891012  TECLADO MULTI 150.25    2      300.50')

        self.listbox.ItemIndex = 49;

        #INFORMAÇÕES PARA CHAMAR MODULOS
        lblInfo = Label(text='s - FINALIZAR VENDA*   z- CANCELAR VENDA   l - LISTAR PROD.   p - MCP*   c - MBV*', fg='red', font='Courier 8 bold')
        lblInfo.place(x=10, y=660)

        #aguadar o enter do usuario
        self.window.bind("<Return>", self.keyPressed)
        self.window.bind("<KeyPress-s>", self.keyPressed)
        self.window.bind("<KeyPress-p>", self.keyPressed)
        self.window.bind("<KeyPress-c>", self.keyPressed)
        self.window.bind("<KeyPress-z>", self.keyPressed)
        self.window.bind("<KeyPress-l>", self.keyPressed)

        self.scrollbar.config(command=self.listbox.get)
        self.window.mainloop()

    def getAmountProd(self):
        amount = self.entryAmountProd.get()

        #caso haja retorna o valor
        return amount

    def on_write(self, *args):
        #pega o codigo de barras
        s = self.var.get()

        #verifica se é igual a 13
        if len(s) == 13:

            #chamar funcao para adcionar produto e exibir informações
            self.entryProduct(s)

            #limpa e foca o campo quantidade
            self.etCodProd.delete(0, END)
            self.entryAmountProd.focus()
    
    #trata o pressionamento de uma tecla
    def keyPressed(self, event):
        l = event.keysym
        
        #enter
        if l == 'Return':
            
            #CASO NÃO TENHA PASSADO NENHUM PRODUTO
            if self.lblNameProd['text'] != '':

                amount = self.getAmountProd()

                #CAMPO DE QUANTIDADE VAIZO EQUIVALE A 1
                if(amount == ''):
                    amount = 1

                def tratarNome():
                    #TRATAR A STRING DO NOME DO PRODUTO
                    if len(self.productName) >= 8:
                        return self.productName[:8]

                    #RETORNA A STRING FORMATADA 
                    return '{}{}'.format(self.productName, ''*(8 - len(self.productName)))

                nomeP = tratarNome()

                #TUPLA DE INFORMAÇÕES
                data = strftime("%Y-%m-%d", gmtime())
                data = data.replace('-', '')

                tuplaDadosCompra = (self.productCode, nomeP, amount, self.productValue, (int(amount) * self.productValue), data)

                #inserir no listbox
                code = '{}{}'.format(tuplaDadosCompra[0], " " * (14 - len(str(tuplaDadosCompra[0]))))
                nome = '{}{}'.format(tuplaDadosCompra[1], " " * (14 - len(str(tuplaDadosCompra[1]))))
                valor = '{:.2f}{}'.format(tuplaDadosCompra[3], " " * (8 - len(str(tuplaDadosCompra[3]))))
                quant = '{}{}'.format(tuplaDadosCompra[2], " " * (4 - len(str(tuplaDadosCompra[2]))))
                total = '{:.2f}'.format(tuplaDadosCompra[4])

                inforProductAdd = '{}  {}      {}         {}     {}'.format(code, nome, valor, quant, total)
                self.listbox.insert('end', inforProductAdd)

                #ATUALIZAR QUANTIDADE DE PRODUTOS E VALOR
                self.refreshValues(int(amount), (int(amount) * self.productValue))

                #LIMPAR CAIXA DE QUANTIDADE E INFORMAÇÕES DO PRODUTO
                self.entryAmountProd.delete(0, END)
                self.lblNameProd['text'] = ''
                self.lblValueProduct['text'] = ''

                #INSERIR TUPLA NOVA NA LISTA
                self.listaVenda.append(tuplaDadosCompra)

                #FOCAR NO CODIGO DE BARRAS
                self.etCodProd.focus()

            else:
                messagebox.showerror('','POR FAVOR, ENTRE COM ALGUM PRODUTO !')
            
        elif l == "s":
            if self.lblTotalVariable['text'] == '00.00':
                messagebox.showwarning('', 'POR FAVOR, REALIZE UMA COMPRA !')
                
                #LIMPAR S
                self.etCodProd.delete(0, END)

            else:
                #ARMAZENA O VALOR DA COMPRA PARA O TROCO
                valorCompra = self.lblTotalVariable['text']

                #FINALIZA A VENDA
                self.finishSale()

                #CALCULA O TROCO
                self.moduloTroco(valorCompra)
        
        elif l == "p":
            #LIMPAR LOCAL DE CODIGO DE BARRAS
            self.etCodProd.delete(0, END)

            #CADASTRO DE PRODUTOS
            interfaceProduct()

        elif l == "c":
            #LIMPAR LOCAL DE CODIGO DE BARRAS
            self.etCodProd.delete(0, END)

            #CADASTRO DE PRODUTOS
            cont()

        elif l == "z":
            #CANCELAR VENDA E LIMPAR TUDO
            self.saleClean()

        elif l == "l":
            #CALL EM JANELA DE PRODUTOS
            listProducts()

    def finishSale(self):

        if messagebox.askyesno('FINALIZAR COMPRA', 'DESEJA FINALIZAR A COMPRA?') == True:
            
            #--------------------- COMMITAR NO BANCO DE DADOS ---------------------

            for prod in self.listaVenda:

                #ADCIONAR CADA PRODUTO
                self.ConnectionBD.registerSale(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5])

            # --------------------- LIMPAR TODOS OS DADOS ---------------------

            #LIMPAR LISTBOX
            self.listbox.delete(0,'end')
            self.dadosBaseListBox()

            #LIMPAR QUANTIDADE, TOTAL E DADOs DOS PRODUTOS
            self.lblAmountVariable['text'] = '0'
            self.lblTotalVariable['text'] = '00.00'

            self.lblNameProd['text'] = ''
            self.lblValueProduct['text'] = ''

            self.etCodProd.delete(0, END)

            #LIMPAR LISTA DE COMPRA
            self.listaVenda.clear()

            #MENSAGEM DE SUCESSO
            messagebox.showinfo('','COMPRA FINALIZADA COM SUCESSO !')

    def refreshValues(self, newAmount, newValue):

        #SOMAR NOVOS VALORES
        amount = int(self.lblAmountVariable['text']) + newAmount
        value = float(self.lblTotalVariable['text']) + newValue

        #ATUALIZAR VALORES
        self.lblAmountVariable['text'] = amount
        self.lblTotalVariable['text'] = value


    def entryProduct(self, barCodeS):
        
        #connectar com o banco de dados
        barCode = int(barCodeS)

        #retorna os dados do produto
        product = self.ConnectionBD.getProduct(barCode)

        self.productCode = 0
        self.productName = ''
        self.productValue = 0

        if product == []:
            #PRODUTO NÃO CADASTRADO
            messagebox.showerror('', 'Produto não Encontrado !')
            
        else:
            #INFORMAÇÕES DO PRODUTO
            self.productCode = product[0][0]
            self.productName = product[0][1]
            self.productValue = product[0][2]

            #EXIBIR INFORMAÇÕES
            self.lblNameProd['text'] = self.productName
            self.lblValueProduct['text'] = self.productValue
    
    def moduloTroco(self, valor):

        self.windowTroco = Tk()
        self.windowTroco.title('FINZALIZAR VENDA')

        lblValor = Label(self.windowTroco, text='            VALOR DA VENDA:            ', font='Courier 15 bold')
        lblValor.pack()

        lblTotal = Label(self.windowTroco, text='R$ {:.2f}'.format(valor), font='Courier 35 bold', fg='orange')
        lblTotal.pack(pady=8)

        # --------- INFORMAR O VALOR ---------
        lblInformeValor = Label(self.windowTroco, text='            VALOR DO CLIENTE:            ', font='Courier 15 bold')
        lblInformeValor.pack()

        etValor = Entry(self.windowTroco, font='Courier 25 bold', fg='red')
        etValor.pack(pady=8)

        # --------- INFORMAR O TROCO ---------
        #lblTroco = lblInformeValor = Label(self.windowTroco, text='            TROCO:            ', font='Courier 15 bold')
        #lblTroco.pack()

        #lblTrocoValor = Label(self.windowTroco, text='R$ 0.00', font='Courier 35 bold', fg='green')
        #lblTrocoValor.pack(pady=8)

        #FOCAR NO CAMPO VALOR 1234567891012
        etValor.focus()

        def calcTroco():

            if etValor.get() == '':
                pass

            else:
                #ARMAZENAR O VALOR PARA CALCULAR
                vCompra = float(valor)
                vCliente = float(etValor.get())

                if vCompra > vCliente:
                    messagebox.showerror('', 'O VALOR DA COMPRA É MAIOR QUE O VALOR DADO PELO CLIENTE !')

                else:
                    #CALCULAR TROCO
                    troco = vCliente - vCompra
                
                    #EXIBIR TROCO
                    messagebox.showinfo('', 'TROCO: R$ {:.2f}'.format(troco))

                    #FECHAR JANELA DE TROCO
                    self.windowTroco.destroy()

        btCalcTroco = Button(self.windowTroco, text='CALCULAR TROCO', font='Courier 25 bold', height=2, command=calcTroco)
        btCalcTroco.pack(pady=8)

        self.windowTroco.mainloop()
    
    def saleClean(self):

        if messagebox.askyesno('', 'Cancelar venda?') == True:

            #LIMPAR TODOS OS CAMPOS

            #LIMPAR LISTBOX
            self.listbox.delete(0,'end')
            self.dadosBaseListBox()

            #LIMPAR QUANTIDADE, TOTAL E DADOs DOS PRODUTOS
            self.lblAmountVariable['text'] = '0'
            self.lblTotalVariable['text'] = '00.00'

            self.lblNameProd['text'] = ''
            self.lblValueProduct['text'] = ''

            #LIMPAR LISTA DE COMPRA
            self.listaVenda.clear()

            #MENSSAGEM DE SUCESSO
            messagebox.showinfo('','VENDA CANCELADA !')
        
        #LIMPAR LOCAL DO COD BARRAS
        self.etCodProd.delete(0, END)

    def dadosBaseListBox(self):
        
        #DADOS INFORMACIONAIS
        self.listbox.insert("end", 'CODE            PROD.                VAL UNT.       QUANT.  VAL. TOTAL')
        self.listbox.insert("end", '-----------------------------------------------------------------------')

if __name__ == '__main__':
    interfaceSales()
