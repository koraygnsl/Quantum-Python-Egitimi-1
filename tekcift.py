girilensayi = input("Lütfen bir sayı giriniz : ")
print(type(girilensayi))
girilensayi = int(girilensayi)
print(type(girilensayi))

if girilensayi%2 == 0:
    print("Girilen sayı çift")
else:
    print("Girilen sayı tek")
