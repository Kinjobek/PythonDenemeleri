import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

"""
SMTP Modülü ile mail gönderme

Gmail'den daha az güvenli uygulamalar için güvenliği kaldır. -> https://myaccount.google.com/lesssecureapps

"""

mesaj = MIMEMultipart()  # Mail yapısı

mesaj["From"] = "...@gmail.com"  # Kimden
mesaj["To"] = "....@windowslive.com"  # Kime
mesaj["Subject"] = "Smtp Message"  # Mail Konusu

icerik = """

Smtp ile mesaj deneme.
gmail ve hotmail gönderimi basarili.
Sira windowslive'da(basarili)
Mebon


"""
mesaj_icerigi = MIMEText(icerik, "plain")  # Mailimizin gövdesini bu sınıftan oluşturuyoruz.
mesaj.attach(mesaj_icerigi)  # Mailimizin gövdesini mail yapımıza ekliyoruz.

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)  # SMTP objemizi oluşturuyoruz ve gmail smtp server'ına bağlanıyoruz.
    mail.ehlo()  # SMTP serverına kendimizi tanıtıyoruz.
    mail.starttls()  # Adresimizin ve Parolamızın şifrelenmesi için gerekli

    mail.login("....@gmail.com",
               "sifre")  # SMTP server'ına giriş yapıyoruz. Kendi mail adresimizi ve parolamızı yapıyoruz.
    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())  # Mailimizi gönderiyoruz.
    print("Mail başarıyla gönderildi....")
    mail.close()  # Smtp serverımızın bağlantısını koparıyoz.

except:
    sys.stderr.write(
        "Mail göndermesi başarısız oldu...")  # Herhangi bir bağlanma sorunu veya mail gönderme sorunu olursa
    sys.stderr.flush()