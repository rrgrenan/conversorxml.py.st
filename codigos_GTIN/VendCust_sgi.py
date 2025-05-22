import pandas as pd
import pyautogui as pa
import openpyxl
import time


base = pd.read_excel(r"C:\Users\User100\Documents\Arquivos Renan\mudança SGI\Envios mar_2025\Produtos\produtos_segmentados\Atualizados para sincronizar\attprecos.xlsx")

# print(base)
              

pa.PAUSE=1.2


pa.hotkey("alt", "tab")
# Codigo pra acessar o sistema 


pa.click(x=439, y=72) #clicar em produtos
pa.click(x=885, y=236) #clicar em pesquisar
pa.click(x=244, y=201) #clica na pesquisa por cod
pa.press('F9')


for linha in base.index[0:]:

    cod = base.loc[linha,"Cod sgi"]
    custo = base.loc[linha,"custo"]
    venda = base.loc[linha,"venda"]

    pa.write(str(cod))
    print("Indice: ", base.loc[linha,"Colunas1"], " ,cod_prod:",cod)
   

    pa.press('enter')
    time.sleep(0.7)
    pa.press("F5")
    pa.click(x=888, y=184) #clicar em alterar

    time.sleep(0.8)

    pa.click(x=114, y=180) #clicar em precificação
    pa.click(x=814, y=545) #clicar no cadeado

    #Digitar compra
    pa.write(str(custo).replace('.',','))
    #tab
    pa.press('tab')
    #Digitar custo
    pa.write(str(custo).replace('.',','))
    #tab x 2
    pa.press('tab', 2)
    #digitar venda
    pa.write(str(venda).replace('.', ','))

    

    pa.click(x=888, y=354) #clicar em confirmar

    time.sleep(0.8)
    pa.click(x=887, y=233)# clicar na pesquisa
    pa.press("F9")



