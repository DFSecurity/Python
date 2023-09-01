
import pandas as pd
from bs4 import BeautifulSoup
import os

filename = 'PRODUTOS_TÉCNICOS.xlsx'
datas = pd.read_excel (filename, sheet_name='Sheet1')

pd.set_option ('display.max_rows', None)

for index, row in datas.iterrows ():

    uuid = row ['UUID TRATADOS']
    produto_tecnico = row ['PRODUTOS TÉCNICOS TRATADOS']

    if pd.notna (uuid):
    
        html_filename = f'{uuid}.html'

        if os.path.exists (html_filename):
        
            with open(html_filename, 'r', encoding='utf-8') as file:
        
                html_content = file.read()

            soup = BeautifulSoup(html_content, 'html.parser')
            p_tags = soup.find_all ('p')
            info_text = [p.strong.get_text () if p.strong else None for p in p_tags]
            info_text = [text for text in info_text if text is not None]

            if info_text:
            
                df = pd.DataFrame ({produto_tecnico: info_text})
                excel_filename = f'{produto_tecnico}.xlsx'
                df.to_excel (excel_filename, index=False)



                






