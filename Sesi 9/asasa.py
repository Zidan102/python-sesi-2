nama = 'zidan'
total = len(nama)
nama = nama.upper()

for i in range(total):
    print(nama[:total-i] + ('*' * (i-2)))