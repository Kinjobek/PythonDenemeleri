"""
Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
"""
isim = input("İsim : ")
soyisim = input("Soyisim : ")
telefonNumarası = input("Tel No : ")
print("Print içerisinde ',' koyarak sırasıyla yazdırmak")
print("İsim : ",isim,"\nSoyisim : ",soyisim,"\nTelefon Numarası : ",telefonNumarası)
#veya
print("Print içerisinde formatlama ve sep=""\\n"" ile yazdırmak ")
print("İsim : {}".format(isim),"Soyisim : {}".format(soyisim),"Telefon Numarası : {}".format(telefonNumarası),sep="\n")

#Problem Çözüldü.