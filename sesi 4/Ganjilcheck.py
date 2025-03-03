angka = int(input('Masukan angka: '))

if angka % 2 == 0:
    jenis = "genap"
    jenis2 = 'ganjil'
    print('%s adalah angka %s'%(angka, jenis))
else:
    print('%s adalah angka ganjil'%(angka))