from tkinter import Tk, FALSE, Frame, Label, Entry
from tkinter.ttk import Style
from PIL import Image, ImageTk

import locale

# Defina a localidade para o país da moeda utilizada
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Cores ---------------------------------------------

co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#F3E99F"
co6 = "#03091f"
 
janela = Tk()
janela.title("Calculadora de Investimento - AlphaTest 0.1")
janela.geometry("400x350")
janela.configure(background=co1) 
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Frames --------------------------------------------
frameCima = Frame(janela, width=450, height=50, bg=co1, relief="flat",)
frameCima.grid(row=0, column=0)

framePergunta = Frame(janela, width=450, height=100, bg=co1, relief="solid",)
framePergunta.grid(row=1, column=0, padx=5, sticky="nsew")

frameResultado = Frame(janela, width=300, height=310, bg='#4E6E81', relief="raised",)
frameResultado.grid(row=3, column=0, sticky="nsew")

frameDia = Frame(frameResultado, width=200, height=100, bg=co1, relief="solid",)
frameDia.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")

frameSemana = Frame(frameResultado, width=200, height=100, bg=co1, relief="solid",)
frameSemana.grid(row=0, column=1, padx=1, pady=1, sticky="nsew")

frameMes = Frame(frameResultado, width=200, height=100, bg=co1, relief="solid",)
frameMes.grid(row=1, column=0, padx=1, pady=1, sticky="nsew")

frameTotal = Frame(frameResultado, width=200, height=100, bg=co1, relief="solid",)
frameTotal.grid(row=1, column=1, padx=1, pady=1, sticky="nsew")

# Logo ----------------------------------------------

# Abrindo a imagem
app_img = Image.open("logo.png")
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text="Calculadora de Investimento", font=("Verdana, 14"), width=350, compound="left", padx=5, anchor="center", bg=co1, fg=co0)
app_logo.place(x=5, y=0)

l_linha = Label(frameCima, width=450, height=1, font=("Verdana, 1"), bg='#4E6E81', fg=co1)
l_linha.place(x=0, y=48)

# Frame Pergunta -----------------------------------

app_ = Label(framePergunta, text="Investimento", width=20, font=("Verdana, 10"), anchor="nw", bg=co1, fg=co0)
app_.place(x=50, y=15)
e_valor = Entry(framePergunta, width=10, font=("Ivy, 22"), justify="center", relief="solid", bg='#F3E99F', fg='#4E6E81')
e_valor.place(x=5, y=50)

app_ = Label(framePergunta, text="Dias*", width=10, font=("Verdana, 10"), anchor="nw", bg=co1, fg=co0)
app_.place(x=200, y=15)
e_valor_dias = Entry(framePergunta, width=5, font=("Ivy, 22"), justify="center", relief="solid", bg='#F3E99F', fg='#4E6E81')
e_valor_dias.place(x=174, y=50)

app_ = Label(framePergunta, text="Porcentagem %", width=13, font=("Verdana, 10"), anchor="nw", bg=co1, fg=co0)
app_.place(x=260, y=15)
e_valor_porcentagem = Entry(framePergunta, width=5, font=("Ivy, 22"), justify="center", relief="solid", bg='#F3E99F', fg='#4E6E81')
e_valor_porcentagem.place(x=270, y=50)

# Função para calcular -----------------------------

def calcular_lucro(event):
    try:
        investimento_inicial = float(e_valor.get())
        dias_de_investimento = int(e_valor_dias.get())
        retorno_garantido = float(e_valor_porcentagem.get())
        
        retorno_diario = retorno_garantido / 100 / dias_de_investimento
        
        lucro_diario = investimento_inicial * retorno_diario
        lucro_semanal = lucro_diario * 7
        lucro_mensal = lucro_semanal * 30
        lucro_total = investimento_inicial * (1 + retorno_garantido / 100)
        
        app_dia['text'] = locale.currency(lucro_diario, symbol=True, grouping=True)
        app_semana['text'] = locale.currency(lucro_semanal, symbol=True, grouping=True)
        app_mes['text'] = locale.currency(lucro_mensal, symbol=True, grouping=True)
        app_total['text'] = locale.currency(lucro_total, symbol=True, grouping=True)
        
    except ValueError as e:
       pass

# Frame Resultado ----------------------------------

# Diário
app_ = Label(frameDia, text="Lucro Diário", width=15, anchor="center", font=("Verdana, 11"), bg=co1, fg='#4E6E81')
app_.place(x=20, y=7)

app_dia = Label(frameDia, text="", width=10, anchor="center", font=("Verdana, 15"), bg=co1, fg=co0)
app_dia.place(x=20, y=35)

# Semanal
app_ = Label(frameSemana, text="Lucro Semanal", width=15, anchor="center", font=("Verdana, 11"), bg=co1, fg='#4E6E81')
app_.place(x=20, y=7)

app_semana = Label(frameSemana, text="", width=10, anchor="center", font=("Verdana, 15"), bg=co1, fg=co0)
app_semana.place(x=20, y=35)

# Mensal
app_ = Label(frameMes, text="Lucro Mensal", width=15, anchor="center", font=("Verdana, 11"), bg=co1, fg='#4E6E81')
app_.place(x=20, y=7)

app_mes = Label(frameMes, text="", width=10, anchor="center", font=("Verdana, 15"), bg=co1, fg=co0)
app_mes.place(x=20, y=35)

# Total
app_ = Label(frameTotal, text="Montante", width=15, anchor="center", font=("Verdana, 11"), bg=co1, fg='#4E6E81')
app_.place(x=20, y=7)

app_total = Label(frameTotal, text="", width=10, anchor="center", font=("Verdana, 15"), bg=co1, fg=co0)
app_total.place(x=20, y=35)


# Vincule o evento KeyRelease ao Widget Entry e chame a Função calcular_lucro
e_valor.bind("<KeyRelease>", calcular_lucro)
e_valor_dias.bind("<KeyRelease>", calcular_lucro)
e_valor_porcentagem.bind("<KeyRelease>", calcular_lucro)

janela.mainloop()

# TESTE.
