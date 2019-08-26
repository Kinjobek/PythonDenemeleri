"""Problem 1
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.

İpucu : Kodlama egzersizimizde buna çok benzer bir şey yapmıştık."""

class Dosya():
    def dosyadakiKelimleriAyir(self,dosyaAdi):
        with open(dosyaAdi,"r",encoding="utf-8") as file:
            kelimeler = file.read().split()
            self.yalinKelimeler = list()
            for kelime in kelimeler:
                kelime = kelime.lower()
                kelime = kelime.strip()
                kelime = kelime.strip(".")
                kelime = kelime.strip("\n")
                self.yalinKelimeler.append(kelime)
    def kelimeleriNumaraliYazdir(self):
        k = 1
        print("*******************************************************************************************")
        for i in self.yalinKelimeler:
            if k%5 == 1:
                if k == 1:
                    pass
                else:
                    print("")
            print(k,") ",i,"  ",end="")
            k+=1
        print("")
        print("*******************************************************************************************")
    def kelime_bul(self,aranan):
        konumlar = list()
        sayac = 1
        for kelime in self.yalinKelimeler:
            if kelime == aranan:
                konumlar.append(sayac)
            sayac +=1
        if len(konumlar) == 0:
            print("Dosyada böyle bir kelime bulunmuyor.")
        else:
            print("'{}' kelimesi şurada geçiyor.\n{}".format(aranan,konumlar))
    def kelimeHistagrami(self):
        kelimeFrekansi = dict()
        for kelime in self.yalinKelimeler:
            if kelime in kelimeFrekansi:
                kelimeFrekansi[kelime]+=1
            else:
                kelimeFrekansi[kelime] = 1
        print("Kelimelerin Frekansı")
        for i,j in kelimeFrekansi.items():
            print("{} kelimesi metinde {} defa geçiyor.".format(i,j))
    def harfHistagrami(self):
        harfFrekansi = dict()
        harfListesi = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
        for h in harfListesi:
            if h in harfFrekansi:
                pass
            else:
                harfFrekansi[h] = 0
        for kelime in self.yalinKelimeler:
            for harf in harfListesi:
                harfFrekansi[harf] += kelime.count(harf)
        for i, j in harfFrekansi.items():
            print("{} kelimesi metinde {} defa geçiyor.".format(i, j))

dosya = Dosya()
dosya.dosyadakiKelimleriAyir("metin.txt")
dosya.kelimeleriNumaraliYazdir()
dosya.kelime_bul("da")
dosya.kelimeHistagrami()
dosya.harfHistagrami()
#Problem çözüldü.