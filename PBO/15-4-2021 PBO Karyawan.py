class Karyawan:
    '''Daftar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, gaji, usia, jenis_kelamin):
        self.nama = nama
        self.gaji = gaji
        self.usia = usia
        self.jenis_kelamin = jenis_kelamin
        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah():
        print("Total Karyawan :", Karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)
        print("Usia :", self.usia)
        print("Jenis Kelamin :", self.jenis_kelamin)
    
daftar_karyawan = []
daftar_karyawan.append(Karyawan("Sarah", 1000000, 22, "Perempuan"))
daftar_karyawan.append(Karyawan("Budi", 2000000, 25, "Laki - Laki"))
daftar_karyawan.append(Karyawan("Jono", 1500000, 28, "Laki - Laki"))
daftar_karyawan.append(Karyawan("Ratna", 4500000, 43, "Perempuan"))

for karyawan in daftar_karyawan:
    karyawan.tampilkan_profil()
Karyawan.tampilkan_jumlah()
print()