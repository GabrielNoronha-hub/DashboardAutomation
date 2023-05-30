import datetime

def buscaData():
    data_hoje = datetime.datetime.now()
    data_formatada = data_hoje.strftime('%Y_%m_%d')
    return data_formatada