"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

Vize1 toplam notun %30'una etki edecek.

Vize2 toplam notun %30'una etki edecek.

Final toplam notun %40'ına etki edecek.


Toplam Not >=  90 -----> AA

Toplam Not >=  85 -----> BA

Toplam Not >=  80 -----> BB

Toplam Not >=  75 -----> CB

Toplam Not >=  70 -----> CC

Toplam Not >=  65 -----> DC

Toplam Not >=  60 -----> DD

Toplam Not >=  55 -----> FD

Toplam Not <  55 -----> FF
"""
print("********************************\n"
      "      Harf Notu Hesaplama\n"
      "********************************")
vize1 = int(input("1. Vize:"))
vize2 = int(input("2. Vize:"))
final = int(input("Final  :"))
toplamNot = int((vize1 * 30 / 100) + (vize2 * 30 / 100) + (final * 40 / 100))

print("Toplam notunuz : ", toplamNot)
if toplamNot >= 90:
    print("AA")
elif toplamNot >= 85:
    print("BA")
elif toplamNot >= 80:
    print("BB")
elif toplamNot >= 75:
    print("CB")
elif toplamNot >= 70:
    print("CC")
elif toplamNot >= 65:
    print("DC")
elif toplamNot >= 60:
    print("DD")
elif toplamNot >= 55:
    print("FD")
elif toplamNot < 55:
    print("FF")
# Problem Çözüldü.
