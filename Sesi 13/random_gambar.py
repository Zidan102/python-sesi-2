import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

img1 = mpimg.imread('Sesi 13/meme/tung.jpg')
img2 = mpimg.imread('Sesi 13/meme/assa.jpg')
img3 = mpimg.imread('Sesi 13/meme/bre.jpg')
img4 = mpimg.imread('Sesi 13/meme/bom.jpg')
img5 = mpimg.imread('Sesi 13/troll.jpg')

img_list = [img1, img2, img3, img4, img5]
pick_img = random.choice(img_list)
plt.imshow(pick_img)
plt.axis('off')
plt.show()