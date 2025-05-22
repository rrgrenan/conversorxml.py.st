#importar libs
import pyautogui as pa
import pandas as pd
import time
import openpyxl
pa.PAUSE = 2

ase = pd.read_excel(r"C:\Users\User100\Documents\Arquivos Renan\mudança SGI\eansgi_ready.xlsx")       
print(ase)
# Acessar a tiny
pa.hotkey('alt', 'tab')

#Repetrir para cada produto da base

for linha in tabela.index:

    #clicar na pesquisa
    pa.click(x=402, y=195)
    pa.hotkey('ctrl', 'a')

    #digitar o produto, pesquisar, acessa-lo
    pa.write(str(tabela.loc[linha, 'SKU']))
    pa.press('enter')
    pa.click(x=467, y=429)

    #clicar em editar
    pa.click(x=1137, y=117)

    #acessar a caixa de controle de lote e marcar 'sim'
    pa.press('pagedown',2)

    pa.click(x=1124, y=370)
    pa.click(x=1061, y=408)

    #salvar e voltar
    pa.click(x=387, y=680)
    pa.click(x=384, y=113)

