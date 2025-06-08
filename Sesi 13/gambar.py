import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('Sesi 13/OIP.jpg')
plt.imshow(img)
plt.axis('off')  # Sembunyikan sumbu
plt.show()