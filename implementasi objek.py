class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)


class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            print("Nama:", mahasiswa.nama)
            print("NIM:", mahasiswa.nim)


class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print("Nama Jurusan:", jurusan.NamaJurusan)


# Implementasi sesuai dengan pertanyaan

# 1. Membuat objek Mahasiswa
mahasiswa = Mahasiswa("ANUGRAH HERIANTO", "G1A022068", None)

# 2. Membuat objek Jurusan
jurusan = Jurusan("Teknik Informatika")

# 3. Membuat objek Universitas
universitas = Universitas("XYZ University")

# 4. Menambahkan objek Jurusan ke dalam objek Universitas
universitas.tambah_jurusan(jurusan)

# 5. Menambahkan objek Mahasiswa ke dalam objek Jurusan
jurusan.tambah_mahasiswa(mahasiswa)

# 6. Menampilkan daftar jurusan di Universitas XYZ
universitas.tampilkan_daftar_jurusan()

# 7. Menampilkan daftar mahasiswa di Jurusan Teknik Informatika di Universitas XYZ
for jurusan in universitas.DaftarJurusan:
    if jurusan.NamaJurusan == "Teknik Informatika":
        jurusan.tampilkan_daftar_mahasiswa()
