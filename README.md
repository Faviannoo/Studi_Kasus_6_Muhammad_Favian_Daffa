# Studi Kasus 6 Muhammad Favian Daffa

# Sistem Pencatatan Nilai Mahasiswa

Program sederhana untuk **mencatat dan melihat data nilai mahasiswa**. Data yang dimasukkan disimpan ke dalam file **JSON**, sehingga data tetap tersimpan dan dapat digunakan kembali ketika program dijalankan.

---

## Fitur Program

Program memiliki beberapa fitur utama:

1. **Tampilkan Data Nilai**
2. **Tambah Data Nilai**
3. **Keluar dari Program**
4. **Validasi Data Kosong**
5. **Validasi Nilai 0–100**
6. **Penyimpanan Data Menggunakan JSON**

---

## 1. Import Library dan Data Awal

Bagian ini merupakan awal program. Library `json` digunakan untuk membaca dan menyimpan data dalam format JSON. Variabel `nama_file` digunakan untuk menentukan nama file tempat data mahasiswa disimpan.

```python
import json
import os

nama_file = "nilai_mahasiswa.json"
```

---

## 2. Function `baca_data()`

Function ini digunakan untuk membaca data mahasiswa yang tersimpan di dalam file `nilai_mahasiswa.json`. Data yang telah dibaca kemudian dikembalikan menggunakan `return`.

```python
def baca_data():
    with open(nama_file, "r") as file:
        data = json.load(file)
    return data
```

---

## 3. Function `simpan_data()`

Function ini digunakan untuk menyimpan data mahasiswa ke dalam file JSON. `json.dump()` digunakan untuk menulis data ke file, sedangkan `indent=4` digunakan agar isi file JSON lebih rapi.

```python
def simpan_data(data):
    with open(nama_file, "w") as file:
        json.dump(data, file, indent=4)
```

---

## 4. Function `tampilkan_data()`

Function ini digunakan untuk menampilkan data nilai mahasiswa. Program membaca data menggunakan `baca_data()`. Jika data masih kosong, program menampilkan pesan bahwa belum ada data. Jika data tersedia, program menampilkan setiap data menggunakan perulangan `for`.

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

## 5. Function `tambah_data()`

Function ini digunakan untuk menambahkan data mahasiswa baru. Pengguna memasukkan nama, NIM, mata kuliah, dan nilai.

```python
def tambah_data():
    print("\n=== TAMBAH NILAI MAHASISWA ===")
    nama = input("Nama : ")
    nim = input("NIM : ")
    matkul = input("Mata Kuliah : ")
    nilai = input("Nilai : ")
```

### Validasi Data

Program memeriksa agar nama, NIM, mata kuliah, dan nilai tidak boleh kosong.

```python
if nama == "" or nim == "" or matkul == "":
    print("\nData tidak boleh kosong!")
    return

if nilai == "":
    print("\nNilai tidak boleh kosong!")
    return
```

### Validasi Nilai

Nilai kemudian diubah menjadi angka dan diperiksa agar berada pada rentang 0 sampai 100.

```python
nilai = int(nilai)

if nilai < 0 or nilai > 100:
    print("\nNilai harus berada di antara 0 - 100!")
    return
```

### Menyimpan Data

Jika data sudah benar, program membuat dictionary baru kemudian memasukkannya ke dalam list dan menyimpannya ke file JSON.

```python
data = baca_data()

data_baru = {
    "nama": nama,
    "nim": nim,
    "matkul": matkul,
    "nilai": nilai
}

data.append(data_baru)
simpan_data(data)

print("\nData berhasil ditambahkan dan disimpan.")
```

---

## 6. Program Utama

Bagian ini merupakan bagian utama program. `while True` digunakan agar menu terus berjalan sampai pengguna memilih menu keluar.

```python
while True:
    print("\n==============================")
    print(" SISTEM PENCATATAN NILAI")
    print("==============================")
    print("1. Tampilkan Data Nilai")
    print("2. Tambah Data Nilai")
    print("3. Keluar")
```

Pilihan pengguna diproses menggunakan `if`, `elif`, dan `else`.

```python
pilihan = input("Pilih menu: ")

if pilihan == "1":
    tampilkan_data()
elif pilihan == "2":
    tambah_data()
elif pilihan == "3":
    print("\nProgram selesai.")
    break
else:
    print("\nPilihan tidak tersedia.")
```

Setelah menjalankan menu, pengguna diminta menekan Enter untuk kembali ke menu utama.

```python
input("\nTekan Enter untuk melanjutkan...")
```

---

# Fungsi yang Digunakan

| Function            | Kegunaan                         |
| ------------------- | -------------------------------- |
| `baca_data()`       | Membaca data dari file JSON      |
| `simpan_data(data)` | Menyimpan data ke file JSON      |
| `tampilkan_data()`  | Menampilkan data nilai mahasiswa |
| `tambah_data()`     | Menambahkan data mahasiswa baru  |

---

# Struktur Data

Data mahasiswa disimpan dalam bentuk **list yang berisi dictionary**.

Contoh:

```json
[
    {
        "nama": "Favian",
        "nim": "021",
        "matkul": "DDPWANGI",
        "nilai": 100
    }
]
```

---

# Menu Program

```text
==============================
 SISTEM PENCATATAN NILAI
==============================
1. Tampilkan Data Nilai
2. Tambah Data Nilai
3. Keluar
Pilih menu:
```

---

# Contoh Output
