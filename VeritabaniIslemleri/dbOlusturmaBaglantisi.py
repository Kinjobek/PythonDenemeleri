import sqlite3
con = sqlite3.connect("kütüphane.db") #yoksa oluşturup bağlanır.varsa direk bağlanır

cursor = con.cursor() #imleç oluştu ve tüm db işlemlerini buradan gerçekleştiririz.
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()

tablo_olustur()
def veri_ekle():
    cursor.execute("INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest Yayıncılık',561)")
    con.commit()
def kullanci_verileri(isim,yazar,yayınEvi,sayfaSayısı):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınEvi,sayfaSayısı))
    con.commit()
def kullanici_veri_ekle():
    isim  = input("İsim:")
    yazar = input("Yazar:")
    yayınEvi = input("Yayınevi:")
    sayfaSayısı = int(input("Sayfa Sayısı:"))
    kullanci_verileri(isim,yazar,yayınEvi,sayfaSayısı)
#kullanici_veri_ekle()
def verileri_al():
    cursor.execute("SELECT * FROM kitaplık")
    liste = cursor.fetchall()
    #con.commit() yapmıyoruz çünkü veritabanında güncelleme yapmıyoruz.
    print("Kitaplık tablosunun bilgileri....")
    for i in liste:
        print(i)
#verileri_al()
def verilerin_bazılarını_al():
    cursor.execute("SELECT İsim,Yazar FROM kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun isim ve yazar özellikleri")
    for i,j in liste:
        print("İsim : {} , Yazar : {} ".format(i,j))
#verilerin_bazılarını_al()
def verilerin_belli_olanlarını_al(yayınevi):
    cursor.execute("SELECT * FROM kitaplık where Yayınevi = ?",(yayınevi,))
    liste = cursor.fetchall()
    for i in liste:
        print("Yayınevi : ",i)
#verilerin_belli_olanlarını_al("Can Roman")
def verileri_guncelle(eski_yayınevi,yeni_yayınevi):
    cursor.execute("UPDATE kitaplık set Yayınevi = ? where Yayınevi = ?",(yeni_yayınevi,eski_yayınevi))
    con.commit()
def verileri_guncelleme_islemi():
    verileri_al()
    eskiyayınevi = input("Değişecek olanı yazınız.")
    yeniyayınevi = input("Ne olarak degişecek")
    verileri_guncelle(eskiyayınevi,yeniyayınevi)
    verileri_al()
#verileri_guncelleme_islemi()
def verileri_silme(yazar):
    cursor.execute("DELETE FROM kitaplık where Yazar = ?",(yazar,))
    con.commit()
def verileri_silme_islemi():
    verileri_al()
    yazar = input("Yazar : ")
    verileri_silme(yazar)
    verileri_al()
#verileri_silme_islemi()
con.close() # iş bitti buradan yaparız


