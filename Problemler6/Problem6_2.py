"""
Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.

Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.
"""
import time
class Bilgisayar():
    konum = None
    dosyalar = {}
    durum = None
    def __init__(self):
        self.konum = "Masaüstü"
        self.dosyalar ={"Masaüstü":{"1":"Bilgisayarım","2":"Çöp Kutusu","3":"Belgeler","4":"Google Chrome"},
                        "Bilgisayarım":{"1":"Yerel Disk C","2":"Yerel Disk D","3":"Belgeler",},
                        "Belgeler":{"1":"Resimler","2":"Müzikler","3":"Videolar","4":"İndirmeler"}}
        self.durum = "Kapalı"
    def menuYazdir(self):
        if self.bilgisayarDurum() == "Kapalı":
            print("1) Bilgisayarı aç\n"
                  "q) Programı kapat")
        elif self.bilgisayarDurum() == "Açık":
            print("1) Masaüstü göster\n"
                  "2) Bilgisayarım göster\n"
                  "3) Belgeler göster\n"
                  "4) Konumu göster\n"
                  "5) \n"
                  "6) \n"
                  "7) \n"
                  "q) ")
    def bilgisayarAcKapat(self):
        if self.durum == "Kapalı":
            i=0
            while i <= 15:
                print(".",end="")
                i+=1
                time.sleep(0.10)
            print("\nMebon'a Hoşgeldiniz :)")
            self.durum = "Açık"
        elif self.durum == "Açık":
            i = 0
            print("Kapatılıyor :(")
            while i <= 15:
                print(".", end="")
                i += 1
                time.sleep(0.30)
            self.durum = "Kapalı"
            print("")
    print("******************************")
    def bilgisayarDurum(self):
        return self.durum
    def masaüstüDosyalarıGoster(self):
        for i in self.dosyalar["Masaüstü"]:
            print(i,")",self.dosyalar["Masaüstü"][str(i)])
            time.sleep(0.5)
        print("******************************")
    def bilgisayarımDosyalarıGoster(self):
        for i in self.dosyalar["Bilgisayarım"]:
            print(i,")",self.dosyalar["Bilgisayarım"][str(i)])
            time.sleep(0.5)
        print("******************************")
    def belgelerDosyalarıGoster(self):
        for i in self.dosyalar["Belgeler"]:
            print(i,")",self.dosyalar["Belgeler"][str(i)])
            time.sleep(0.5)
        print("******************************")
    def konumuGoster(self):
        time.sleep(0.5)
        print("Konum : ",self.konum)
        time.sleep(0.5)
        print("Konumda bulunanlar : ",*self.dosyalar[self.konum].items())
        time.sleep(0.5)
        print("******************************")
    def __str__(self):
        return self.konum

def baslatPC():
    pc = Bilgisayar()
    while True:
        pc.menuYazdir()
        secenek = input("Seçenek giriniz : ")
        if secenek == "1":
            pc.bilgisayarAcKapat()
            while True:
                pc.menuYazdir()
                secenek = input("Seçenek giriniz : ")
                if secenek == "1":
                    pc.masaüstüDosyalarıGoster()
                elif secenek == "2":
                    pc.bilgisayarımDosyalarıGoster()
                elif secenek == "3":
                    pc.belgelerDosyalarıGoster()
                elif secenek == "4":
                    pc.konumuGoster()
                elif secenek == "q":
                    pc.bilgisayarAcKapat()
                    break
        elif secenek != "1" and secenek != "q":
            print("PC kapalı xD\n")
        elif secenek == "q":
            break
baslatPC()