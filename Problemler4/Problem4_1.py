"""
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını
 dönen bir tane fonksiyon yazın.
Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
"""
def tamSayiBolenleriBul():
    sayi = range(1,10001)
    tumSayilar = range(1,10001)
    tamSayıBolenleri = list()
    toplam = 0
    for x in sayi:
        for y in tumSayilar:
            if x > y:
                if x % y == 0:
                    tamSayıBolenleri.append(y)
            elif x == y:
                for k in tamSayıBolenleri:
                    toplam += k
                if x == toplam:
                    print(x," bir mükemmel sayıdır.")
        tamSayıBolenleri.clear()
        toplam = 0
tamSayiBolenleriBul()
#Problem çözüldü.