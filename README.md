# Code Convention - PPPL

## Federico Matthew Pratama - 233405001

### Project : Contact (Python)

Dalam Project ini terdapat :

- Contact List (Ascending)
- Contact List (Descending)
- Contact Details
- Add Contact
- Edit Contact
- Delete Contact
- Search Contact

## Deskripsi Project

Project ini adalah aplikasi manajemen kontak yang dibuat menggunakan Python. Aplikasi ini memungkinkan pengguna untuk mengelola daftar kontak dengan berbagai fitur yang lengkap. Data kontak disimpan dalam bentuk **List of Dictionaries**.

## Struktur Data

Setiap kontak disimpan dalam bentuk **Dictionary** dengan struktur sebagai berikut:

```python
{
    "name": "Nama Kontak",
    "email": "email@example.com",
    "phone": "nomor_telepon"
}
```

**Data Dictionary yang digunakan dalam project:**

```python
contacts = [
    {
        "name": "Mashu",
        "email": "federicomatthewpratamaa@gmail.com",
        "phone": "00000"
    },
    {
        "name": "Arthur",
        "email": "arthur@gmail.com",
        "phone": "2221112"
    },
    {
        "name": "Badut",
        "email": "anjingkaubadutbeban@gmail.com",
        "phone": "12121131"
    },
    {
        "name": "Jefferey",
        "email": "jeffereymonyet@gmail.com",
        "phone": "12345"
    }
]
```

**Tipe Data:**

- `contacts`: `List[Dict]` - List yang berisi dictionary kontak
- Setiap kontak: `Dict` dengan keys: `name`, `email`, `phone` (semua bertipe `str`)

## Fitur Utama

### 1. Contact List (Ascending)

Menampilkan daftar kontak dalam urutan naik (A-Z) berdasarkan nama.

### 2. Contact List (Descending)

Menampilkan daftar kontak dalam urutan turun (Z-A) berdasarkan nama.

### 3. Contact Details

Menampilkan detail lengkap dari kontak yang dipilih, termasuk nama, email, dan nomor telepon.

### 4. Add Contact

Menambahkan kontak baru ke dalam daftar dengan memasukkan nama, email, dan nomor telepon.

### 5. Edit Contact

Mengubah atau memperbarui informasi kontak yang sudah ada dalam daftar.

### 6. Delete Contact

Menghapus kontak dari daftar berdasarkan pilihan pengguna.

### 7. Search Contact

Mencari kontak berdasarkan nama atau nomor telepon.

## Cara Menjalankan

```bash
python main.py
```

## Requirements

- Python 3.x
- Module `typing` untuk type hints (`List[Dict]`)

## Struktur Project

```
CODE_CONVENTION/
├── main.py          # File utama untuk menjalankan aplikasi
├── function.py      # Modul berisi semua fungsi untuk mengelola kontak
└── README.md        # Dokumentasi project
```

## Author

Federico Matthew Pratama - 233405001
