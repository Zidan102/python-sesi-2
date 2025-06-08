import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

secret_number = random.randint(1, 100)

for attempts in range(1, 8):
    print(f"Percobaan ke-{attempts}:")
    guess = int(input("Tebak angka dari 1 hingga 100: "))
    if guess < secret_number:
        print("Terlalu rendah.")
    elif guess > secret_number:
        print("Terlalu tinggi.")
    else:
        print(f"Selamat! Angka yang benar adalah {secret_number}. Anda berhasil dalam {attempts} percobaan.")
        break

    if attempts == range:
        print(f"Maaf, Anda telah kehabisan percobaan. Angka yang benar adalah {secret_number}.")
        img = mpimg.imread('random/img/bomb.jpg')
        plt.imshow(img)
        plt.axis('off')
        plt.show()
        
print("Permainan selesai.")