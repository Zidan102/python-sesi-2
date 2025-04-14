nama = input('Masukan nama: ')
for i in range(1, len(nama) + 1):
    hasil = nama[:i] + '*' * (len(nama) - i)
    print(hasil)