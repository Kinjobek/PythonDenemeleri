"""
"futbolcular.txt" şeklinde bir dosya oluşturun ve içine Galatasaray,Fenerbahçe ve Beşiktaşta oynayan futbolcuları rastgele yerleştirin.
Bu dosyadan herbir takımın futbolcularını ayırarak "gs.txt" , "fb.txt", "bjk.txt" şeklinde 3 farklı dosyaya yazın.

"futbolcular.txt" dosyasının başlangıç hali şu şekilde olsun.

                Fernando Muslera,Galatasaray
                Atiba Hutchinson,Beşiktaş
                Simon Kjaer,Fenerbahçe
                           //
                           //
                           //
                           //
                           //
"""
def fenerbahceOyuncular():
    fenerbahce = list()
    fenerbahce.append("Altay Bayındır,Fenerbahçe\n")
    fenerbahce.append("Mauricio Isla,Fenerbahçe\n")
    fenerbahce.append("Zanka,Fenerbahçe\n")
    fenerbahce.append("Sadık Çiftpınar,Fenerbahçe\n")
    fenerbahce.append("Nabil Dirar,Fenerbahçe\n")
    fenerbahce.append("Ozan Tufan,Fenerbahçe\n")
    fenerbahce.append("Emre Belözoğlu,Fenerbahçe\n")
    fenerbahce.append("Ferdi Kadıoğlu,Fenerbahçe\n")
    fenerbahce.append("Max Kruse,Fenerbahçe\n")
    fenerbahce.append("Garry Rodrigues,Fenerbahçe\n")
    fenerbahce.append("Vedat Muriqi,Fenerbahçe\n")
    return fenerbahce
def galatasarayOyuncular():
    galatasaray = list()
    galatasaray.append("Muslera,Galatasaray\n")
    galatasaray.append("Mariano,Galatasaray\n")
    galatasaray.append("Ozornwafor,Galatasaray\n")
    galatasaray.append("Luyindama,Galatasaray\n")
    galatasaray.append("Nagatomo,Galatasaray\n")
    galatasaray.append("Ryan Donk,Galatasaray\n")
    galatasaray.append("Steven Nzonzi,Galatasaray\n")
    galatasaray.append("Jimmy Durmaz,Galatasaray\n")
    galatasaray.append("Belhanda,Galatasaray\n")
    galatasaray.append("Babel,Galatasaray\n")
    galatasaray.append("Radamel Falcao,,Galatasaray\n")
    return galatasaray
def besiktasOyuncular():
    besiktas = list()
    besiktas.append("Karius,Beşiktaş\n")
    besiktas.append("Douglas,Beşiktaş\n")
    besiktas.append("Domagoj Vida,Beşiktaş\n")
    besiktas.append("Victor Ruiz,Beşiktaş\n")
    besiktas.append("Pedro Rebocho,Beşiktaş\n")
    besiktas.append("Quaresma,Beşiktaş\n")
    besiktas.append("Dorukhan,Beşiktaş\n")
    besiktas.append("Adem Ljajic,Beşiktaş\n")
    besiktas.append("Jeremain Lens,Beşiktaş\n")
    besiktas.append("Burak Yılmaz,Beşiktaş\n")
    besiktas.append("Tyler Boyd,Beşiktaş\n")
    return besiktas
def futbolcularListesiOlustur():
    futbolcularListesi = fenerbahceOyuncular() + galatasarayOyuncular() + besiktasOyuncular()
    futbolcularListesi.sort()
    return futbolcularListesi
futbolcularListesi = futbolcularListesiOlustur()
def futbolcularOlustur():
    with open("futbolcular.txt","w",encoding="utf-8") as file:
        for i in futbolcularListesi:
            file.write(i)
futbolcularOlustur()
fbList = list()
gsList = list()
bjkList = list()
def fbTakimi(oy,ta):
    fbList.append(oy + ":" + ta + "\n")
def gsTakimi(oy,ta):
    gsList.append(oy + ":" + ta + "\n")
def bjkTakimi(oy,ta):
    bjkList.append(oy + ":" + ta + "\n")
def futbolcuyuTani(satir):
    satir = satir [:-1]
    liste = satir.split(",")
    oyuncu = liste[0]
    takim = liste[1]
    takimAyarla(oyuncu,takim)
def takimAyarla(oy,ta):
    if ta == "Fenerbahçe":
        fbTakimi(oy,ta)
    elif ta == "Galatasaray":
        gsTakimi(oy,ta)
    elif ta == "Beşiktaş":
        bjkTakimi(oy,ta)

with open("futbolcular.txt","r",encoding="utf-8") as file:
    for i in file:
        futbolcuyuTani(i)
def fbtxtOlustur():
    fbList.sort()
    with open("fb.txt","w",encoding="utf-8") as file:
        for i in fbList:
            file.write(i)
def gstxtOlustur():
    gsList.sort()
    with open("gs.txt","w",encoding="utf-8") as file:
        for i in gsList:
            file.write(i)
def bjktxtOlustur():
    bjkList.sort()
    with open("bjk.txt","w",encoding="utf-8") as file:
        for i in bjkList:
            file.write(i)

fbtxtOlustur()
gstxtOlustur()
bjktxtOlustur()
#Problem Çözüldü.