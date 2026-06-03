#
# PROGRAM MENAMPILKAN DAFTAR MENU MAKANAN
#

# Data menu makanan
menu = [
    {"nama": "bakso", "harga": 15000},
    {"nama": "nasi ikan", "harga": 10000},
    {"nama": "nasi ayam", "harga": 25000},
    {"nama": "soto ayam", "harga": 20000},
    {"nama": "sate ayam", "harga": 13000}
]
# Inisialisasi
i = 0
Total_data = len(menu)
print("_"*20)
print("   DAFTAR MENU MAKANAN  ")
print("_"*20)
print("No\tNama Menu\t\tHarga")
print("_"*20)
# Bagian ini adalah perulangan

while i < Total_data:
    print(f"{i+1}\t{menu[i]['nama']}\t\tRp{menu[i]['harga']:,}")
    i = i + 1 #
print("_"*20)
