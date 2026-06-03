# ==========================================
# PROGRAM PEMESANAN MAKANAN (RESTORAN)
# ==========================================

# Daftar Menu Makanan & Minuman
menu = {
    1: {"nama": "Nasi Goreng", "harga": 15000},
    2: {"nama": "Mie Goreng", "harga": 12000},
    3: {"nama": "Ayam Bakar", "harga": 20000},
    4: {"nama": "Es Teh", "harga": 3000},
    5: {"nama": "Es Jeruk", "harga": 4000}
}

keranjang = []

print("_"*35)
print("        MENU RESTORAN MAKANAN       ")
print("_"*35)
print(f"{'No':<3} {'Nama Menu':<15} {'Harga':>10}")
print("_"*35)
for nomor, item in menu.items():
    print(f"{nomor:<3} {item['nama']:<15} Rp {item['harga']:>8,.0f}")
print("_"*35)

# Proses Pemesanan (Menggunakan Looping)
while True:
    print("\n MASUKKAN PESANAN ")
    
    # Input nomor menu
    while True:
        try:
            pilih = int(input("Pilih nomor menu  : "))
            if pilih in menu:
                break
            else:
                print("Nomor menu tidak tersedia! Coba lagi.")
        except ValueError:
            print("Harap masukkan angka!")

    # Input jumlah
    while True:
        try:
            jumlah = int(input("Masukkan jumlah    : "))
            if jumlah > 0:
                break
            else:
                print("Jumlah harus lebih dari 0!")
        except ValueError:
            print("Harap masukkan angka!")

    # Hitung subtotal
    nama_menu = menu[pilih]['nama']
    harga_satuan = menu[pilih]['harga']
    subtotal = harga_satuan * jumlah

    # Simpan ke keranjang
    keranjang.append({
        'menu': nama_menu,
        'jumlah': jumlah,
        'harga': harga_satuan,
        'subtotal': subtotal
    })

    # Tanya tambah lagi?
    lanjut = input("\nTambah pesanan lain? (y/t): ")
    if lanjut.lower() == 't':
        break

# ==========================================
# CETAK STRUK PEMBAYARAN
# ==========================================
print("\n\n")
print("_"*40)
print("          STRUK PEMBAYARAN           ")
print("          RESTORAN MAKANAN           ")
print("_"*40)
print(f"{'Menu':<15} {'Jml':>3} {'Harga':>10} {'Total':>10}")
print("_"*40)

total_bayar = 0
for beli in keranjang:
    print(f"{beli['menu']:<15} {beli['jumlah']:>3} Rp {beli['harga']:>7,.0f} Rp {beli['subtotal']:>7,.0f}")
    total_bayar += beli['subtotal']

print("_"*40)
print(f"{'TOTAL BAYAR':<28} Rp {total_bayar:>9,.0f}")

# Input Uang Bayar
while True:
    try:
        bayar = int(input("\nMasukkan uang bayar: Rp "))
        if bayar >= total_bayar:
            break
        else:
            print(f"Uang kurang! Kurang Rp {total_bayar - bayar:,}")
    except ValueError:
        print("Harap masukkan angka!")

kembalian = bayar - total_bayar
print(f"Kembalian       : Rp {kembalian:>9,.0f}")

print("\n" + "_"*40)
print("Terima kasih sudah makan di sini!")
print("_"*40)