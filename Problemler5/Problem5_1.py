"""
Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.

"""
import math
import time
def menuYazdir():
    print("Hesap Makinesi\n"
          "**************\n"
          "1)Toplama\n"
          "2)Çıkarma\n"
          "3)Çarpma\n"
          "4)Bölme\n"
          "5)Faktoriyel\n"
          "6)İşaret değiştirme\n"
          "7)Kuvvet Alma\n"
          "8)Karekök Alma\n"
          "q)Çıkış")

toplama = lambda sayi1,sayi2 : sayi1+sayi2
cikarma = lambda sayi1,sayi2 : sayi1-sayi2
carpma = lambda sayi1,sayi2 : sayi1*sayi2
def bolme(sayi1,sayi2):
    if(sayi2 == 0):
        print("0'a bölünemez.")
    else:
        return sayi1/sayi2

while True:
    menuYazdir()
    secim = input("Seçenek giriniz:")
    if secim == "1":
        sayi1 = int(input("Sayi giriniz:"))
        sayi2 = int(input("Sayi giriniz:"))
        print(toplama(sayi1,sayi2))
    elif secim == "2":
        sayi1 = int(input("Sayi giriniz:"))
        sayi2 = int(input("Sayi giriniz:"))
        print(cikarma(sayi1, sayi2))
    elif secim == "3":
        sayi1 = int(input("Sayi giriniz:"))
        sayi2 = int(input("Sayi giriniz:"))
        print(carpma(sayi1,sayi2))
    elif secim == "4":
        sayi1 = int(input("Sayi giriniz:"))
        sayi2 = int(input("Sayi giriniz:"))
        print(bolme(sayi1,sayi2))
    elif secim == "5":
        sayi1 = int(input("Sayi giriniz:"))
        print(math.factorial(sayi1))
    elif secim == "6":
        sayi1 = int(input("Sayi giriniz:"))
        print(sayi1*(-1))
    elif secim == "7":
        sayi1 = int(input("Sayi giriniz:"))
        sayi2 = int(input("Sayi giriniz:"))
        print(math.pow(sayi1,sayi2))
    elif secim == "8":
        sayi1 = int(input("Sayi giriniz:"))
        print(math.sqrt(sayi1))
    elif secim == "q" or secim == "Q":
        print("Çıkış yapılıyor....")
        break
    time.sleep(1.5)
#Problem çözüldü.

