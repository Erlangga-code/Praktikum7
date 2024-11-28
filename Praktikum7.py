def hitung_nilai_akhir(tugas, uts, uas):
    """Hitung nilai akhir berdasarkan bobot tugas, UTS, dan UAS"""
    return 0.3 * tugas + 0.35 * uts + 0.35 * uas

def tambah_data(data_mahasiswa):
    """Tambah data mahasiswa baru"""
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    data_mahasiswa[nim] = {'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas, 'nilai_akhir': nilai_akhir}
    print("Data mahasiswa berhasil ditambahkan.")

def ubah_data(data_mahasiswa):
    """Ubah data mahasiswa"""
    nim = input("Masukkan NIM yang ingin diubah: ")
    if nim in data_mahasiswa:
        tugas = float(input("Masukkan Nilai Tugas baru: "))
        uts = float(input("Masukkan Nilai UTS baru: "))
        uas = float(input("Masukkan Nilai UAS baru: "))
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        data_mahasiswa[nim] = {'nama': data_mahasiswa[nim]['nama'], 'tugas': tugas, 'uts': uts, 'uas': uas, 'nilai_akhir': nilai_akhir}
        print("Data mahasiswa berhasil diubah.")
    else:
        print("NIM tidak ditemukan.")

def hapus_data(data_mahasiswa):
    """Hapus data mahasiswa"""
    nim = input("Masukkan NIM yang ingin dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("NIM tidak ditemukan.")

def tampilkan_data(data_mahasiswa):
    """Tampilkan data mahasiswa dalam bentuk tabel"""
    print("Daftar Nilai")
    print("| No | NIM      | Nama       | Tugas | UTS | UAS | Akhir |")
    print("------------------------------------------------------")
    no = 1
    for nim, nilai in data_mahasiswa.items():
        print(f"| {no:1.0f} | {nim:8s} | {nilai['nama']:10s} | {nilai['tugas']:2.0f} | {nilai['uts']:2.0f} | {nilai['uas']:2.0f} | {nilai['nilai_akhir']:5.2f} |")
        no += 1

def cari_data(data_mahasiswa):
    """Cari data mahasiswa berdasarkan NIM"""
    nim = input("Masukkan NIM yang ingin dicari: ")
    if nim in data_mahasiswa:
        print(data_mahasiswa[nim])
    else:
        print("NIM tidak ditemukan.")

if __name__ == "__main__":
    data_mahasiswa = {}
    while True:
        print("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ", end="")
        pilihan = input().lower()
        if pilihan == 'l':
            tampilkan_data(data_mahasiswa)
        elif pilihan == 't':
            tambah_data(data_mahasiswa)
        elif pilihan == 'u':
            ubah_data(data_mahasiswa)
        elif pilihan == 'h':
            hapus_data(data_mahasiswa)
        elif pilihan == 'c':
            cari_data(data_mahasiswa)
        elif pilihan == 'k':
            break
        else:
            print("Pilihan tidak valid.")
