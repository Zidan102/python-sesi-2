#import random
#def pilih():
#    pilihan = "gunting", "kertas", "batu"
#    skor_user = 0;
#    skor_komputer = 0;
#    pick_komputer = random.choice(pilihan)
#    print("Gunting, Kertas, Batu")
#pilih()
#inuser = input('Masukan pilihanmu: ')
#if inuser == "gunting" and pick_komputer == "kertas" or inuser == "kertas" and pick_komputer == "batu" or inuser == "batu" and pick_komputer == "gunting":
#    kategori = "kamu menang"
#    skor_user += 1
#elif inuser == "gunting" and pick_komputer == "batu" or inuser == "kertas" and pick_komputer == "gunting" or inuser == "batu" and pick_komputer == "kertas":
#    kategori = "komputer menang"
#    skor_komputer += 1
#else:
#    kategori = "seri"
#print("%s, karna kamu memilih %s dan komputer memilih %s" % (kategori,inuser,pick_komputer))
#    print()
#    pilih2 = input("Apakah kamu ingin bermain lagi?(Y/T) ").lower()
#    if pilih2 == 'y':
#        pilih()
#        inuser = input('Masukan pilihanmu: ')
#    else:
#        print("terima kasih!")