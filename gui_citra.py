import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Fungsi untuk membuka gambar
def open_image():
    global img, img_tk
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.png *.jpeg")]
    )
    if file_path:
        img = cv2.imread(file_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)
        canvas1.create_image(0, 0, anchor="nw", image=img_tk)

# Fungsi untuk proses gambar (ubah ke grayscale)
def process_image():
    global img, img_tk2
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_pil = Image.fromarray(gray)
        img_tk2 = ImageTk.PhotoImage(img_pil)
        canvas2.create_image(0, 0, anchor="nw", image=img_tk2)

# Inisialisasi GUI
root = tk.Tk()
root.title("GUI Pengolahan Citra Python")

# Canvas untuk gambar asli dan hasil
canvas1 = tk.Canvas(root, width=300, height=300, bg="gray")
canvas1.grid(row=0, column=0)

canvas2 = tk.Canvas(root, width=300, height=300, bg="gray")
canvas2.grid(row=0, column=1)

# Tombol Open dan Proses
btn_open = tk.Button(root, text="Open", command=open_image)
btn_open.grid(row=1, column=0, pady=10)

btn_process = tk.Button(root, text="Proses", command=process_image)
btn_process.grid(row=1, column=1, pady=10)

# Variabel global gambar
img = None
img_tk = None
img_tk2 = None

root.mainloop()
