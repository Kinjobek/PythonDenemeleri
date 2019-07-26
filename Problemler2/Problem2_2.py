"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""
print("Girilen 3 sayı arasından büyüğünü bulma")
sayi1 = float(input("1.Sayı : "))
sayi2 = float(input("2.Sayı : "))
sayi3 = float(input("3.Sayı : "))

if sayi1 == sayi2 or sayi1 == sayi3 or sayi2 == sayi3:
    if sayi1 == sayi2 == sayi3:
        print("Sayılar eşit.")
    elif sayi1 == sayi2:
        if sayi1 > sayi3:
            print(sayi1, "ve ", sayi2, "eşit, ", sayi3, " den büyükler")
        elif sayi1 < sayi3:
            print(sayi1, "ve ", sayi2, "eşit, ", sayi3, " den küçükler")
    elif sayi1 == sayi3:
        if sayi1 > sayi2:
            print(sayi1, "ve ", sayi3, "eşit, ", sayi2, " den büyükler")
        elif sayi1 < sayi2:
            print(sayi1, "ve ", sayi3, "eşit, ", sayi2, " den küçükler")
    elif sayi2 == sayi3:
        if sayi2 > sayi1:
            print(sayi3, "ve ", sayi2, "eşit, ", sayi1, " den büyükler")
        elif sayi2 < sayi1:
            print(sayi3, "ve ", sayi2, "eşit, ", sayi1, " den küçükler")
else:
    if sayi1 > sayi2 and sayi1 > sayi3:
        if sayi2 > sayi3:
            print("En büyük : {} \nOrtanca : {} \nEn Küçük : {}".format(sayi1,sayi2,sayi3))
        else:
            print("En büyük : {} \nOrtanca : {} \nEn Küçük : {}".format(sayi1,sayi3,sayi2))
    elif sayi2 > sayi3 and sayi2 > sayi1:
        if sayi1 > sayi3:
            print("En büyük : {} \nOrtanca : {} \nEn Küçük : {}".format(sayi2, sayi1, sayi3))
        else:
            print("En büyük : {} \nOrtanca : {} \nEn Küçük : {}".format(sayi2, sayi3, sayi1))
    elif sayi3 > sayi1 and sayi3 > sayi2:
        if sayi1 > sayi2:
            print("En büyük : {} \nOrtanca : {} \nEn Küçük : {}".format(sayi3, sayi1, sayi2))
        else:
            print("En büyük : {} \nOrtanca : {} \nEn Küçük : {}".format(sayi3, sayi2, sayi1))
#Problem çözüldü.