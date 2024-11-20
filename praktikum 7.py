mahasiswa = {}
pilihan = ""

def tambah_data():
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    nilai_tugas = float(input("Masukkan nilai tugas: "))
    nilai_uts = float(input("Masukkan nilai UTS: "))
    nilai_uas = float(input("Masukkan nilai UAS: "))
    nilai_akhir = nilai_tugas * 0.3 + nilai_uts * 0.35 + nilai_uas * 0.35
    mahasiswa[nim] = {'Nama': nama, 'Nilai Tugas': nilai_tugas, 'Nilai UTS': nilai_uts, 'Nilai UAS': nilai_uas, 'Nilai Akhir': nilai_akhir}
    print("Data berhasil ditambahkan!")

def ubah_data():
    nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
    if nim in mahasiswa:
        nama = input("Masukkan nama baru: ")
        nilai_tugas = float(input("Masukkan nilai tugas baru: "))
        nilai_uts = float(input("Masukkan nilai UTS baru: "))
        nilai_uas = float(input("Masukkan nilai UAS baru: "))
        nilai_akhir = nilai_tugas * 0.3 + nilai_uts * 0.35 + nilai_uas * 0.35
        mahasiswa[nim] = {'Nama': nama, 'Nilai Tugas': nilai_tugas, 'Nilai UTS': nilai_uts, 'Nilai UAS': nilai_uas, 'Nilai Akhir': nilai_akhir}
        print("Data berhasil diubah!")
    else:
        print("NIM tidak ditemukan!")

def hapus_data():
    nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
    if nim in mahasiswa:
        del mahasiswa[nim]
        print("Data berhasil dihapus!")
    else:
        print("NIM tidak ditemukan!")

def tampilkan_data():
    if not mahasiswa:
        print("Tidak ada data mahasiswa")
    else:
        print("No\tNama\tNIM\tTugas\tUTS\tUAS\tAkhir")
        for i, (nim, data) in enumerate(mahasiswa.items(), start=1):
            print(f"{i}\t{data['Nama']}\t{nim}\t{data['Nilai Tugas']:.2f}\t{data['Nilai UTS']:.2f}\t{data['Nilai UAS']:.2f}\t{data['Nilai Akhir']:.2f}")

def cari_data():
    nim = input("Masukkan NIM mahasiswa yang ingin dicari: ")
    if nim in mahasiswa:
        data = mahasiswa[nim]
        print(f"Nama: {data['Nama']}")
        print(f"Nilai Tugas: {data['Nilai Tugas']}")
        print(f"Nilai UTS: {data['Nilai UTS']}")
        print(f"Nilai UAS: {data['Nilai UAS']}")
        print(f"Nilai Akhir: {data['Nilai Akhir']}")
    else:
        print("NIM tidak ditemukan!")

while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        ubah_data()
    elif pilihan == '3':
        hapus_data()
    elif pilihan == '4':
        tampilkan_data()
    elif pilihan == '5':
        cari_data()
    elif pilihan == '6':
        break
    else:
        print("Pilihan tidak valid!")
