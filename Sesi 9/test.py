nama = input('Masukan namamu: ')
total = len(nama)
nama = nama.upper()

for i in range(total):
    print(' '.join(nama[:total-i] + ('*' * (i-1+1))))