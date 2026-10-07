# Studi Kasus 6 Muhammad Favian Daffa
# Sistem Pencatatan Nilai Mahasiswa

Merupakan program sederhana yang digunakan untuk mencatat dan melihat data nilai mahasiswa. Data yang dimasukkan disimpan ke dalam file **JSON**, sehingga data tetap dapat digunakan kembali ketika program dijalankan.

---

# Fitur Program

### 1. Menampilkan Data

Program dapat membaca data yang terdapat pada `nilai_mahasiswa.json` kemudian menampilkannya ke layar.

Data yang ditampilkan meliputi:

- Nama mahasiswa
- NIM
- Mata kuliah
- Nilai

Jika belum ada data yang tersimpan, program akan menampilkan pesan bahwa data nilai belum tersedia.

Contoh kode:

```python
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
```

---

### 2. Menambahkan Data

Pengguna dapat memasukkan data mahasiswa melalui menu **Tambah Data Nilai**. Data yang perlu dimasukkan yaitu:

```text
Nama
NIM
Mata Kuliah
Nilai
```

Data tersebut kemudian dibuat menjadi sebuah dictionary.

```python
data_baru = {
    "nim": nim,
    "nama": nama,
    "matkul": matkul,
    "nilai": nilai
}
```

Setelah dibuat, data dimasukkan ke dalam list menggunakan `append()`.

```python
data.append(data_baru)
```

---

### 3. Validasi Data

Sebelum data disimpan, program melakukan pemeriksaan terhadap data. Nama, Nim, Matkul dan Nilai tidak boleh kosong serta Nilai harus berada di antara 0 sampai 100.

```python
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
```

Jika data tidak sesuai, proses penambahan data dihentikan dan data tidak disimpan.

---

### 4. Penyimpanan Data JSON

Data mahasiswa disimpan dalam file:

```text
nilai_mahasiswa.json
```

Program menggunakan `json` untuk membaca dan menyimpan data.

Fungsi penyimpanan data:

```python
def simpan_data(data):
    with open(nama_file, "w") as file:
        json.dump(data, file, indent=4)
```
---

### 5. Menu Berulang

Program menggunakan `while True` agar menu dapat digunakan secara berulang.

Menu yang tersedia:

```text
1. Tampilkan Data Nilai
2. Tambah Data Nilai
3. Keluar
```

Program akan terus berjalan sampai pengguna memilih menu **3. Keluar**.

```python
while True:
    print("\n==============================")
    print(" SISTEM PENCATATAN NILAI")
    print("==============================")
    print("1. Tampilkan Data Nilai")
    print("2. Tambah Data Nilai")
    print("3. Keluar")
```

---


---

# Fungsi yang Digunakan

| Fungsi | Kegunaan |
|---|---|
| `baca_data()` | Mengambil data dari file JSON |
| `simpan_data(data)` | Menyimpan perubahan data ke file JSON |
| `tampilkan_data()` | Menampilkan data mahasiswa |
| `tambah_data()` | Memasukkan dan menyimpan data mahasiswa baru |

---
