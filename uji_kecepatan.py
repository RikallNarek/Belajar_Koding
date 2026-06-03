import math

# Coba import scipy
try:
    from scipy import stats
    scipy_available = True
except:
    scipy_available = False

# Data loading website (detik)
data = [2.5, 2.8, 3.1, 2.9, 3.0, 2.7, 2.6, 3.2, 2.8, 2.9]

# Parameter
mu0 = 3
alpha = 0.05

# Jumlah data
n = len(data)

# Rata-rata
mean = sum(data) / n

# Standar deviasi (sample)
std_dev = math.sqrt(sum((x - mean) ** 2 for x in data) / (n - 1))

# t hitung
t_hit = (mean - mu0) / (std_dev / math.sqrt(n))

print("=== HASIL UJI HIPOTESIS ===")
print(f"Jumlah data: {n}")
print(f"Rata-rata: {mean:.3f}")
print(f"Standar deviasi: {std_dev:.3f}")
print(f"t hitung: {t_hit:.3f}")

# Jika scipy tersedia
if scipy_available:
    df = n - 1
    t_tabel = stats.t.ppf(1 - alpha, df)
    p_value = 1 - stats.t.cdf(t_hit, df)

    print(f"t tabel: {t_tabel:.3f}")
    print(f"p-value: {p_value:.5f}")

    if t_hit > t_tabel:
        print("Keputusan: Tolak H0")
        print("Kesimpulan: Website lebih lambat dari 3 detik")
    else:
        print("Keputusan: Gagal menolak H0")
        print("Kesimpulan: Website masih memenuhi standar (≤ 3 detik)")

# Jika scipy tidak tersedia
else:
    print("\n(scipy tidak ditemukan, pakai perbandingan manual)")
    t_tabel = 1.833  # df=9, alpha=0.05

    print(f"t tabel (manual): {t_tabel}")

    if t_hit > t_tabel:
        print("Keputusan: Tolak H0")
    else:
        print("Keputusan: Gagal menolak H0")