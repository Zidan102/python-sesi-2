sisi1 = int(input("Masukan sisi pertama: "))
sisi2 = int(input("Masukan sisi kedua: "))
sisi3 = int(input("Masukan sisi ketiga: "))

if sisi1 ==0 or sisi2 == 0 or sisi3 == 0:
    kategori = "Tidak dapat membuat segitiga"
elif sisi1 == sisi2 and sisi2 == sisi3:
    kategori = "Segitiga sama sisi"
elif sisi1 == sisi2 or sisi2 == sisi3 or sisi3 == sisi1:
    kategori = "Segitiga sama kaki"
else:
    kategori = "Segitiga sembarang"
print("%s adalah hasil yang kamu dapatkan dengan angka yang kamu masukan." % (kategori))