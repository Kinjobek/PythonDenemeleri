from kütüphane import *

print("""*********************************
Kütüphane Programına Hoşgeldiniz.

İşlemler;
1. Kitapları Göster
2. Kitap Sorgulama
3. Kitap Ekle
4. Kitap Sil
5. Baskı Yükselt
Çıkmak için 'q'ya basın.
*********************************
""")
ktphane = Kütüphane()

while True:
    islem = input("Yapıcağınız işlemi giriniz:")
    if islem == "q":
        print("Program sonlandırılıyor")
        ktphane.baglantiyi_kes()
        break
    elif islem == "1":
        ktphane.kitapları_goster()
    elif islem == "2":
        isim = input("Hangi kitabı istiyorsunuz?")
        print("Kitap sorgulanıyor...")
        time.sleep(1)
        ktphane.kitap_sorgula(isim)
    elif islem == "3":
        isim = input("İsim : ")
        yazar = input("Yazar : ")
        yayınevi = input("Yayınevi : ")
        tür = input("Tür : ")
        baskı = int(input("Baskı : "))

        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        print("Kitap ekleniyor...")
        time.sleep(1)
        ktphane.kitap_ekle(yeni_kitap)
    elif islem == "4":
        isim = input("Kitap ismi : ")
        print("Kitap siliniyor...")
        cevap = input("Emin misiniz? (E/H)")
        if cevap.upper() == 'E':
            time.sleep(1)
            ktphane.kitap_sil(isim)
            print("Kitap silindi.")
    elif islem == "5":
        isim = input("Kitap ismi : ")
        print("Baskı yükseltiliyor")
        time.sleep(1)
        ktphane.baskı_yukselt(isim)
    else:
        print("Geçersiz işlem....")