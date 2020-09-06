from tkinter import *
from classDataBase import bd
from tkinter import messagebox

class listProducts:

    def __init__(self):
        
        self.defaultFont = 'Arial 20 bold'

        #OBEJETO DE BANCO DE DADOS
        self.dataBase = bd()

        self.windowProducts = Tk()
        self.windowProducts.resizable(False, False)
        self.windowProducts.title('LISTA DE PRODUTOS -- ISS')

        #BARRA DE FUNÇÕES
        menubar = Menu(self.windowProducts)
        myMenu = Menu(menubar, tearoff=0)

        #Menu de vendedores
        fileMenuSalvar = Menu(myMenu)
        fileMenuSalvar.add_command(label='CÓDIGO DE BARRAS', command=lambda: self.windowChangeCod(self.getBarCode(self.listbox.get(ACTIVE))))
        fileMenuSalvar.add_command(label='NOME', command=lambda: self.windowChangeNome(self.getBarCode(self.listbox.get(ACTIVE))))
        fileMenuSalvar.add_command(label='VALOR', command=lambda: self.windowChangeValor(self.getBarCode(self.listbox.get(ACTIVE))))

        fileMenuSalvar.add_separator()

        fileMenuSalvar.add_command(label='ATUALIZAR LISTA DE PRODUTOS', command=lambda: listProducts())
        menubar.add_cascade(label="EDITAR", menu=fileMenuSalvar)
        
        self.listbox = Listbox(self.windowProducts, height=34, width=42, font='Courier 10', bg='LemonChiffon')
        self.listbox.pack()

        def listProducts():
            
            #LIMPAR PARA REFRESH
            self.listbox.delete(0, END)

            #INSERIR CABEÇALHO
            self.listbox.insert("end", 'CODE             PRODDUTO         VALOR')
            self.listbox.insert("end", '-----------------------------------------')

            #LISTAR PRODUTOS
            for p in self.dataBase.getAllProducts():
                
                data = self.formatProduct(p)
                self.listbox.insert('end', data)

        #LISTA PRODUTOS
        listProducts()

        #configurar file menu
        self.windowProducts.config(menu=menubar)

        self.windowProducts.mainloop()

    def formatProduct(self, p):
        
        #FORMATAR A VISUALIZAR DOS DADOS
        code = '{}{}'.format(p[0], " " * (17 - len(str(p[0]))))
        nome = '{}{}'.format(p[1], " " * (17 - len(p[1])))
        valor = '{}'.format(p[2])

        #MONTA OS DADOS E RETORNA
        data = '{}{}{}'.format(code, nome, valor)

        return data

    #PEGAR O CÓDIGO DE BARRAS
    def getBarCode(self, tuplaProduct):

        l = []

        for i in tuplaProduct:
            
            if i == ' ':
                break

            l.append(i)
                
        #RETORNA APENAS O CÓDIGO DE BARRAS
        return int(''.join(l))

    def windowChangeCod(self, barCode):
        
        window = Tk()
        window.title('PRODUTO: {}'.format(barCode))

        lbl = Label(window, text='DIGITE O NOVO CÓDIGO:', font=self.defaultFont)
        lbl.pack(pady=5)

        etCodNovo = Entry(window, font=self.defaultFont)
        etCodNovo.pack(pady=5)

        bt = Button(window, text='ATUALIZAR PRODUTO', command=lambda: update(), font=self.defaultFont, bg='black', fg='white')
        bt.pack(pady=5)

        def update():

            if messagebox.askyesno('', 'ATUALIZAR CÓDIGO\n DE [{}] PARA [{}]'.format(barCode, etCodNovo.get())) == True and etCodNovo.get() != "":

                #ENVIAR INFORMAÇÔES PARA BD
                self.dataBase.changeCod(barCode, etCodNovo.get())

                messagebox.showinfo('','ATUALIZADO COM SUCESSO !')

                #DESTRUIR JANELA E ATUALIZAR LISTBOX
                window.destroy()
                lambda:listProducts()

        window.mainloop()

    def windowChangeNome(self, barCode):
        
        window = Tk()
        window.title('PRODUTO: {}'.format(barCode))

        lbl = Label(window, text='DIGITE O NOVO NOME:', font=self.defaultFont)
        lbl.pack(pady=5)

        etNomeNovo = Entry(window, font=self.defaultFont)
        etNomeNovo.pack(pady=5)

        bt = Button(window, text='ATUALIZAR PRODUTO', command=lambda: update(), font=self.defaultFont, bg='black', fg='white')
        bt.pack(pady=5)

        def update():

            if messagebox.askyesno('', 'ATUALIZAR NOME PARA [{}]'.format(etNomeNovo.get())) == True and etNomeNovo.get() != "":

                #ENVIAR INFORMAÇÔES PARA BD
                self.dataBase.changeName(barCode, etNomeNovo.get().upper())

                messagebox.showinfo('','ATUALIZADO COM SUCESSO !')

                #DESTRUIR JANELA E ATUALIZAR LISTBOX
                window.destroy()
                lambda:listProducts()

        window.mainloop()

    def windowChangeValor(self, barCode):
        
        window = Tk()
        window.title('PRODUTO: {}'.format(barCode))

        lbl = Label(window, text='DIGITE O NOVO VALOR:', font=self.defaultFont)
        lbl.pack(pady=5)

        etValorNovo = Entry(window, font=self.defaultFont)
        etValorNovo.pack(pady=5)

        bt = Button(window, text='ATUALIZAR PRODUTO', command=lambda: update(), font=self.defaultFont, bg='black', fg='white')
        bt.pack(pady=5)

        def update():

            if messagebox.askyesno('', 'ATUALIZAR VALOR PARA [{}]'.format(etValorNovo.get())) == True and etValorNovo.get() != "":

                #ENVIAR INFORMAÇÔES PARA BD
                self.dataBase.changeValue(barCode, etValorNovo.get().replace(',','.'))

                messagebox.showinfo('','ATUALIZADO COM SUCESSO !')

                #DESTRUIR JANELA E ATUALIZAR LISTBOX
                window.destroy()
                lambda:listProducts()

        window.mainloop()

#listProducts()