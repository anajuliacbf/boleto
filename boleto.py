print ("Informe o valor do boleto:")
vlrBol = float (input())
print ("Informe o percentual da multa em %:")
percMulta = int (input())
multa = (percMulta * vlrBol) /100
print ("O valor do boleto com atraso será de R$", multa)
