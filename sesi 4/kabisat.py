tahun = int(input('masukan tahunnya: '))

if tahun % 4 == 0:
    print('%s adalah tahun kabisat'%(tahun))
else:
    print('%i bukan tahun kabisat'%(tahun))