import pandas as pd
import pyautogui as pa
import openpyxl
import time


base = pd.read_excel(r"C:\Users\User100\Documents\Arquivos Renan\Estoque virtual\Aacadão Jequie\semNCM_atualizados.xlsx")

              

pa.PAUSE=1.5


pa.hotkey("alt", "tab")
# Codigo pra acessar o sistema 


for linha in base.index[217:]:


    pa.click(x=885, y=228) #clicar no campo pesquisa
    pa.hotkey('ctrl', 'a')
    pa.press('del')

     #ESCREVER COD PRODUTO
    produto = base.loc[linha,"COD"]
    pa.write(str(produto))
    print("Indice: ", base.loc[linha,"indice"], " ,cod_prod:",produto)


    pa.press('enter') #pesquisar item
    time.sleep(1)
    pa.click(x=1248, y=341) #clicar em editar
    pa.click(x=429, y=236) #clicar em "fiscais"
    # pa.click(x=653, y=382) #Temporario para excluir os ncm errados
    pa.click(x=543, y=377) #clicar no campo ncm

    time.sleep(0.4)

 #ESCREVER NCM
    pa.write(str(base.loc[linha, 'NCM']))
    time.sleep(0.3)
    pa.click(x=448, y=404) #confirmando o NCM
    time.sleep(0.4)

    pa.press('pagedown')
    time.sleep(0.6)
    pa.click(x=48, y=647) #clicar em salvar

    time.sleep(2.2)







   


