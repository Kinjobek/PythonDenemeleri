"""
Kodlama egzersizimizde bir sınıfın harf notlarını hesapladığımız programı geliştirerek kalanları "kalanlar.txt"
 dosyasında ve geçenleri "geçenler.txt" dosyasına yazmaya çalışın.
"""
kalanlar = list()
gecenler = list()
def not_hesapla(satir):
    satir = satir [:-1] #\n'i siler
    liste = satir.split(",")
    isimler = liste[0]
    vize1 = int(liste[1])
    vize2 = int(liste[2])
    final = int(liste[3])

    ortalama = int(vize1*3/10 + vize2*3/10 + final*4/10)
    gecmeDurumuHesapla(isimler,ortalama)

def gecmeDurumuHesapla(isim,ort):

    if ort >= 90:
        gecenler.append(isim + ": AA :" + str(ort) + "\n")
    elif ort >= 85:
        gecenler.append(isim + ": BA :" + str(ort) + "\n")
    elif ort >= 80:
        gecenler.append(isim + ": BB :" + str(ort) + "\n")
    elif ort >= 75:
        gecenler.append(isim + ": CB :" + str(ort) + "\n")
    elif ort >= 70:
        gecenler.append(isim + ": CC :" + str(ort) + "\n")
    elif ort >= 65:
        gecenler.append(isim + ": DC :" + str(ort) + "\n")
    elif ort >= 60:
        gecenler.append(isim + ": DD :" + str(ort) + "\n")
    elif ort >= 55:
        kalanlar.append(isim + ": FD :" + str(ort) + "\n")
    elif ort < 55:
        kalanlar.append(isim + ": FF :" + str(ort) + "\n")

with open("notlar.txt","r",encoding="utf-8") as file:
    for i in file:
        not_hesapla(i)
def gecenlerDosyasiOlustur():
    gecenler.sort()
    with open("gecenler.txt", "w", encoding="utf-8") as file:
        for i in gecenler:
            file.write(i)
def kalanlarDosyasiOlustur():
    kalanlar.sort()
    with open("kalanlar.txt","w",encoding="utf-8") as file:
        for i in kalanlar:
            file.write(i)

gecenlerDosyasiOlustur()
kalanlarDosyasiOlustur()