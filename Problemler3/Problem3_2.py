"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı
( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""
print("****************************\n"
      "       Armstrong Sayı\n"
      "****************************")
sayi = input("Sayı giriniz:")
sayiStringliste = list(sayi)
sayiIntListesi = list()
toplam = 0
for x in sayiStringliste:
    sayiIntListesi.append(int(x))
print("Hesaplanıyor.....")
for y in sayiIntListesi:
    print(y," sayısının ",len(sayiIntListesi),". kuvveti : ",y**len(sayiIntListesi),sep="")
    toplam =toplam + y**len(sayiIntListesi)
print("Toplamları {} idir.".format(toplam))
if int(sayi) == toplam:
    print(sayi,"bir armstrong sayıdır.")
else:
    print(sayi,"bir armstrong sayı değildir.")
#Problem çözüldü.