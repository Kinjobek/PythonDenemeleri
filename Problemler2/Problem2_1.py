"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

Beden Kitle İndeksi: Kilo / Boy(m) * Boy(m)

BKİ 18.5'un altındaysa -------> Zayıf

BKİ 18.5 ile 25 arasındaysa ------> Normal

BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

BKİ 30'un üstündeyse -------------> Obez
"""
print("***************************\n"
      "    Beden Kitle İndeksi\n"
      "***************************")
boy = int(input("Lütfen boy(cm) giriniz(örneğin 172):"))
kilo = int(input("Lütfen kilo(kg) giriniz(örneğin 70):"))
print("Hesaplanıyor.....")
bki =float("{:.2f}".format(kilo/((boy/100)**2)))
print("Beden kitle indeksiniz :{}".format(bki))
if bki<18.5 :
    print("Zayıfsın. Dengeli beslenerek ve düzgün spor yaparak kilonu arttırmalısın.")
elif bki>18.5 and bki<25 :
    print("Gayet normalsin. Yediklerini abartma ve düzenli yürüyüş, spor ile kilonu koru.")
elif bki>25 and bki<30 :
    print("Şişkosun. Yemeyi içmeyi kes ve hemen kalkıp yürümeye başla.")
elif bki>30:
    print("Obezsin. Acilen bir doktora görünmelisin.")

#Problem çözüldü