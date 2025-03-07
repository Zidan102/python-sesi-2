angka = int(input('masukan angkanya: '))

if angka == 0:
    bil = "nol"
elif angka >= 0:
    bil = "positif"
elif angka <= 0:
    bil = "negatif"

print(angka, "adalah angka %s" % (bil))