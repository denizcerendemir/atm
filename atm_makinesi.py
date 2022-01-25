print(
"""***********DCD ATM'SİNE HOŞGELDİNİZ***********
1.İşlem: Bakiye Sorgulama
2.İşlem : Para Yatırma
3.İşlem : Para Çekme
Programdan çıkmak için q'ya basınız.
     ********************** """)
bakiye= 1000
while True :
    islem= int(input("Yapmak istediğiniz işlemi seçiniz:"))

    if (islem == "q") :
        print("Sistemden başarıyla çıkış yapıldı...")
        break
    elif islem ==1 :
        print("Bakiyeniz: {}".format(bakiye))
    elif islem ==2 :
        miktar1= int(input("Yatırmak istediğiniz miktar:"))
        bakiye += miktar1
    elif islem ==3 :
        miktar = int(input("Çekmek istediğiniz miktarı giriniz :"))
        if bakiye - miktar < 0:
            print("Yetersiz Bakiye!")
            print("Bakiyeniz : {}".format(bakiye))
            continue
        bakiye -= miktar
    else:
        print("Lütfen geçerli bir işlem giriniz.")
