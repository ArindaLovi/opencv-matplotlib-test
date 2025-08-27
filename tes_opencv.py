import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import cv2

print("Numpy version:", np.__version__)
print("Matplotlib version:", matplotlib.__version__)
print("OpenCV version:", cv2.__version__)

# Membuat gambar kosong (hitam 200x200)
img = np.zeros((200, 200, 3), dtype=np.uint8)

# Menambahkan garis putih
cv2.line(img, (50, 50), (150, 150), (255, 255, 255), 2)

# Menampilkan menggunakan matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Tes OpenCV + Matplotlib + Numpy")
plt.show()
