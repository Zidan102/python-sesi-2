usia = float(input('Masukan umur anak anda: '))

if usia >= 18:
    keterangan = 'Dewasa'
    print('Anak kmu adalah %s' % (keterangan))
elif usia >= 12:
    keterangan = 'Remaja'
    print('Anak kmu adalah %s' % (keterangan))
elif usia >= 5:
    keterangan = 'Anak - anak'
    print('Anak kmu adalah %s' % (keterangan))
elif usia >= 2:
    keterangan = 'Balita'
    print('Anak kmu adalah %s' % (keterangan))
else:
    print('Anak anda adalah bayi')