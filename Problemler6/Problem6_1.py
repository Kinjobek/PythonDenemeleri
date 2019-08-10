"""
Kodlama Egzersizimizde yazdığımız Kumanda Sınıfına ek olarak metodlar ve özellikler eklemeye çalışın.
"""
import time
class Kumanda():
    sesSeviyesi = 0
    kanallar = {}
    acikKapali = False
    kanalNumarasi = "1"
    def menuYazdir(self):
        print("1 : TV Durumu\n"
              "2 : TV Aç/Kapat\n"
              "3 : Ses Seviyesi Ayarla\n"
              "4 : Kanallar\n"
              "5 : Kanal Seç\n"
              "6 : Kanal Ekle\n"
              "q : Çıkış\n"
              "b : Genel Bilgi")
    def __init__(self):
        self.sesSeviyesi = 5
        self.kanallar.update({"1":"TRT"})
        self.acikKapali = False
    def tvAcKapat(self):
        if(self.acikKapali == False):
            print("TV açılıyor...")
            self.acikKapali = True
        else:
            print("TV kapatılıyor...")
            self.acikKapali = False
    def tvDurumu(self):
        if (self.acikKapali == False):
            return "Kapalı"
        else:
            return "Açık"
    def tvDurumuYaz(self):
        print(self.tvDurumu())
    def sesSeviyesiAyarla(self):
        print("Arttırmak için '+'\n"
              "Azaltmak için '-' tuşlarına basınız.")
        if("+" == input()):
            if(self.sesSeviyesi<=10 and self.sesSeviyesi>=0):
                self.sesSeviyesi +=1
        elif("-" == input()):
            if (self.sesSeviyesi <= 10 and self.sesSeviyesi >= 0):
                self.sesSeviyesi -= 1
    def sesSeviyesiGoster(self):
        print(self.sesSeviyesi)
    def kanalEkle(self):
        kanalNumarasi = input("Kanal için numara giriniz:")
        kanalAdi = input("Kanal adı giriniz:")
        self.kanallar.update({kanalNumarasi:kanalAdi})
    def kanallariGoster(self):
        for i in self.kanallar:
            print("Kanal numarası - adı : {} -> ".format(i),self.kanallar[i])
    def kanalaGit(self):
        global kanalNumarasi
        kanalNumarasi = input("Kanal Numarası Giriniz:")
        if(int(kanalNumarasi) < len(self.kanallar.keys())+1 and int(kanalNumarasi) >= 0):
            print("Açılan kanal : ", self.kanallar[kanalNumarasi])
        else:
            print("Böyle bir kanal bulunmamakta.")
    def __str__(self):
         return "TV Durumu : "+self.tvDurumu()+"\nSes Seviyesi : "+str(self.sesSeviyesi)+"\nKanal : "+self.kanallar[kanalNumarasi]
def baslat():
    tv = Kumanda()
    while True:
        tv.menuYazdir()
        sayi = input("Seçenek Giriniz.")
        if sayi == "1":
            tv.tvDurumuYaz()
        elif sayi == "2":
            tv.tvAcKapat()
        elif sayi == "3":
            tv.sesSeviyesiAyarla()
            tv.sesSeviyesiGoster()
        elif sayi == "4":
            tv.kanallariGoster()
        elif sayi == "5":
            tv.kanalaGit()
        elif sayi == "6":
            tv.kanalEkle()
        elif sayi == "q":
            break
        elif sayi == "b":
            print(Kumanda())
        print("********************************")
baslat()

