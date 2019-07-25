"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""
'Beden Kitle İndeksi\n-------------------'
boy = int(input("Boy giriniz(cm örn:176) :"))
kilo = int(input("Kilo giriniz(kg örn:63) :"))

"hesaplanıyor...."
bki = kilo/(boy/100)**2
bki = "{:.2f}".format(bki)

print("Beden kitle indeksiniz : ",bki)

#Problem çözüldü.