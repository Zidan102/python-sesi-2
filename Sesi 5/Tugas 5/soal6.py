n1 = int(input("Masukan angka pertama: "))
n2 = int(input("Masukan angka kedua: "))
op = input("Masukan tipe operator aritmatika (+,-,*,/): ")
if op == '+':
    hasil_tambah = n1 + n2
    print("hasilnya adalah %s" % (hasil_tambah))
elif op == '-':
    hasil_kurang = n1 - n2
    print("Hasilnya adalah %s" % (hasil_kurang))
elif op == '*':
    hasil_kali = n1 * n2
    print("hasilnya adalah %s" % (hasil_kali))
elif op == '/' and n2 > 0:
    hasil_bagi = n1 / n2
    print("hasilnya adalah %s" % (hasil_bagi))
else:
    print("Program error")