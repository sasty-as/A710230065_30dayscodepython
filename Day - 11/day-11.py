# kalkulator pengeluaran harian
# Program ini membantu pengguna mencatat dan menghitung total pengeluaran harian.

def tambah_pengeluaran(pengeluaran, deskripsi, jumlah):
    pengeluaran.append({"deskripsi": deskripsi, "jumlah": jumlah})

def hitung_total(pengeluaran):
    total = sum(item["jumlah"] for item in pengeluaran)
    return total

def tampilkan_pengeluaran(pengeluaran):
    for item in pengeluaran:
        print(f"{item['deskripsi']}: Rp{item['jumlah']:,}")

def main():
    # Daftar pengeluaran harian
    pengeluaran = []

    while True:
        deskripsi = input("Masukkan pengeluaran hari ini (atau ketik 'selesai' untuk berhenti): ")
        if deskripsi.lower() == 'selesai':
            break

        try:
            jumlah = int(input("Masukkan harga pengeluaran: "))
        except ValueError:
            print("Jumlah pengeluaran harus berupa angka. Silakan coba lagi.")
            continue

        tambah_pengeluaran(pengeluaran, deskripsi, jumlah)

    # Menampilkan daftar pengeluaran
    print("\nDaftar Pengeluaran Harian:")
    tampilkan_pengeluaran(pengeluaran)

    # Menghitung total pengeluaran
    total = hitung_total(pengeluaran)
    print(f"\nTotal Pengeluaran: Rp{total:,}")

if __name__ == "__main__":
    main()

