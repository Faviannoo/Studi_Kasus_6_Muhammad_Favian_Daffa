# 📚 Sistem Pencatatan Nilai Mahasiswa

**Sistem Pencatatan Nilai Mahasiswa** merupakan program sederhana berbasis terminal yang dibuat menggunakan Python. Program ini digunakan untuk mencatat dan melihat data nilai mahasiswa.

Data yang dimasukkan disimpan ke dalam file **JSON**, sehingga data tetap dapat digunakan kembali ketika program dijalankan.

---

## 🎯 Tujuan Program

Program ini dibuat untuk mempermudah proses pencatatan nilai mahasiswa secara sederhana. Pengguna dapat:

- Melihat data nilai yang sudah tersimpan.
- Menambahkan data nilai mahasiswa.
- Memeriksa nilai agar berada pada rentang yang sesuai.
- Menyimpan data secara otomatis ke dalam file JSON.
- Mengakhiri program melalui menu yang tersedia.

---

## ⚙️ Fitur Program

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

Pengguna dapat memasukkan data mahasiswa melalui menu **Tambah Data Nilai**.

Data yang perlu dimasukkan yaitu:

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

### 3. Validasi Nilai

Sebelum data disimpan, program melakukan pemeriksaan terhadap nilai.

Nilai tidak boleh kosong dan harus berada di antara **0 sampai 100**.

```python
if nilai == "":
    print("\nNilai tidak boleh kosong!")
    return

nilai = int(nilai)

if nilai < 0 or nilai > 100:
    print("\nNilai harus berada di antara 0 - 100!")
    return
```

Jika nilai tidak sesuai, proses penambahan data dihentikan dan data tidak disimpan.

---

### 4. Penyimpanan Data JSON

Data mahasiswa disimpan dalam file:

```text
nilai_mahasiswa.json
```

Program menggunakan modul `json` untuk membaca dan menyimpan data.

Fungsi penyimpanan data:

```python
def simpan_data(data):
    with open(nama_file, "w") as file:
        json.dump(data, file, indent=4)
```

Penggunaan `indent=4` membuat isi file JSON lebih rapi dan mudah dibaca.

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

## 🗂️ Struktur Data

Data yang digunakan berupa **list** yang berisi beberapa **dictionary**.

Gambaran sederhananya:

```text
List
│
├── Data Mahasiswa 1
│   ├── Nama
│   ├── NIM
│   ├── Mata Kuliah
│   └── Nilai
│
├── Data Mahasiswa 2
│   ├── Nama
│   ├── NIM
│   ├── Mata Kuliah
│   └── Nilai
│
└── dan seterusnya
```

Contoh isi file JSON:

```json
[
    {
        "nim": "230101",
        "nama": "Andi",
        "matkul": "Algoritma",
        "nilai": 85
    }
]
```

---

## 🔧 Fungsi yang Digunakan

| Fungsi | Kegunaan |
|---|---|
| `baca_data()` | Mengambil data dari file JSON |
| `simpan_data(data)` | Menyimpan perubahan data ke file JSON |
| `tampilkan_data()` | Menampilkan data mahasiswa |
| `tambah_data()` | Memasukkan dan menyimpan data mahasiswa baru |

---

## 📁 Struktur File

```text
Project/
│
├── program.py
└── nilai_mahasiswa.json
```

`program.py` merupakan file utama yang menjalankan program, sedangkan `nilai_mahasiswa.json` digunakan sebagai tempat penyimpanan data.

---

## 🖥️ Tampilan Program

### Menu Utama

```text
==============================
 SISTEM PENCATATAN NILAI
==============================
1. Tampilkan Data Nilai
2. Tambah Data Nilai
3. Keluar
Pilih menu:
```

### Input Data

```text
=== TAMBAH NILAI MAHASISWA ===
Nama : Andi
NIM : 230101
Mata Kuliah : Algoritma
Nilai : 85

Data berhasil ditambahkan dan disimpan.
```

### Hasil Data

```text
=== DATA NILAI MAHASISWA ===
Nama        : Andi
NIM         : 230101
Mata Kuliah : Algoritma
Nilai       : 85
------------------------
```

### Validasi Nilai

Jika pengguna memasukkan nilai di luar batas:

```text
Nilai : 120

Nilai harus berada di antara 0 - 100!
```

Jika nilai tidak diisi:

```text
Nilai :

Nilai tidak boleh kosong!
```

---

## 🛠️ Teknologi yang Digunakan

- **Python** — bahasa pemrograman utama.
- **JSON** — digunakan sebagai media penyimpanan data.
- **VS Code** — digunakan untuk menulis dan menjalankan program.
- **GitHub** — digunakan untuk menyimpan project.

### Library

Program menggunakan modul bawaan Python:

```python
import json
import os
```

Modul `json` digunakan untuk membaca dan menyimpan data. Modul `os` sudah diimpor pada program, tetapi pada versi kode ini belum digunakan dalam proses utama.

---

## 📌 Alur Singkat Program

```text
Mulai
  ↓
Tampilkan Menu
  ↓
Pilih Menu
  ├── 1 → Baca Data JSON → Tampilkan Data
  │
  ├── 2 → Input Data
  │        ↓
  │      Validasi Nilai
  │        ↓
  │      Simpan ke JSON
  │
  └── 3 → Keluar
           ↓
        Program Selesai
```

---

## 📌 Kesimpulan

Program **Sistem Pencatatan Nilai Mahasiswa** merupakan program sederhana yang menerapkan penggunaan fungsi, list, dictionary, perulangan, percabangan, input pengguna, validasi data, serta penyimpanan menggunakan JSON.

Program ini masih dapat dikembangkan dengan menambahkan fitur lain seperti mengubah data, menghapus data, mencari mahasiswa, atau menghitung grade berdasarkan nilai.
