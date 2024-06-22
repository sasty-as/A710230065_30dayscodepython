 #fungsi pada python

def apakah_prima(bilangan):
    # Jika bilangan kurang dari atau sama dengan 1, bukan prima
    if bilangan <= 1:
        print("Bukan Bilangan Prima")
        return

    # Memeriksa apakah bilangan habis dibagi oleh angka lain selain 1 dan dirinya sendiri
    for i in range(2, bilangan):
        if bilangan % i == 0:
            print("Bukan Bilangan Prima")
            return

    # Jika loop selesai tanpa menemukan pembagi selain 1 dan dirinya sendiri, maka prima
    print("Bilangan Prima")

# Contoh penggunaan fungsi
bil = int(input("Masukkan bilangan bulat: "))
apakah_prima(bil)
