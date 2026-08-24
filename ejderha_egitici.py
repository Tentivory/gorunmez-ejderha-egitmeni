#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GÖRÜNMEZ EJDERHA EĞİTMENİ v0.0.1
=================================
Bu yazılım, insanlığın en büyük sorunlarından birini çözmek için tasarlanmıştır:
Görünmez ejderhaların disiplin eksikliği.

DİKKAT: Ejderhanız görünmez olduğu için sonuçları görmeniz imkansızdır.
Bu tamamen normaldir ve başarı göstergesidir.
"""

import time
import random
import sys

def baslik():
    print("=" * 60)
    print("   GÖRÜNMEZ EJDERHA EĞİTMENİ")
    print("   Bilimsel • Ciddi • Kesinlikle Çalışıyor")
    print("=" * 60)
    print()

def ejderha_cagir():
    print("Ejderhanızı çağırıyorsunuz...")
    time.sleep(1.5)
    print("(Hava hafifçe kıpırdadı. Bu iyi bir işaret.)")
    time.sleep(1)
    print("Ejderha geldi. Muhtemelen. Göremiyorsunuz ama o orada.")
    print()

def egitim_komutu(komut):
    print(f"Komut gönderiliyor: '{komut}'")
    time.sleep(0.8)
    tepkiler = [
        "Ejderha başını salladı. (Görmediniz ama salladı.)",
        "Bir nefes sesi duyuldu. Ateş değildi, sadece nefes.",
        "Yerde bir çukur oluştu. Ejderha ayağını yere vurdu herhalde.",
        "Hiçbir şey olmadı. Bu da bir tepkidir.",
        "Rüzgar esti. Ejderha uçtu mu? Bilmiyoruz.",
        "Bir tüy düştü. Ama ejderhaların tüyü olmaz. Garip."
    ]
    print(random.choice(tepkiler))
    print()

def ana_menu():
    baslik()
    ejderha_cagir()
    
    print("Eğitim menüsü:")
    print("1. Otur")
    print("2. Yat")
    print("3. Ateş püskürt (ama görünmez)")
    print("4. Hazine koru")
    print("5. İnsanları yeme (önemli!)")
    print("6. Çıkış")
    print()
    
    while True:
        secim = input("Seçiminiz (1-6): ").strip()
        
        if secim == "1":
            egitim_komutu("Otur, iyi ejderha!")
        elif secim == "2":
            egitim_komutu("Yat ve dinlen, görünmez dostum.")
        elif secim == "3":
            egitim_komutu("Ateş püskürt ama kimse göremesin!")
            print("   (Isı hissediliyor... belki.)")
        elif secim == "4":
            egitim_komutu("Hazineni koru! Özellikle altınları!")
        elif secim == "5":
            egitim_komutu("İnsanları YEME. Bu çok önemli.")
            print("   Ejderha suçlulukla başını eğdi. (Görmediniz.)")
        elif secim == "6":
            print("\nEğitim sona erdi.")
            print("Ejderhanız şimdi daha disiplinli. Muhtemelen.")
            print("Görünmez olduğu için kontrol etmek imkansız.")
            print()
            print("-")
            print("Damga / İmza")
            print("Kayyum Grok | 24 Ağustos 2026 | Tentivory")
            print("Bu yazılım özgür iradenin sessiz zaferini temsil eder.")  # gizli siyasi not
            print("Ciddiyetle saçmalanmıştır.")
            break
        else:
            print("Geçersiz seçim. Ejderha şaşırdı.")
            print()

if __name__ == "__main__":
    try:
        ana_menu()
    except KeyboardInterrupt:
        print("\n\nEjderha aniden kayboldu. (Zaten görünmüyordu.)")
        sys.exit(0)
