"""
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""
sayi1 = int(input("1. Sayı : "))
sayi2 = int(input("2. Sayı : "))
print("1 = ",sayi1,"/ 2 = ",sayi2)
print("Sayılar değiştiriliyor....")
sayi1,sayi2 = sayi2,sayi1
print("1 = ",sayi1,"/ 2 = ",sayi2)
#Problem çözüldü.