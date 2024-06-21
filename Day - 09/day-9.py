# Meminta input dari pengguna untuk nama dan nomor telepon
phone_book = {}
for i in range(1, 6):
    nama = input(f"Masukkan nama teman ke-{i}: ")
    no_hp = input(f"Masukkan nomor telepon {nama}: ")
    phone_book[nama] = no_hp

# Menampilkan output dalam format yang diminta
print("Phone Book\n")
for index, (nama, no_hp) in enumerate(phone_book.items(), start=1):
    print(f"{index}. {nama} = {no_hp}")
