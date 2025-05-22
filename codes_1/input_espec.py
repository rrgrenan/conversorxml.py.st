#Code que inputa as especificações dos produtos na tiny


#import de libs
import pandas as pd
import pyautogui as pa
import openpyxl
import time

pa.PAUSE = 1.0

#receber planilha

caminho_planilha = r"C:\Users\USER\Documents\Planilhas Renan\SIte ready\febella_site_ready\info_febella.xlsx"
planilha = pd.read_excel(caminho_planilha)

pa.hotkey('alt', 'tab') #acessou a tiny

time.sleep(1.5)

for linha in planilha.index[2:]:
    pa.click(x=328, y=246) #clicar na busca
    pa.hotkey('ctrl', 'a')

    #pesquisa e acessa o produto

    pa.write(str(planilha.loc[linha,'COD']))
    print(planilha.loc[linha,'COD'])
    pa.press('enter')

    time.sleep(0.8)

    pa.click(x=385, y=420)
    


    #clica em editar
    time.sleep(1.5)
    pa.click(x=1181, y=152)
    time.sleep(0.8)

    #ir para o campo de especificação
    pa.press('pagedown')
    pa.click(x=333, y=248)
    pa.hotkey('ctrl', 'a')

    #converte o "." automatico de digitação do python em ","
    peso_liq = str(planilha.loc[linha, 'Peso liquido (Kg)']).replace('.', ',')
    peso_brt = str(planilha.loc[linha, 'PESO BRUTO KG']).replace('.', ',')
    largura = str(planilha.loc[linha,'Largura embalagem']).replace('.', ',')
    altura = str(planilha.loc[linha,'Altura embalagem']).replace('.', ',')
    comprimento = str(planilha.loc[linha,'Comprimento embalagem']).replace('.', ',')


    pa.write(peso_liq) #digita o peso liquido
    pa.press('tab')
    pa.write(peso_brt) #digita peso bruto

    pa.click(x=305, y=424) #clica na largura
    pa.hotkey('ctrl', 'a')
    pa.write(largura) #digita largura
    pa.press('tab')

    pa.write(altura) #digita peso altura
    pa.press('tab')

    pa.write(comprimento) #digita peso comprimento 
    pa.click(x=278, y=817) #clicar em salvar
    time.sleep(3)

    pa.click(x=189, y=152) #clicar em voltar

#repete
