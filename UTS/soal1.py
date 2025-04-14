harga_printer = int(input('Masukan harga barang: '))
harga_masa = int(input('Masukan harga masa: '))
susut_tahunan = (harga_printer - harga_masa) / 5
tahun = int(input("masukan tahun: "))
fsusut = susut_tahunan * tahun
NAT = harga_printer - fsusut
print('Jadi dalam %s tahun, nilai aset yang tersisa adalah %s'%(tahun,NAT))