"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""
print("*****************************\n"
      "       Mükemmel Sayı\n"
      "*****************************")
sayi = int(input("Sayı giriniz : "))
sayiListesi = range(1,sayi)
tamBölenler = list()
toplam = 0
for x in sayiListesi:
    if sayi % x == 0:
        tamBölenler.append(x)
print(tamBölenler)
for i in tamBölenler:
    toplam += i
if sayi == toplam :
    print(sayi,"bir mükemmel sayıdır.")
else :
    print(sayi ,"bir mükemmel sayı değildir.\nToplamları : {}".format(toplam))
