import random

def pilihan():
    print('Permainan gunting, kertas, batu!')

gukeba = "gunting", "kertas", "batu"
skor_user = 0;
skor_komputer = 0;
pick_komputer = random.choice(gukeba)
pilihan()
inuser = input("Pilih pilihanmu! (gunting, kertas, batu)? ")

while inuser != gukeba:
    if inuser == "gunting" and pick_komputer == "kertas" or inuser == "kertas" and pick_komputer == "batu" or inuser == "batu" and pick_komputer == "gunting":
    pass