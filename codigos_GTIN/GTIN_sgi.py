import pandas as pd
import pyautogui as pa
import openpyxl
import time


base = pd.read_excel(r"C:\Users\User100\Documents\Arquivos Renan\mudança SGI\Envios mar_2025\Produtos\produtos_segmentados\Nova pasta\gerar_sgi_repetidos_vsc.xlsx")

# print(base)
              

pa.PAUSE=1.3


pa.hotkey("alt", "tab")
# Codigo pra acessar o sistema 


pa.click(x=439, y=72) #clicar em produtos
pa.click(x=885, y=236) #clicar em pesquisar
pa.click(x=244, y=201) #clica na pesquisa por ID
pa.press('F9')


for linha in base.index[166:]:

    cod = base.loc[linha,"cod_prod"]
    pa.write(str(cod))
    print("Indice: ", base.loc[linha,"Colunas1"], " ,cod_prod:",cod)

    time.sleep(0.8)    

    pa.press('enter')
    pa.press("F5")
    pa.click(x=888, y=184) #clicar em alterar

    time.sleep(0.8)

    pa.click(x=133, y=454) #clicar em gerar codigo
    # pa.press('enter') #Clicar em ok quando acusar codigo repetido
    # pa.click(x=133, y=454) #clicar em gerar codigo novamente

    time.sleep(0.8)

    pa.click(x=888, y=354) #clicar em confirmar

    pa.click(x=887, y=233)# clicar na pesquisa
    pa.press("F9")

    # pa.click(x=286, y=197) #clicar em pesquisar pelo id
    # pa.press("backspace",5)


