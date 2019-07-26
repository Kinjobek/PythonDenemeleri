"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu
bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu
bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz.
Kullanımı şu şekildedir ;

abs(-4)
4
"""
print("**********************************\n"
      "    Geometrik Şekil Hesaplama\n"
      "**********************************\n"
      "1) Dörtgen için 1 yazınız.\n"
      "2) Üçgen için 2 yazınız.\n"
      "**********************************")
kenar1 = None
kenar2 = None
kenar3 = None
kenar4 = None
while True:
    secenek = input("Seçeneğinizi giriniz.")
    if secenek == "1":
        print("Dörtgen Seçtiniz.\n        Dörtgen Hesaplama\n**********************************\n")
        kenar1 = int(input("1.Kenarı giriniz"))
        kenar2 = int(input("2.Kenarı giriniz"))
        kenar3 = int(input("3.Kenarı giriniz"))
        kenar4 = int(input("4.Kenarı giriniz"))
        if kenar1 == kenar2 == kenar3 == kenar4:
            print("Dörtgeniniz bir kare.")
        elif kenar1 == kenar2 and kenar3 == kenar4:
            print("Dörtgeniniz bir dikdörtgen.")
        elif kenar2 == kenar3 and kenar1 == kenar4:
            print("Dörtgeniniz bir dikdörtgen.")
        else:
            print("Dörtgeniniz sıradan bir dörtgen.")
        break;
    elif secenek == "2":
        print("Üçgen seçtiniz.\n          Üçgen Hesaplama\n**********************************")
        kenar1 = int(input("1.Kenarı giriniz"))
        kenar2 = int(input("2.Kenarı giriniz"))
        kenar3 = int(input("3.Kenarı giriniz"))
        if abs(kenar1+kenar2) > kenar3 and abs(kenar1+kenar3) > kenar2 and abs(kenar2+kenar3) > kenar1:
            if kenar1 == kenar2 and kenar1 == kenar3:
                print("Üçgenininz bir eşkenar üçgen.")
            elif ((kenar1 == kenar2 and kenar1 != kenar3) or (kenar1 == kenar3 and kenar1 != kenar2) or (kenar3 == kenar2 and kenar3 != kenar1)):
                print("Üçgeniniz bir ikizkenar üçgen.")
            else:
                print("Üçgeniniz bir çeşitkenar üçgen.")
        else:
            print("Üçgen değil.")
        break;
    else:
        print("Böyle bir seçenek bulunmamakta.\nTekrar giriniz.")
print("Program sonlandırıldı.")
#Problem çözüldü.