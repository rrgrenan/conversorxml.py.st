#importar libs
import pyautogui as pa
import pandas as pd
import time
import openpyxl
pa.PAUSE = 2

#Importar a base
tabela = pd.read_excel(r"C:\Users\User100\Documents\Arquivos Renan\mudança SGI\Envios mar_2025\Produtos\produtos_segmentados\atualizar_GTINtiny.xlsx")       


# Acessar a tiny
pa.hotkey('alt', 'tab')

#Repetrir para cada produto da base

for linha in tabela.index[0:]:

    #clicar na pesquisa
    pa.click(x=402, y=195)
    pa.hotkey('ctrl', 'a')

    
    #digitar o produto, pesquisar, acessa-lo
    # pa.write(str(tabela.loc[linha, 'SKU']))

    produto = tabela.loc[linha, 'Referência']
    pa.write(str(produto))
    print( 'produto:', produto, 'index =', tabela.loc[linha,'ref'])

    pa.press('enter')
    time.sleep(2)
    pa.click(x=467, y=429)
    time.sleep(1)

    #clicar em editar
    pa.click(x=1137, y=117)

    #clicar em GTIN
    pa.click(x=743, y=581)
    pa.hotkey('ctrl', 'a')

    pa.write(str(tabela.loc[linha, 'GTIN']))


    #salvar e voltar
    pa.click(x=387, y=680)
    time.sleep(3)
    pa.click(x=384, y=113)
    time.sleep(1.8)