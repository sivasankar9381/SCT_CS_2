import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

def encrypt_image(path, key=123):
    img = Image.open(path).convert('RGB')  # ensure it's RGB
    arr = np.array(img, dtype=np.uint8)
    encrypted_arr = np.bitwise_xor(arr, key)  # XOR encryption avoids overflow
    encrypted_img = Image.fromarray(encrypted_arr, 'RGB')
    return encrypted_img

def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if file_path:
        global original_image_path
        original_image_path = file_path
        img = Image.open(file_path).resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        panel_original.config(image=img_tk)
        panel_original.image = img_tk

def save_encrypted():
    if not original_image_path:
        messagebox.showerror("Error", "Please select an image first!")
        return
    encrypted = encrypt_image(original_image_path)
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    if save_path:
        encrypted.save(save_path)
        img_tk = ImageTk.PhotoImage(encrypted.resize((200, 200)))
        panel_encrypted.config(image=img_tk)
        panel_encrypted.image = img_tk
        messagebox.showinfo("Success", f"Encrypted image saved:\n{save_path}")

# GUI Setup
original_image_path = None
root = tk.Tk()
root.title("Image Encryption Tool")

tk.Label(root, text="Original Image").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Encrypted Image").grid(row=0, column=1, padx=10, pady=10)

panel_original = tk.Label(root)
panel_original.grid(row=1, column=0, padx=10, pady=10)

panel_encrypted = tk.Label(root)
panel_encrypted.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Choose Image", command=open_image).grid(row=2, column=0, pady=10)
tk.Button(root, text="Encrypt and Save", command=save_encrypted).grid(row=2, column=1, pady=10)

root.mainloop()