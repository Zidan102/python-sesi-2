uang = int(input("Masukan jumlah uang: "))
ratusan = uang - 100000
sisa_ratusan = (uang - ratusan) % 100000
puluh5 = uang - 50000
puluh2 = uang - 20000
puluh1 = uang - 10000
ribu5 = uang - 5000
ribu2 = uang - 2000
ribu1 = uang - 1000

print('jumlah ', int(ratusan))
print('jumlah  ', int(puluh5))
print('jumlah  ', int(puluh2))
print('jumlah  ', int(puluh1))
print('jumlah  ', int(ribu5))
print('jumlah  ', int(ribu2))
print('jumlah  ', int(ribu1))