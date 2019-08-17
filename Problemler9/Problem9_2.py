"""
Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]

     Not: filter() fonksiyonunu kullanmaya çalışın.


"""

kenarUzunluklari = [(3,4,5),(6,8,10),(3,10,7)]
def ucgenMi(uzunluk):
    if uzunluk[0] + uzunluk[1] > uzunluk[2] and uzunluk[0] + uzunluk[2] > uzunluk[1] and uzunluk[1] +uzunluk[2] > uzunluk[0]:
        return True
    else :
        return False
print(list(filter(ucgenMi,kenarUzunluklari)))
    
#Problem çözüldü.