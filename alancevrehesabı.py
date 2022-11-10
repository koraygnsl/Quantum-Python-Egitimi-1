uzunkenar = input("Lütfen uzun kenarın ölçüsünü giriniz : ")
kisakenar = input("Lütfen kısa kenarın ölçüsünü giriniz : ")
uzunkenar = int(uzunkenar)
kisakenar = int(kisakenar)

def cevrehesap(uzunkenar, kisakenar):
    return uzunkenar*2 + kisakenar*2

def alanhesap(a,b):
    return a*b
cevre = cevrehesap(uzunkenar,kisakenar)
print("Girilen dikdörtgenin çevresi : " + str(cevre))

alan = alanhesap(uzunkenar,kisakenar)
print("Girilen dikdörtgenin alanı : " + str(alan))