# A. Membuat class dengan nama "Orang"
class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur}")

# B. Membuat class turunan dengan nama "Mahasiswa" dan "Pekerja"
class Mahasiswa(Orang):
    def __init__(self, nama, umur, universitas):
        super().__init__(nama, umur)
        self.universitas = universitas

    # C. Override method "kenalan" untuk class Mahasiswa
    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur} dan aku kuliah di {self.universitas}")

class Pekerja(Orang):
    def __init__(self, nama, umur, tempatKerja):
        super().__init__(nama, umur)
        self.tempatKerja = tempatKerja

    # D. Override method "kenalan" untuk class Pekerja
    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur} dan aku kerja di {self.tempatKerja}")

# E. Membuat object dari class "Orang", "Mahasiswa", dan "Pekerja"
orang1 = Orang("Andi", 40)
mahasiswa1 = Mahasiswa("Budi", 20, "Universitas Indonesia")
pekerja1 = Pekerja("Citra", 30, "PT Maju Mundur")

# Memanggil method "kenalan" untuk setiap object
orang1.kenalan()
mahasiswa1.kenalan()
pekerja1.kenalan()
