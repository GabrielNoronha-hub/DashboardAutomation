import time
from data import buscaData
from navegacao import navegar 
from dataBase import trataArquivo

def main():
    execucao = True
    while execucao == True:
        buscaData()
        navegar()
        trataArquivo()
        time.sleep(10)
main()