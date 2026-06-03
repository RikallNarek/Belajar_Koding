# ==============================================
# TUGAS ANALISIS STATISTIK - WAKTU RESPON UGD
# ==============================================

# DATA
data = [3, 5, 2, 8, 4, 3, 10, 4, 2, 5, 3, 6, 1, 4, 3]

print("="*50)
print("DATA WAKTU RESPON UGD (DALAM MENIT)")
print("="*50)
print("Data:", data)
print("\n")

# 1. HITUNG MEAN (RATA-RATA)
mean_val = sum(data) / len(data)

# 2. HITUNG MEDIAN (NILAI TENGAH)
data_urut = sorted(data)
n = len(data_urut)
if n % 2 == 0:
    median_val = (data_urut[n//2 - 1] + data_urut[n//2]) / 2
else:
    median_val = data_urut[n//2]

# 3. HITUNG MODUS (NILAI SERING MUNCUL)
from collections import Counter
hitung = Counter(data)
modus_val = hitung.most_common(1)[0][0]

# MENAMPILKAN HASIL
print("-"*50)
print("HASIL PERHITUNGAN")
print("-"*50)
print(f"Mean   : {mean_val:.2f} menit")
print(f"Median : {median_val:.2f} menit")
print(f"Modus  : {modus_val} menit")
print("\n")

# 4. ANALISIS OUTLIER
Q1 = 3
Q3 = 5
IQR = Q3 - Q1

batas_bawah = Q1 - 1.5 * IQR
batas_atas = Q3 + 1.5 * IQR

print("-"*50)
print("ANALISIS OUTLIER")
print("-"*50)
print(f"Q1      : {Q1}")
print(f"Q3      : {Q3}")
print(f"IQR     : {IQR}")
print(f"Batas Bawah : {batas_bawah}")
print(f"Batas Atas  : {batas_atas}")

outlier = [x for x in data if x > batas_atas]

if outlier:
    print(f"--> Ditemukan Outlier: {outlier}")
else:
    print("--> Tidak ada Outlier")

print("\n" + "_"*50)
print("SELESAI!")
print("_"*50)