#Script para subir todas imagens presentes na planilha

#input Libs

import pyautogui as pa
import pandas as pd
import openpyxl
import time

#Install settings
pa.PAUSE=1.2

# Upload dataFrame
df = pd.read_excel(r'C:\Users\User100\Documents\Arquivos Renan\from drive\Codes Backup\codes_3\imagens_ready.xlsx')

#Entrando o sistema
pa.hotkey('alt', 'tab')

for linha in df.index[5:]:

    pa.click(x=434, y=77) #clinicando no modulo PRODUTOS
    pa.click(x=894, y=234) #clicando em pesquisar
    pa.press('F9') #limpando a pesquisa anterior
    pa.click(x=439, y=284) #Clicando na pesquisa por ean

    #Pesquisar item 
    pa.write(str(df.loc[linha,'Codigo de Barras'])) #digitar ean

    pa.press('enter') #confirmar
    pa.press('f5') #acessar produto

    #inserir imagem
    pa.click(x=645, y=183) #clicar em outro
    pa.click(x=87, y=429) #clicar em pesquisar imagem
    pa.write(str(df.loc[linha,'search']))

    #digitar nome da imagem
    pa.press('enter')
    pa.click(x=895, y=354) #clicar em confirmar
