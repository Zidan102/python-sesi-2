from datetime import datetime

# def hitungUmur(tahunLahir):
#     tahunIni = datetime.now().year
#     umur = tahunIni - tahunLahir
#     print("Umur ",umur)
#
# tahunLahir = int(input("Masukan tahun lahir: "))
# hitungUmur(tahunLahir)

# def hitungUmur(tahunLahir):
#     tahunIni = datetime.now().year
#     umur = tahunIni - tahunLahir
#     return umur
#
# tahunLahir = int(input("Masukan tahun lahir: "))
# umur = hitungUmur(tahunLahir)
# print("Umur anda",umur, "Tahun")

# def selamatDatang(nama):
#     print('Halo',nama+",","Selamat datang")
#
# selamatDatang('Nurul')
# selamatDatang('Landis')
# selamatDatang('Febri')
# selamatDatang('Isa')

# def konversiSuhu(suhu, dari="C", ke="R"):
#     if (dari == "C" and ke == "R" or ke == "K"):
#         return suhu+273.15
#
# suhu = float(input())

# def konversiSuhu(suhu,ke):
#     if ke == "K":
#         return print(suhu+273.15)
#     else: return print((suhu*9/5)+32)
#
# suhu = float(input("Masukan derajat suhu(Celcius): "))
# ke = input("Pilih konversi yang dituju (F/K): ")
# konversiSuhu(suhu,ke)

def konversisuhu(suhu,ke):
    if ke == "K":
        konversi = (suhu+273.15)
        return print("Konversi dari %s C adalah %s %s"%(suhu,konversi,ke))
    elif ke == "F":
        print("Konversi dari %s C adalah %s %s"%(suhu,(suhu*9/5)+32,ke))
    elif ke == "R":
        print("Konversi dari %s C adalah %s %s" % (suhu,4/5*suhu, ke))
        return

suhu = float(input("Masukan derajat suhu(Celcius): "))
ke = input("Pilih konversi yang dituju (F/K/R): ").upper()
konversisuhu(suhu,ke)