def menu():
    data = {}

    while True:
        print("\nMenu:")
        print("1. Masukan data baru dengan NIM")
        print("2. Mengecek semua data yang ada")
        print("3. Mengecek data menggunaka NIM")
        print("4. Menghapus data dengan NIM")
        print("5. Keluar")

        pilihan = int(input("Masukan menu yang akan kamu pilih: "))

        if pilihan == 1:
            try:
                nim = int(input("Masukan NIM yang akan ditambahkan: "))
                nama = input("Masukan nama anda: ")
                jurusan = input("Masukan Jurusan anda: ")
                ipk = float(input("Masukan IPK anda: "))
                data[nim]= {"Nama" : nama, "Jurusan" : jurusan, "IPK" : ipk}
            except ValueError:
                print("NIM harus berupa angka")
        elif pilihan == 2:
            print(data)
        elif pilihan == 3:
            cek_nim = int(input("Masukan NIM yang ingin kamu cari datanya: "))
            if cek_nim in data:
                print(data[cek_nim])
            else:"NIM yang anda masukan salah atau tidak ada"
        elif pilihan == 4:
            del_nim = int(input("Masukan NIM yang ingin kamu hapus datanya: "))
            if del_nim in data:
                data.pop(del_nim)
                print("Data yang anda masukan telah sukses dihapus")
            else:"NIM yang kamu masukan salah atau tidak ada"
        elif pilihan == 5:
            print("Terima kasih!")
            break
        else:"Menu yang anda input tidak ada"

if __name__ == "__main__":
    menu()