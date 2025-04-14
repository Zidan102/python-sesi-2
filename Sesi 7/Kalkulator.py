def menu():
    print("=== Calculator ===")
    print()
    print('1.+')
    print('2.-')
    print('3.*')
    print('4./')
    print('5. Keluar')

menu()
pilihan = int(input("Pilih operasi yang akan kamu jalankan: "))

while pilihan != 5:
    n1 = int(input("Masukan angka pertama: "))
    n2 = int(input("Masukan angka kedua: "))
    if pilihan == 1:
        hasil_plus = n1 + n2
        print('Hasil penjumlahan dari %s dan %s adalah'%(n1,n2),hasil_plus)
    elif pilihan == 2:
        hasil_minus = n1 - n2
        print('Hasil perkurangan dari %s dan %s adalah'%(n1,n2), hasil_minus,)
    elif pilihan == 3:
        hasil_kali = n1 * n2
        print('Hasil perkalian dari %s dan %s adalah'%(n1,n2), hasil_kali)
    elif pilihan == 4:
        hasil_bagi = n1 / n2
        print('Hasil pembagian dari %s dan %s adalah'%(n1,n2), hasil_bagi)
    elif pilihan != 1 or 2 or 3 or 4 or 5:
        print("Operasi tidak ada")
    menu()
    pilihan = int(input("Pilih operasi yang akan kamu jalankan: "))

print("Terima kasih")