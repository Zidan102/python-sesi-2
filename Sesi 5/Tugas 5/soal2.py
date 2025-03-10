angka = int(input('Masukan angkanya: '))
keterangan = "genap" if angka % 2 == 0 else "ganjil"
print("%s merupakan bilangan %s" % (angka, keterangan))