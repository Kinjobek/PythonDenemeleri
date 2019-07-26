"""
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
"""
print("****************************\n"
      "      Çarpım Tablosu\n"
      "****************************")
sayilar=range(1,11)

for x in sayilar:
    for y in sayilar:
        print(x,"x",y,"=",x*y)
    print("****************************")
#Problem çözüldü.