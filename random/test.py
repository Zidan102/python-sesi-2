def urutkan_kalimat(kalimat, urutan):
    kata_list = kalimat.split()
    hasil = [''] * len(urutan)
    
    for i in range(len(urutan)):
        hasil[i] = kata_list[urutan[i] - 1]    
    return ' '.join(hasil)

kalimat = input("Masukkan kalimat: ")

urutan_input = input("Masukkan urutan indeks kata (pisahkan dengan koma, contoh: 5,1,4,3,2): ")
urutan = [int(x.strip()) for x in urutan_input.split(',')]

hasil_akhir = urutkan_kalimat(kalimat, urutan)
print("Kalimat baru:", hasil_akhir)