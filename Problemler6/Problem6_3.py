"""
Bu projede ise 4 tane sınıfı oluşturun.

Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.

Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.

At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.
"""
class Hayvan():
    ses = None
    bacakSayısı = None
    kuyrukDurumu = None
    ad = None
    def __init__(self,ses="Yok",bacakSayısı="Yok",kuyrukDurumu="Yok",ad="Yok"):
        self.ses = ses
        self.bacakSayısı = bacakSayısı
        self.kuyrukDurumu = kuyrukDurumu
        self.ad = ad
class Kopek(Hayvan):
    ekOzellik = None
    def __init__(self,ses,bacakSayısı,kuyrukDurumu,ad,ekOzellik="Daha yok"):
        print("Köpek")
        super().__init__(ses,bacakSayısı,kuyrukDurumu,ad)
        self.ekOzellik = ekOzellik
    def ekOzellikGir(self):
        ekOz = "Isırır"
        self.ekOzellik = ekOz
        return self.ekOzellik
    def yakalamaca(self):
        print("Yakalamaca oyunu oynanabilir.")
    def bilgiler(self):
        print("Ad:",self.ad,"\nBacak sayısı:",self.bacakSayısı,"\nKuyruk durumu:",self.kuyrukDurumu,"\nSes:",self.ses,"\nEk ozellik:",self.ekOzellikGir())
class Kus(Hayvan):
    ekOzellik = None
    def __init__(self,ses,bacakSayısı,kuyrukDurumu,ad,ekOzellik="Daha yok"):
        print("Kuş")
        super().__init__(ses,bacakSayısı,kuyrukDurumu,ad)
        self.ekOzellik = ekOzellik
    def ekOzellikGir(self):
        ekOz = "Uçar"
        self.ekOzellik = ekOz
        return self.ekOzellik
    def konusma(self):
        print("Konuşma öğretilebilir.")
    def bilgiler(self):
        print("Ad:",self.ad,"\nBacak sayısı:",self.bacakSayısı,"\nKuyruk durumu:",self.kuyrukDurumu,"\nSes:",self.ses,"\nEk ozellik:",self.ekOzellikGir())
class At(Hayvan):
    ekOzellik = None
    def __init__(self,ses,bacakSayısı,kuyrukDurumu,ad,ekOzellik="Daha yok"):
        print("At")
        super().__init__(ses,bacakSayısı,kuyrukDurumu,ad)
        self.ekOzellik = ekOzellik
    def ekOzellikGir(self):
        ekOz = "Koşar"
        self.ekOzellik = ekOz
        return self.ekOzellik
    def binme(self):
        print("Binilebilir.")
    def bilgiler(self):
        print("Ad:",self.ad,"\nBacak sayısı:",self.bacakSayısı,"\nKuyruk durumu:",self.kuyrukDurumu,"\nSes:",self.ses,"\nEk ozellik:",self.ekOzellikGir())
print("************************************")
h2 = Kopek("Havhav",4,"Kuyruk var","Kopek")
h2.bilgiler()
h2.yakalamaca()
print("************************************")
h3 = Kus("Cikcik",2,"Kuyruk var","Kuş")
h3.bilgiler()
h3.konusma()
print("************************************")
h4 = At("İhiahaha",4,"Kuyruk var","At")
h4.bilgiler()
h4.binme()
print("************************************")
#Problem çözüldü.