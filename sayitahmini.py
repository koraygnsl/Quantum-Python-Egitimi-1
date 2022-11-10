tutulansayi = 44

while True:
    tahminsayisi = input("Sayıyı tahmin et : ")
    tahminsayisi = int(tahminsayisi)
    if tahminsayisi == tutulansayi:
        print("Doğru tahmin! ")
        break
    elif tahminsayisi != tutulansayi:
        if tahminsayisi < tutulansayi:
            print("Daha yüksek bir sayı")
        elif tahminsayisi > tutulansayi:
            print("Daha düşük bir sayı")