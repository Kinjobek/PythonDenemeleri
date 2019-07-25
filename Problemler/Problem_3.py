"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""
print("Yakıt tüketimi hesaplama")

aracAdi = "Skoda"
model = "Octavia 1.6 TDI"
tüketilenYakit = float(input("100 kilometrede kaç litre tüketiyor"))
yakıtFiyatı = float(input("Kayıt fiyatı kaç türk lirasıdır?"))
kilometreBasinaTL = tüketilenYakit/100*yakıtFiyatı
gidilecekMesafe = float(input("Kaç kilometre gideceksiniz?"))
toplamTutar = gidilecekMesafe*kilometreBasinaTL

print("Araç adı : {} {}".format(aracAdi,model),
      "100km'de tüketilen yakıt : {} L/100km".format(tüketilenYakit),
      "Yakıt Fiyatı : {}".format(yakıtFiyatı),
      "Kilometre Başına : {} TL".format("{:.2f}".format(kilometreBasinaTL)),
      "Gidilecek Mesafe : {} m".format(gidilecekMesafe),
      "Toplam Tutar {} TL".format("{:.2f}".format(toplamTutar)),sep="\n")

#Problem Çözüldü