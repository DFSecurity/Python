import os
import pandas as pd
from bs4 import BeautifulSoup
import shutil

def extract_info_and_save_to_excel(html_filenames, output_filename):
    all_info_text = []

    for html_filename in html_filenames:
        with open(html_filename, 'r', encoding='utf-8') as arquivo:
            html_content = arquivo.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        p_tags = soup.find_all('p')
        info_text = [p.strong.get_text() if p.strong else None for p in p_tags]
        info_text = [texto for texto in info_text if texto is not None]
        
        all_info_text.extend(info_text)

    if all_info_text:
        df = pd.DataFrame({'FABRICANTES': all_info_text})
        df.to_excel(output_filename, index=False)

html_directory = f'C:\\Users\\rycmi\\GIAGRO\\technical_products'

html_filenames = [os.path.join(html_directory, filename) for filename in os.listdir(html_directory) if filename.endswith('.html')]

output_filename = 'PRODUTOS TÉCNICOS TRATADOS.xlsx'

extract_info_and_save_to_excel(html_filenames, output_filename)

user_profile = os.getlogin ()

destination_path = os.path.join('C:\\Users', user_profile, 'GIAGRO', 'technical_products')
shutil.move(output_filename, os.path.join(destination_path, output_filename))







