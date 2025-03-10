berat = float(input("Masukan berat badan anda(dalam satuan KG): "))
tinggi = float(input("Masukan tinggi badan kamu(dalam satuan M): "))
tinggi2 = tinggi ** 2
hasil = berat / tinggi2

if hasil >= 30.0:
    kategori = "obesitas"
elif hasil >= 25.0 and hasil < 30.0:
    kategori = "kelebihan berat badan"
elif hasil >= 18.5 and hasil < 25.0:
    kategori = "Normal"
else:
    kategori = "kekurangan berat badan"

print("Dengan BMI %s, maka kamu termasuk kedalam %s" % (hasil,kategori))