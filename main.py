# funcao para calcular
def calcular_lucro(investimento_inicial, dias_de_investimento, retorno_garantido):
    retorno_diario = retorno_garantido / 100 / dias_de_investimento
    
    lucro_diario = dias_de_investimento * retorno_diario
    lucro_semanal = lucro_diario * 7
    lucro_mensal = lucro_semanal * 30
    lucro_total = lucro_mensal * ( 1 + retorno_garantido / 100)
    
    print("Lucro diário: {:.2f}".format(lucro_diario))
    print("Lucro Semanal: {:.2f}".format(lucro_semanal))
    print("Lucro Mensal: {:.2f}".format(lucro_mensal))
    print("Lucro Total: {:.2f}".format(lucro_total))
    
calcular_lucro(5000,30,5)