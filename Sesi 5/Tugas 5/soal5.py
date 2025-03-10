tahun = int(input("masukan tahunnya: "))
keterangan = "kabisat" if tahun % 4 == 0 and tahun % 100 != 0 or tahun % 400 == 0 else 'bukan kabisat'
print("Tahun %s adalah %s" % (tahun, keterangan))