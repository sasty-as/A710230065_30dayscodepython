# mendefinisikan variabel
nama_depan = input("Masukkan nama depan Anda: ")
nama_belakang = input("Masukkan nama belakang Anda: ")

# Output nama lengkap
nama_lengkap = nama_depan + " " + nama_belakang
print("Nama lengkap Anda adalah:", nama_lengkap)

# Operasi pada string
nama_lengkap_upper = nama_lengkap.upper()
nama_lengkap_lower = nama_lengkap.lower()
panjang_nama = len(nama_lengkap)

# Output hasil operasi
print("Nama lengkap dalam huruf besar:", nama_lengkap_upper)
print("Nama lengkap dalam huruf kecil:", nama_lengkap_lower)
print("Panjang nama lengkap (termasuk spasi):", panjang_nama)

# Tambahan: memeriksa apakah nama depan atau nama belakang mengandung huruf tertentu
huruf_diperiksa = input("Masukkan huruf yang ingin diperiksa: ").lower()
memuat_huruf = huruf_diperiksa in nama_lengkap_lower

print(f"Apakah nama lengkap mengandung huruf '{huruf_diperiksa}'?:", memuat_huruf)
