from tkinter import *
from tkinter import ttk
from datetime import date

class cont:

    def __init__(self):

        self.windowPrint()

    def windowPrint(self):

        #objeto de data
        data_atual = date.today()

        #armazenar o valor das combos
        #dia = StringVar()
        #mes = StringVar()
        #ano = StringVar()

        #FONTE
        fonteCombos = 'Courier 12'

        self.windowCont = Tk()
        self.windowCont.title('SETOR DE CONTABILIDADE')

        #COMBO DOS DIAS
        lblDias =  Label(self.windowCont, text='SELECIONE O DIA:', font= fonteCombos)
        lblDias.pack()

        comboDia = ttk.Combobox(self.windowCont, width = 27, font= fonteCombos) 

        comboDia['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31') 
        comboDia.current(data_atual.day-1)
        comboDia.pack(pady=5)

        #COMBO DOS MESES
        lblDias =  Label(self.windowCont, text='SELECIONE O MÊS:', font= fonteCombos)
        lblDias.pack()

        comboMes = ttk.Combobox(self.windowCont, width = 27, font= fonteCombos) 

        comboMes['values'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12') 
        comboMes.current(data_atual.month-1)
        comboMes.pack(pady=5)

        #COMBO DOS ANOS
        lblDias =  Label(self.windowCont, text='SELECIONE O ANO:', font= fonteCombos)
        lblDias.pack()

        comboAno = ttk.Combobox(self.windowCont, width = 27, font= fonteCombos)

        comboAno['values'] = ('2020', '2021', '2022', '2023', '2024', '2050', '2026', '2027', '2028', '2029', '2030') 
        comboAno.current(0)
        comboAno.pack(pady=5)

        #LISTA DE PRODUTOS VENDIDOS
        self.listbox = Listbox(self.windowCont, height=19, width=47, font='Courier 10', bg='LemonChiffon')
        self.listbox.pack()

        def buscarProds():
            pass

        #BOTAO DE BUSCA
        btBusca = Button(self.windowCont, text='Buscar', font=fonteCombos, width=20, height=2)
        btBusca.pack(pady=10)

        self.windowCont.mainloop()

cont()