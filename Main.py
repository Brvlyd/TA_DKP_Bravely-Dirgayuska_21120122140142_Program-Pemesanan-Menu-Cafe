import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

menu = {
    "Air Putih": 2000,
    "Air Es": 4000,
    "Es Teh Tawar": 6000,
    "Es Teh Manis": 8000,
    "Kopi Hitam": 10000,
    "Cappuccino": 15000,
    "Caffe Latte": 18000,
    "Espresso": 12000,
    "Mocha": 15000,
    "Matcha Latte": 15000,
    "Chocolate Panas": 15000,
    "Croissant": 18000,
    "Kue": 20000,
    "Bagel": 8000,
    "Donat": 7000,
    "Carbonara": 25000,
    "Roti Bakar": 16000,
    "Chicken Burger": 20000,
    "Cheeseburger": 21000,
    "Fish and Chips": 22000
}

def pesan_menu():
    index = menu_listbox.curselection()
    if index:
        item = menu_listbox.get(index)
        pesanan_listbox.insert(tk.END, item)
        jumlah_listbox.insert(tk.END, '1')  # Mengatur jumlah pesanan awal menjadi 1
        messagebox.showinfo("Informasi", f"{item} telah ditambahkan ke pesanan Anda.")
    else:
        messagebox.showinfo("Informasi", "Silakan pilih menu yang ingin dipesan.")

    menu_listbox.selection_clear(0, tk.END)  # Clear the selection after adding the item to pesanan_listbox

def kurangi_pesanan():
    if pesanan_listbox.curselection():
        index = pesanan_listbox.curselection()[0]
        pesanan_listbox.delete(index)
        jumlah_listbox.delete(index)

def hitung_total():
    total = 0
    pesanan_items = pesanan_listbox.get(0, tk.END)
    jumlah_items = jumlah_listbox.get(0, tk.END)

    for item, jumlah in zip(pesanan_items, jumlah_items):
        item_name = item.split(":")[0].strip()
        harga = menu[item_name]
        total += harga * int(jumlah)

    total_label.config(text=f"Total harga: Rp {total}")

def keluar_aplikasi():
    if messagebox.askokcancel("Konfirmasi", "Apakah Anda ingin keluar?"):
        window.destroy()

# Membuat jendela aplikasi
window = tk.Tk()
window.title("Cafe Menu")
window.configure(bg="#f5a680")  # Memberikan nuansa coklat muda pada background

window.attributes("-fullscreen", True)

judul_label = tk.Label(window, text="Cafe Xifutang", font=("Arial", 30, "bold"))
judul_label.pack()

bg_image = ImageTk.PhotoImage(Image.open("Hololive (1).jpg"))
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Membuat frame untuk menu
menu_frame = tk.Frame(window, bg="#f8c3aa")
menu_frame.pack(pady=12)  # Add padding of 12 pixels

cafe_label = tk.Label(window, text="Cafe Xifutang", font=("Monaco", 40, "bold"), bg="#f5a680")
cafe_label.place(x=20, y=120)

menu_label = tk.Label(menu_frame, text="Menu", font=("Arial", 23, "bold"), bg="#f8c3aa")
menu_label.pack()

menu_listbox = tk.Listbox(menu_frame, width=60, height=10)  # Atur lebar dan tinggi listbox
for item, harga in menu.items():
    menu_listbox.insert(tk.END, f"{item}: Rp {harga}")
menu_listbox.pack(side=tk.LEFT)

menu_scrollbar = tk.Scrollbar(menu_frame)
menu_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

menu_listbox.config(yscrollcommand=menu_scrollbar.set)
menu_scrollbar.config(command=menu_listbox.yview)

pesan_button = tk.Button(window, text="Pesan", font=("Arial", 10), command=pesan_menu, bg="#f8c3aa")
pesan_button.pack()

# Membuat frame untuk pesanan
pesanan_frame = tk.Frame(window, bg="#fcdecf")
pesanan_frame.pack(pady=12)  # Add padding of 12 pixels

pesanan_label = tk.Label(pesanan_frame, text="Pesanan", font=("Arial", 10, "bold"), bg="#F5F4DC")
pesanan_label.pack()

pesanan_listbox = tk.Listbox(pesanan_frame, width=35, height=10)
pesanan_listbox.pack(side=tk.LEFT)

pesanan_scrollbar = tk.Scrollbar(pesanan_frame)
pesanan_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

pesanan_listbox.config(yscrollcommand=pesanan_scrollbar.set)
pesanan_scrollbar.config(command=pesanan_listbox.yview)

# Membuat tombol untuk mengurangi pesanan
kurangi_button = tk.Button(window, text="Kurangi Pesanan", font=("Arial", 10), command=kurangi_pesanan, bg="#f8c3aa")
kurangi_button.pack()

# Membuat frame untuk jumlah pesanan
jumlah_frame = tk.Frame(window, bg="#fcdecf")
jumlah_frame.pack(pady=12)

jumlah_label = tk.Label(jumlah_frame, text="Jumlah", font=("Arial", 10, "bold"), bg="#F5F4DC")
jumlah_label.pack()

jumlah_listbox = tk.Listbox(jumlah_frame, width=2, height=10)
jumlah_listbox.pack(side=tk.LEFT)

jumlah_scrollbar = tk.Scrollbar(jumlah_frame)
jumlah_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

jumlah_listbox.config(yscrollcommand=jumlah_scrollbar.set)
jumlah_scrollbar.config(command=jumlah_listbox.yview)

# Membuat tombol untuk menghitung total harga
hitung_button = tk.Button(window, text="Hitung Total Harga", command=hitung_total, font=("Arial", 10), bg="#f8c3aa")
hitung_button.pack()

# Membuat label untuk menampilkan total harga
total_label = tk.Label(window, text="Total harga: Rp 0", font=("Arial", 19), bg="#fde1c3", fg="#fe1b30")
total_label.pack(pady=12)

keluar_button = tk.Button(window, text="Keluar", font=("Arial", 14),  fg="#fe1b30", bg="#f8c3aa", command=keluar_aplikasi)
keluar_button.pack(side=tk.RIGHT)

# Menjalankan aplikasi
window.mainloop()