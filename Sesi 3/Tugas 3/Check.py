a = int(input("Masukan angka A: "))
b = int(input("Masukan angka B: "))
c = int(input("Masukan angka C: "))

genap = (a % 2) == 0
ganjil = (c % 2) != 0
if a > b and b > c and b != c and ganjil is True and genap is True:
    print('Angka Valid')
elif ganjil is False:
    print('Angka tidak valid karna c bukan ganjil')
elif genap is False:
    print('Angka tidak valid karna a bukan genap')
elif a < b:
    print('Angka tidak valid karna a lebih kecil daripada b')
elif b < c:
    print('Angka tidak valid karna b lebih kecil daripada c')
elif b == c:
    print('Angka tidak valid karna b dan c nilainya sama')