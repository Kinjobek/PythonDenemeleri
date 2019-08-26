""""şiir.txt" şeklinde bir dosya oluşturun.
-
Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu string'i ekrana yazdırın."""
def satirlariAl():
    with open("şiir.txt","r",encoding="utf-8") as file:
        satirlar = file.readlines()
    return satirlar
def basHarfleriAl():
    basHarfler = list()
    for i in satirlariAl():
        basHarfler.append(i[0])
    return basHarfler
def stringOlustur():
    yazi =""
    for i in basHarfleriAl():
        yazi += i
        if len(yazi) == 7:
            yazi +=" "
    print(yazi)
stringOlustur()
#Problem çözüldü.