harga = int(input('Masukan harga kendaraan: '))
mobil = 143000
motor = 35000
njkb = 2;
plus_njkb = 5
nilai_jual = int(input('Masukan NJPB anda: '))
if nilai_jual == 1:
    njkb += 0
elif nilai_jual > 1:
    njkbawal = nilai_jual - 1
    pnjkb = njkbawal * plus_njkb
    pajak = (pnjkb/10) + njkb
    njkb += pajak - 2
kendaraan = input('Masukan jenis kendaraan: ')
if kendaraan == 'Motor' or 'motor':
    pajak_motor = (harga * (njkb/100)) + motor
    print('Pajak kmu adalah %s' % (pajak_motor))
elif kendaraan == 'mobil' or 'Mobil':
    pajak_mobil = (harga * (njkb/100)) + mobil
    print('Pajak kendaraan kmu adalah %s' % (pajak_mobil))