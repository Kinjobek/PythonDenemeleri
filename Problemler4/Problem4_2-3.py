"""Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.
Problem için şu siteye bakabilirsiniz;
http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok
"""
sayi1 = int(input("1. sayı : "))
sayi2 = int(input("2. sayı : "))

def asalSayilar():
    aslSylr = [2]
    for i in range(2, max(sayi1,sayi2)+1):
        kacTaneBolundu = 0
        sayi = 2
        devamlilik = True
        while devamlilik:
            if i % sayi == 0:
                kacTaneBolundu +=1
            sayi+=1
            if sayi >= i:
                devamlilik = False
        if kacTaneBolundu<=0:
            aslSylr.append(i)
        kacTaneBolundu = 0
        sayi = 2
    return aslSylr

def asalCarpanlar(sayi):
    sayininAsalBolenleri = [1]
    kalan = sayi
    for k in asalSayilar():
        devamlilik = True
        while devamlilik:
            if kalan % k == 0:
                kalan = kalan/k
                sayininAsalBolenleri.append(k)
            else:
                devamlilik = False
            if kalan == 0:
                devamlilik = False
    return sayininAsalBolenleri
def ebob(sayi1,sayi2):
    carpim = 1
    ortakAsalCarpanlar = [1]
    for k in asalSayilar():
        if asalCarpanlar(sayi1).count(k) >= asalCarpanlar(sayi2).count(k):
            carpim = carpim*k**asalCarpanlar(sayi2).count(k)
            if "0" != str(k * asalCarpanlar(sayi2).count(k)):
                for m in range(asalCarpanlar(sayi2).count(k)):
                    ortakAsalCarpanlar.append(str(k))
        else:
            carpim = carpim*k**asalCarpanlar(sayi1).count(k)
            if "0" != str(k * asalCarpanlar(sayi1).count(k)):
                for m in range(asalCarpanlar(sayi1).count(k)):
                    ortakAsalCarpanlar.append(str(k))
    if carpim != 1:
        print(sayi1,"ve ",sayi2,"sayılarının ebob için ortak çarpanları :",end = "")
        print(*ortakAsalCarpanlar,sep="x")
        print("EBOB :",carpim)
    else:
        print(sayi1, "ve ", sayi2, "sayılarının ortak çarpanları : 1")
        print("EBOB : 1")


def ekok(sayi1, sayi2):
    carpim = 1
    ortakAsalCarpanlar = [1]
    for k in asalSayilar():
        if asalCarpanlar(sayi1).count(k) <= asalCarpanlar(sayi2).count(k):
            carpim = carpim * k ** asalCarpanlar(sayi2).count(k)
            if "0" != str(k * asalCarpanlar(sayi2).count(k)):
                for m in range(asalCarpanlar(sayi2).count(k)):
                    ortakAsalCarpanlar.append(str(k))
        else:
            carpim = carpim * k ** asalCarpanlar(sayi1).count(k)
            if "0" != str(k * asalCarpanlar(sayi1).count(k)):
                for m in range(asalCarpanlar(sayi1).count(k)):
                    ortakAsalCarpanlar.append(str(k))

    print(sayi1, "ve ", sayi2, "sayılarının ekok için çarpanları :", end="")
    print(*ortakAsalCarpanlar, sep="x")
    print("EKOK :", carpim)


print("\n         Asal Sayilar\n","*******************************")
print(max(sayi1,sayi2),"sayısana kadar olan asal sayilar :",*asalSayilar())
print("{} sayısının çarpanları :".format(sayi1),end = "")
print(*asalCarpanlar(sayi1),sep="x")
print("{} sayısının çarpanları :".format(sayi2),end = "")
print(*asalCarpanlar(sayi2),sep="x")

ebob(sayi1,sayi2)
ekok(sayi1,sayi2)
#Problem çözüldü.
"""
def tamBolenler(sayi):
    sayiListesi = range(1,sayi+1)
    tBlnlr = list()
    for x in sayiListesi:
        if sayi % x == 0:
           tBlnlr.append(x)
    return tBlnlr
"""

"""
print("         Tam Bolenler\n","*******************************")
print(sayi1,"sayısının tam bolenleri :",*tamBolenler(sayi1))
print(sayi2,"sayısının tam bolenleri :",*tamBolenler(sayi2))
"""