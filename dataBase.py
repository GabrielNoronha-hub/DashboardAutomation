from data import buscaData
import shutil, os 

def trataArquivo():
    # Busca o arquivo que foi baixado e o renomeia
    os.rename("C:/Users/######/Downloads/report-configuration_summary_" + buscaData() + ".csv", "C:/Users/#####/Downloads/report-configuration_summary.csv")  
    # Move o arquivo de diretorio   
    shutil.move("C:/Users/#####/Downloads/report-configuration_summary.csv", "C:/Users/#####/OneDrive/report-configuration_summary.csv")