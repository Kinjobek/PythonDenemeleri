"""
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın.
 Bu işlemi continue ile yapmaya çalışın.
"""
print("*******************************\n"
      "100'e kadar 3'e bölünen sayılar\n"
      "*******************************")
sayilar = range(1 , 101)
uceBolunenler = list()
for x in sayilar:
    if x % 3 == 0:
        uceBolunenler.append(x)
print(uceBolunenler)
#Problem çözüldü.