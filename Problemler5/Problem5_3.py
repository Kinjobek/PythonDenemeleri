"""
Random ve Time modüllerini kullanarak sayı tahmin oyunu yazınız.
"""
import random
import time

print("     Sayı Tahmin Oyunu\n"
      "****************************")
rastgeleSayi = random.randint(1,100)
tahminHakki = 10
while True:
    tahminEdilenSayi = int(input("Tahmininiz."))
    if tahminEdilenSayi > rastgeleSayi:
        print("Asıl sayı daha küçük")
        tahminHakki -= 1
    elif tahminEdilenSayi < rastgeleSayi:
        print("Asıl sayı daha büyük")
        tahminHakki -= 1
    elif tahminHakki == 0:
        print("Kaybettiniz. Asıl sayı {} idi.".format(rastgeleSayi))
        break
    else:
        print("Tebrikler! Sayıyı({}) buldunuz.\nBulunan adım sayısı:{}".format(rastgeleSayi,11-tahminHakki))
        break
#problem çözüldü.