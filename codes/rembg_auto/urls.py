import pyautogui as pa
import pandas as pd
import time

planilha = pd.read_excel(r"C:\Users\USER\Documents\Planilhas Renan\codes\rembg_auto\extracao2.xlsx")
print(planilha)

pa.PAUSE = 1.0

site = 'https://www.remove.bg/pt-br/upload'

pa.hotkey('alt', 'tab')

pa.press('win')
pa.write('chorme')
pa.press('enter')


pa.write(site)
pa.press('enter')

time.sleep(2)

for linha in planilha.index[73:]:

    pa.click(x=698, y=572)
    pa.write(str(planilha.loc[linha,'URL']))
    pa.press('enter') #pesquisou

    time.sleep(8)
    pa.click(x=912, y=527) #fez download

    pa.hotkey('alt', 'tab')
    pa.press('f5')
    pa.click(x=233, y=241)
    pa.press('f2')
    pa.write(str(planilha.loc[linha,'COD']))
    pa.press('enter')
    pa.hotkey('alt', 'tab')

    time.sleep(2)

    pa.click(1385, y=816)