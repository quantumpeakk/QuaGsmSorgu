import requests
import time
import sys
import os
from colorama import init, Fore, Style

init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text, color=Fore.WHITE, delay=0.03):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def draw_box(title, subtitle=""):
    width = 50
    print(Fore.MAGENTA + "┌" + "─" * (width-2) + "┐")
    print("│" + title.center(width-2) + "│")
    if subtitle:
        print("│" + subtitle.center(width-2) + "│")
    print("└" + "─" * (width-2) + "┘" + Style.RESET_ALL)

def query_gsm(gsm):
    url = f"https://api.hexnox.pro/sowixapi/gsmdetay.php?gsm={gsm}"
    try:
        animate_text("\nSorgu gönderiliyor...", Fore.MAGENTA)
        response = requests.get(url)
        if response.status_code == 200:
            try:
                return response.json()
            except:
                return {"API Hatası": "Geçersiz yanıt formatı"}
        return {"Hata": f"API hatası: {response.status_code}"}
    except Exception as e:
        return {"Hata": str(e)}

def show_results(data):
    if not data or "Hata" in data:
        animate_text("\nSonuç bulunamadı veya hata oluştu!", Fore.RED)
        print(Fore.RED + str(data))
        return
    
    print(Fore.RED + "\n╔" + "═" * 48 + "╗")
    print("║" + "SONUÇLAR".center(48) + "║")
    print("╠" + "═" * 48 + "╣")
    
    for key, value in data.items():
        value_str = str(value) if value is not None else "Bilinmiyor"
        print("║ " + Fore.MAGENTA + f"{str(key):<15}" + Fore.RED + " : " + Fore.WHITE + f"{value_str:<28}" + Fore.RED + "║")
    
    print("╚" + "═" * 48 + "╝" + Style.RESET_ALL)

def main_menu():
    clear_screen()
    draw_box("TEL NO SORGULAMA ARACI", "Yapımcı: quantumpeak")
    
    while True:
        print(Fore.MAGENTA + "\n" + "═" * 50)
        print(Fore.WHITE + "1. TEL NO SORGULAMA")
        print(Fore.RED + "2. ÇIKIŞ")
        print(Fore.MAGENTA + "═" * 50 + Style.RESET_ALL)
        
        choice = input(Fore.WHITE + "\nSeçiminiz (1-2): " + Style.RESET_ALL)
        
        if choice == "1":
            clear_screen()
            draw_box("TEL NO SORGULAMA ARACI", "Yapımcı: quantumpeak")
            animate_text("\nGSM Numarası (5XXXXXXXX): ", Fore.MAGENTA)
            gsm = input().strip()
            
            if not (gsm.isdigit() and len(gsm) == 10 and gsm.startswith('5')):
                animate_text("Geçersiz numara! 5 ile başlayan 10 haneli olmalı.", Fore.RED)
                time.sleep(2)
                continue
            
            data = query_gsm(gsm)
            show_results(data)
            
            input(Fore.MAGENTA + "\nTekrar sorgu yapmak için ENTER'a basın..." + Style.RESET_ALL)
            clear_screen()
            draw_box("TEL NO SORGULAMA ARACI", "Yapımcı: quantumpeak")
            
        elif choice == "2":
            animate_text("\nÇıkış yapılıyor...", Fore.RED)
            time.sleep(1)
            clear_screen()
            break
            
        else:
            animate_text("\nGeçersiz seçim! Lütfen 1 veya 2 girin.", Fore.RED)
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
