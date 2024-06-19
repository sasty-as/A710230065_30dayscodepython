# Meminta input jumlah anak bebek dari pengguna
jumlah_anak_bebek = int(input("Masukkan jumlah anak bebek: "))

# Loop untuk menampilkan lirik lagu Anak Bebek
for i in range(jumlah_anak_bebek, 0, -1):
    if i == 1:
        print(f"Anak bebek turun {i}, mati satu tinggal induknya")
    else:
        print(f"Anak bebek turun {i}, mati satu tinggal {i-1}")
