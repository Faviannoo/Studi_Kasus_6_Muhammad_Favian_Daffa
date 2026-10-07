import json
import os

nama_file = "nilai_mahasiswa.json"

# FUNCTION MEMBACA DATA
def baca_data():
    with open(nama_file, "r") as file:
        data = json.load(file)
    return data

# FUNCTION MENYIMPAN DATA
def simpan_data(data):
    with open(nama_file, "w") as file:
        json.dump(data, file, indent=4)

# FUNCTION MENAMPILKAN DATA
def tampilkan_data():
    data = baca_data()
    print("\n=== DATA NILAI MAHASISWA ===")
    if data == []:
        print("Belum ada data nilai.")
    else:
        for mahasiswa in data:
            print("Nama        :", mahasiswa["nama"])
            print("NIM         :", mahasiswa["nim"])
            print("Mata Kuliah :", mahasiswa["matkul"])
            print("Nilai       :", mahasiswa["nilai"])
            print("------------------------")

# FUNCTION MENAMBAH DATA
def tambah_data():
    print("\n=== TAMBAH NILAI MAHASISWA ===")
    nama = input("Nama : ")
    nim = input("NIM : ")
    matkul = input("Mata Kuliah : ")
    nilai = input("Nilai : ")

    if nama == "" or nim == "" or matkul == "":
        print("\nData tidak boleh kosong!")
        return

    if nilai == "":
        print("\nNilai tidak boleh kosong!")
        return

    nilai = int(nilai)
    if nilai < 0 or nilai > 100:
        print("\nNilai harus berada di antara 0 - 100!")
        return
    data = baca_data()
    data_baru = {
        "nim": nim,
        "nama": nama,
        "matkul": matkul,
        "nilai": nilai
    }

    data.append(data_baru)
    simpan_data(data)
    print("\nData berhasil ditambahkan dan disimpan.")

# PROGRAM UTAMA
while True:
    print("\n==============================")
    print(" SISTEM PENCATATAN NILAI")
    print("==============================")
    print("1. Tampilkan Data Nilai")
    print("2. Tambah Data Nilai")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        print("\nProgram selesai")
        break
    else:
        print("\nPilihan tidak tersedia.")
    input("\nTekan Enter untuk melanjutkan...")