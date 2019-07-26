"""
Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan
sadece çift sayıları bir listeye atmayı yapmayı çalışın.

Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur.
Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.

İpucu: Basit düşünmeye çalışın.
"""
print("*******************************\n"
      "100'e kadar olan çift sayılar\n"
      "******************************")
sayilar = range(1,101)
ciftSayilar = [x for x in sayilar if x % 2 == 0]
print(ciftSayilar)
#Problem çözüldü