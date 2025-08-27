import cv2
import matplotlib.pyplot as plt

#Membaca gambar
img = cv2.imread("C:/Users/ARINDA/Downloads/tes.jpg")

#Tampilkan dengan OpenCV
cv2.imshow("Citra Asli", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Tampilkan dengan Matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Tampilan dengan Matplotlib")
plt.show()

#Simpan gambar baru
cv2.imwrite("Hasil_tes.jpg", img)