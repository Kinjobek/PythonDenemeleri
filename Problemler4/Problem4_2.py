"""Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok
"""
sayi1 = int(input("1. sayı : "))
sayi2 = int(input("2. sayı : "))

def tamBolenler(sayi):
    sayiListesi = range(1,sayi+1)
    tBlnlr = list()
    for x in sayiListesi:
        if sayi % x == 0:
           tBlnlr.append(x)
    return tBlnlr

def ortakBolenler():
    ortkBlnlr = list()
    for x in tamBolenler(sayi1):
        for y in tamBolenler(sayi2):
            if x == y:
                ortkBlnlr.append(x)
    return ortkBlnlr

def ebob():
    print("En Buyuk Ortak Boleni(EBOB):", max(ortakBolenler()))

print(sayi1,"sayısının tam bolenleri :",tamBolenler(sayi1))
print(sayi2,"sayısının tam bolenleri :",tamBolenler(sayi2))

print("Ortak bolenleri :",ortakBolenler())

#Problem çözüldü.