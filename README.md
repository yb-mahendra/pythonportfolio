# README
Harap baca ini sebelum Anda melanjutkan menggunakan program ini atau jika Anda mengalami masalah saat menjalankan program ini.

Program ini dibuat sebagai capstone project saya sebagai salah satu syarat kelulusan program Job Connector Business & Data Analitycs di Purwadhika. Program ini membahas tentang pembuatan fungsionalitas CRUD. Jadi ini hanyalah program sederhana untuk membantu saya dalam perjalanan belajar saya mempelajari Product Management, Programming & Data Analitycs.

# Credit Management System (CLI Version)

Program sederhana berbasis teks (Command-Line Interface) yang dirancang untuk mengelola data nasabah kredit pada lembaga keuangan seperti bank atau koperasi. Program ini dibuat sebagai final project untuk pembelajaran Python dasar, khususnya implementasi fitur CRUD (Create, Read, Update, Delete).

## Deskripsi Proyek

Credit Management System memungkinkan pengguna untuk:
- Menyimpan data nasabah dalam bentuk list of dictionaries
- Menambahkan data nasabah baru dengan CIF unik
- Melihat daftar nasabah atau menyaring berdasarkan kriteria tertentu
- Memperbarui data nasabah yang sudah ada
- Menghapus data nasabah
- Menampilkan data dalam bentuk tabel teks tanpa library eksternal (seperti Pandas)

Sistem ini sepenuhnya berbasis teks dan tidak membutuhkan instalasi library tambahan.

---

## Struktur Data Nasabah

Setiap data nasabah disimpan sebagai dictionary dengan atribut sebagai berikut:

| Atribut            | Deskripsi                                                                 |
|--------------------|---------------------------------------------------------------------------|
| `Nomor`            | Nomor urut atau ID nasabah (otomatis bertambah)                          |
| `Nama`             | Nama lengkap nasabah                                                      |
| `CIF`              | Customer Information File, nomor unik 10 digit dimulai dari angka 94      |
| `Jenis Kredit`     | Jenis produk kredit (misalnya: Kredit Modal Kerja, KPR, Multiguna, dll.)  |
| `Maksimum Kredit`  | Limit maksimum pinjaman yang disetujui (dalam Rupiah)                     |
| `No HP`            | Nomor telepon seluler nasabah                                             |
| `Alamat`           | Alamat tempat tinggal nasabah                                             |

---

## Fitur Utama

A. **Navigasi Menu**
   - Interaktif berbasis pilihan angka, mudah digunakan bahkan oleh pengguna awam.
![Tampilan Menu Utama](assets/MENU_7.png)

B. **Tampilkan Daftar Nasabah**
   - Menampilkan seluruh data dalam bentuk tabel.
     
C. **Filter Jenis Kredit**
   - Melihat nasabah berdasarkan jenis kredit tertentu.
     
D. **Filter Maksimum Kredit**
   - Menyaring nasabah dengan maksimum kredit di atas jumlah tertentu.
     
E. **Tambah Data Nasabah**
   - Memasukkan data baru dengan validasi dan CIF unik otomatis.
     
F. **Edit Data Nasabah**
   - Mengubah informasi nasabah berdasarkan nomor urut.
     
G. **Hapus Data Nasabah**
   - Menghapus data nasabah dari sistem.


---

## Cara Menjalankan Program

Pastikan Python sudah terinstal di perangkat Anda. Jalankan file `.py` menggunakan terminal atau command prompt:

```bash
python credit_management.py

