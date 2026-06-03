# =========================================
# UJI HIPOTESIS DETAK JANTUNG PASIEN
# Statistik Inferensial + p-value
# Histogram + Boxplot
# =========================================

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# -----------------------------------------
# DATA DETAK JANTUNG PASIEN
# -----------------------------------------

data = [78, 82, 75, 90, 85, 79, 81, 77, 88, 84]

# -----------------------------------------
# MENENTUKAN HIPOTESIS
# H0 : rata-rata = 80 bpm
# H1 : rata-rata ≠ 80 bpm
# -----------------------------------------

mu = 80   # rata-rata standar normal

# -----------------------------------------
# MENGHITUNG STATISTIK DASAR
# -----------------------------------------

n = len(data)
mean = np.mean(data)
std = np.std(data, ddof=1)

print("== HASIL STATISTIK ")
print(f"Jumlah Sampel       : {n}")
print(f"Rata-rata           : {mean:.2f}")
print(f"Standar Deviasi     : {std:.2f}")

# -----------------------------------------
# UJI t (One Sample t-Test)
# -----------------------------------------

t_stat, p_value = stats.ttest_1samp(data, mu)

print("\n== UJI HIPOTESIS")
print(f"t-hitung            : {t_stat:.4f}")
print(f"p-value             : {p_value:.4f}")

# -----------------------------------------
# KEPUTUSAN
# -----------------------------------------

alpha = 0.05

print("\n == KEPUTUSAN ")

if p_value < alpha:
    print("H0 ditolak")
    print("Rata-rata detak jantung berbeda dari normal")
else:
    print("H0 diterima")
    print("Rata-rata detak jantung masih normal")

# -----------------------------------------
# MEMBUAT HISTOGRAM
# -----------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(data, bins=5)

plt.title("Histogram Detak Jantung Pasien")
plt.xlabel("Detak Jantung (bpm)")
plt.ylabel("Frekuensi")

plt.grid(True)
plt.show()

# -----------------------------------------
# MEMBUAT BOXPLOT
# -----------------------------------------

plt.figure(figsize=(6, 4))

plt.boxplot(data)

plt.title("Boxplot Detak Jantung Pasien")
plt.ylabel("Detak Jantung (bpm)")

plt.grid(True)
plt.show()