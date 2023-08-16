
# coding: UTF-8

# automation.py

import pyautogui
import os
import time
import datetime
import win32com.client as win32
import tkinter as tk

os.system ('call cmd /k "powershell.exe if (get-process -name OUTLOOK -ErrorAction SilentlyContinue) {start-process OUTLOOK.EXE -ErrorAction SilentlyContinue} else {start-process OUTLOOK.EXE -ErrorAction SilentlyContinue ;} ; & exit"')
time.sleep (4.5)

def show_message (message, duration):

    root = tk.Tk ()
    root.overrideredirect (True)
    root.attributes ('-topmost', True)

    width, height = 820, 150
    x = (root.winfo_screenwidth () - width) // 2
    y = (root.winfo_screenheight () - height) // 2

    label = tk.Label (root, text=message, font=("Arial", 12), anchor="center")
    label.pack (fill="both", expand=True, padx=20, pady=20)

    root.geometry (f"{width}x{height}+{x}+{y}")
    root.after (duration * 1000, root.destroy)

    root.mainloop ()

show_message ('Atenção! Não utilize a máquina enquanto o código estiver sendo executado...', 10)

os.system ('cls')
user_profile = os.getlogin ()

if not os.path.exists (f'C:\\Users\\{user_profile}\\Downloads\data.xlsx'):

    current_date = datetime.datetime.now()
    date_result = current_date - datetime.timedelta (days=90)
    date_result_format = date_result.strftime ('%d/%m/%Y')

    os.chdir (r'C:\Program Files\Google\Chrome\Application')
    os.system ('start chrome.exe "link"')
    time.sleep (10.5)

    def move_click_one ():
    
        pyautogui.mouseDown()
        
        largura_tela, altura_tela = pyautogui.size ()
        
        click_coordinates = [(940, 645), (940, 645), (940, 645)]
        
        for click, move in click_coordinates:
        
            pyautogui.click (click, move)
            time.sleep (3)
        
        time.sleep (10.5)
        pyautogui.moveTo (135, 275)
        pyautogui.click (button='right')
        pyautogui.click ()
        pyautogui.click (button='right')
        time.sleep (1.5)
        pyautogui.press ('backspace', presses=10)
        time.sleep (1.5)
        pyautogui.write (date_result_format)
        time.sleep (3.5)

    move_click_one ()

    def move_click_two ():

        largura_tela, altura_tela = pyautogui.size ()
        pyautogui.moveTo (1850, 325)
        time.sleep (1.5)
        pyautogui.click ()
        time.sleep (1.5)
        pyautogui.moveTo (1850, 320)
        time.sleep (1.5)
        pyautogui.click ()
        time.sleep (1.5)
        pyautogui.moveTo (1835, 335)
        time.sleep (1.5)
        pyautogui.click ()
        time.sleep (1.5)
        pyautogui.moveTo (1150, 850)
        time.sleep (1.5)
        pyautogui.click ()
        time.sleep (20.5)
        
    move_click_two ()

    old_filename = 'data.xlsx'
    current_date = datetime.datetime.now ().strftime ('%d-%m-%Y')
    new_filename = f'Dados_Zeiss_{current_date}.xlsx'
    
    if os.path.exists (f'C:\\Users\\{user_profile}\\Downloads\\{old_filename}'):
    
        if os.path.exists (f'C:\\Users\\{user_profile}\\Downloads\\Dados_Zeiss_{current_date}.xlsx'):

            os.remove (f'C:\\Users\\{user_profile}\\Downloads\\Dados_Zeiss_{current_date}.xlsx')
            
            os.rename (f'C:\\Users\\{user_profile}\\Downloads\\{old_filename}', f'C:\\Users\\{user_profile}\\Downloads\\{new_filename}')
            time.sleep (3.5)

            def send_email (subject, body, recipients, attachment_path):

                outlook = win32.Dispatch ('outlook.application')
                mail = outlook.CreateItem (0)  

                mail.Subject = subject
                mail.Body = body
                mail.HTMLBody = f"""<html><body>{body}<br><br>{get_signature()}</body></html>"""
                mail.To = ';'.join (recipients)
                mail.Recipients.ResolveAll()

                attachment = attachment_path
                mail.Attachments.Add (attachment)

                mail.Send ()

            def get_signature():
            
                img_src = r"signature.png"
                signature = f"""
                <img src="{img_src}" alt="Assinatura">
                """
                
                return signature

            subject = f'RES: follow up - RELATÓRIO DIÁRIO LOGIC - {current_date}'
            body = 'Bom dia!\n\nSegue o relatório atualizado na data de hoje.'
            recipients = ['outlook@hotmail.com']  
            attachment_path = f'C:\\Users\\{user_profile}\\Downloads\\Dados_Zeiss_{current_date}.xlsx'

            send_email (subject, body, recipients, attachment_path)
        
        elif not os.path.exists (f'C:\\Users\\{user_profile}\\Downloads\\{new_filename}'):
        
            os.rename (f'C:\\Users\\{user_profile}\\Downloads\\{old_filename}', f'C:\\Users\\{user_profile}\\Downloads\\{new_filename}')
            time.sleep (3.5)

            def send_email (subject, body, recipients, attachment_path):

                outlook = win32.Dispatch ('outlook.application')
                mail = outlook.CreateItem (0)  
                mail.HTMLBody = f"""<html><body>{body}<br><br>{get_signature()}</body></html>"""
                mail.Subject = subject
                mail.Body = body
                
                mail.To = ';'.join (recipients)
                mail.Recipients.ResolveAll()

                attachment = attachment_path
                mail.Attachments.Add (attachment)

                mail.Send ()

            def get_signature():
            
                img_src = r"signature.png"
                signature = f"""
                <img src="{img_src}" alt="Assinatura">
                """
                
                return signature

            subject = f'RES: follow up - RELATÓRIO DIÁRIO LOGIC - {current_date}'
            body = 'Bom dia!\n\nSegue o relatório atualizado na data de hoje.'
            recipients = ['outlook@hotmail.com']  
            attachment_path = f'C:\\Users\\{user_profile}\\Downloads\\Dados_Zeiss_{current_date}.xlsx'

            send_email (subject, body, recipients, attachment_path)

elif os.path.exists (f'C:\\Users\\{user_profile}\\Downloads\data.xlsx'):
    
    os.remove (f'C:\\Users\\{user_profile}\\Downloads\data.xlsx')

