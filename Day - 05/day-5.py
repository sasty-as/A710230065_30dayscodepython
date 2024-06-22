from datetime import datetime

# Fungsi untuk menghitung umur berdasarkan tahun kelahiran
def hitung_umur(tahun_lahir):
    tahun_sekarang = datetime.now().year
    return tahun_sekarang - tahun_lahir

# Fungsi untuk menghitung harga tiket setelah diskon berdasarkan umur
def hitung_diskon(umur, harga_tiket):
    if umur <= 4:
        return 0  # Diskon 100%
    elif 5 <= umur <= 12:
        return harga_tiket * 0.5  # Diskon 50%
    else:
        return harga_tiket  # Tidak ada diskon

# Input dari pengguna
tahun_lahir = int(input("Masukkan tahun kelahiran penumpang: "))
harga_tiket = float(input("Masukkan harga tiket kereta api: "))

# Menghitung umur penumpang
umur = hitung_umur(tahun_lahir)

# Menghitung harga tiket setelah diskon
harga_setelah_diskon = hitung_diskon(umur, harga_tiket)

# Menampilkan hasil
print(f"Umur penumpang: {umur} tahun")
print(f"Harga tiket setelah diskon: Rp {harga_setelah_diskon:.2f}")

 