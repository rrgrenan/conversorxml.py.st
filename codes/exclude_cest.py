#importar libs
import pyautogui as pa
import pandas as pd
import time
import openpyxl
pa.PAUSE = 2

tabela = pd.read_excel(r"C:\Users\User100\Documents\Arquivos Renan\deleting_cest.xlsx")

#Acessar a tiny
pa.hotkey('alt', 'tab')

#Repetrir para cada produto da base

for linha in tabela.index[151:]:

    #clicar na pesquisa
    pa.click(x=402, y=195)
    pa.hotkey('ctrl', 'a')

    #digitar o produto, pesquisar, acessa-lo
    pa.write(str(tabela.loc[linha, 'Código (SKU)']))
    pa.press('enter')
    
    time.sleep(2)
    pa.click(x=424, y=360)

    #clicar em editar
    time.sleep(2)
    pa.click(x=1137, y=117)

    #Selecionar e deletar o CEST
    time.sleep(3)
    pa.click(x=879, y=528)
    pa.hotkey('ctrl','a')
    pa.press('del')

    #salvar e voltar
    pa.click(x=387, y=680)
    time.sleep(4)
    pa.click(x=384, y=113)
    pa.sleep(3)

