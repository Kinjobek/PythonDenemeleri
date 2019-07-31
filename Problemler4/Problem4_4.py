"""
Kullanıcıdan 3 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 997 --------->Dokuz Yüz Doksan Yedi
"""
def sozluk():
    sayiSozlugu = {"BirlerBasamağı":  {"0": "",
                                      "1": "Bir",
                                      "2": "İki",
                                      "3": "Üç",
                                      "4": "Dört",
                                      "5": "Beş",
                                      "6": "Altı",
                                      "7": "Yedi",
                                      "8": "Sekiz",
                                      "9": "Dokuz"},
                   "OnlarBasamağı":  {"0": "",
                                       "1": "On",
                                       "2": "Yirmi",
                                       "3": "Otuz",
                                       "4": "Kırk",
                                       "5": "Elli",
                                       "6": "Altmış",
                                       "7": "Yetmiş",
                                       "8": "Seksen",
                                       "9": "Doksan", },
                   "YüzlerBasamağı":  {"0":"",
                                       "1":"Yüz",
                                       "2":"İki Yüz",
                                       "3":"Üç Yüz",
                                       "4":"Dört Yüz",
                                       "5":"Beş Yüz",
                                       "6":"Altı Yüz",
                                       "7":"Yedi Yüz",
                                       "8":"Sekiz Yüz",
                                       "9":"Dokuz Yüz"}}
    return sayiSozlugu
def okunus(yüzlerBasamağı,onlarBasamağı,birlerBasamağı):
    print(sozluk()["YüzlerBasamağı"][yüzlerBasamağı],end=" ")
    print(sozluk()["OnlarBasamağı"][onlarBasamağı],end=" ")
    print(sozluk()["BirlerBasamağı"][birlerBasamağı],end=" ")
    print("")

def kullanicininIstegi():
    print("Çıkmak için 'q' yazınız.")
    while True:
        sayi = input("Lütfen sayıyı giriniz :").replace(" ","")
        if sayi == "q":
            print("Çıkış Yaptınız.")
            break
        if len(sayi) == 3:
            if sayi[0] == "0":
                okunus("0",sayi[1],sayi[2])
            elif sayi[0] == "0" and sayi[1] == "0":
                okunus("0","0",sayi[2])
            else:
                okunus(sayi[0],sayi[1],sayi[2])
        elif len(sayi) == 2:
            if sayi[0] == "0":
                okunus("0","0",sayi[1])
            else:
                okunus("0",sayi[0],sayi[1])
        elif len(sayi) ==1:
            if sayi[0] == "0":
                print("Sıfır")
            else:
                okunus("0","0",sayi[0])
kullanicininIstegi()
#Problem Çözüldü.