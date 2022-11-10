def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

print("**** Quantum hesap makinesine hoş geldin ****")

while True:

    ilksayi = input("Lütfen işlem yapmak istediğiniz 1.sayıyı girin : ")
    ilksayi = int(ilksayi)
    ikincisayi = input("Lütfen işlem yapmak istediğiniz 2.sayıyı girin : ")
    ikincisayi = int(ikincisayi)
    islem = input("Toplama işlemi yapmak için t'ye basın \nÇıkarma işlemi yapmak için ç'ye basın \nÇarpma işlemi yapmak için c'ye basın \nBölme işlemi yapmak için b'ye basın \nÇıkmak için q'ya basın : ")
    if islem == 't':
        sonuc = toplama(ilksayi, ikincisayi)
        print(sonuc)
    elif islem == 'ç':
        sonuc = cikarma(ilksayi, ikincisayi)
        print(sonuc)
    elif islem == 'c':
        sonuc = carpma(ilksayi, ikincisayi)
        print(sonuc)
    elif islem == 'b':
        ilksayi = float(ilksayi)
        ikincisayi = float(ikincisayi)
        sonuc = bolme(ilksayi, ikincisayi)
        print(sonuc)
    elif islem == 'q':
        break
    else:
        print("Lütfen geçerli bir işlem seçiniz! ")

print("**** Quantum hesap makinesini kullandığınız için teşekkür ederiz ****")