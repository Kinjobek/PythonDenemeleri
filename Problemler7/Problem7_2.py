"""
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün.
Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın. Daha sonra, içinde çift ve tek sayılar bulunduran bir liste
tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.
"""
def ciftMiDegilMi(sayi):
    if sayi % 2 == 0:
        return sayi
    else:
        raise ValueError

sayıListesi = range(1,26)
ciftSayilar = list()
for i in sayıListesi:
    try:
        print(ciftMiDegilMi(i))
        ciftSayilar.append(i)
    except ValueError:
        print("Hata, tek sayı : ",i)
print("Çift Sayılar 1-25 : ",*ciftSayilar)
#Problem Çözüldü.