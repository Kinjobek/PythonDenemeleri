"""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin.

Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.
"""
print("**********************************\n"
      "     Dur Diyene Kadar Topla\n"
      "**********************************\n"
      "               Menü\n"
      "Çıkış için 'q' yazınız.\n"
      "**********************************")
girilenSayilar = list()
toplam = 0
while True:
    girilenDeger = input("Sayı giriniz :")

    if(girilenDeger == "q"):
        print("Toplam : {}".format(toplam))
        print("Sayılar : ",*girilenSayilar)
        break
    elif girilenDeger.isnumeric():
        girilenSayilar.append(int(girilenDeger))
        toplam += int(girilenDeger)
    else:
        print("Hatalı değer girdiniz.")

#Problem çözüldü.

