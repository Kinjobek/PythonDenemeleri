"""
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
Hipotenüs Formülü: a^2 + b^2 = c^2
"""
print("Dik üçgenin hipotenüs uzunluğunu bulma")
print("a²+b²=c²")
a = int(input("a'yı giriniz :"))
b = int(input("b'yı giriniz :"))
c = (a**2+b**2)**0.5
print(a**2,"+",b**2,"=","{:.2f}".format(c**2))
print(a,"²+",b,"²=","{:.2f}".format(c),"²",sep="")
print("c =","{:.2f}".format(c))
#Problem Çözüldü