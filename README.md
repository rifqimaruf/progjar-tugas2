# Pemrograman Jaringan - Tugas 2: Concurrent Time Server

Repositori ini berisi implementasi untuk Tugas 2 dari mata kuliah Pemrograman Jaringan. Proyek ini berfokus pada pembuatan sebuah server waktu (Time Server) yang mampu menangani beberapa koneksi client secara bersamaan (konkuren) menggunakan multithreading.

## Deskripsi Tugas

Tujuan utama dari tugas ini adalah untuk membangun sebuah aplikasi client-server dengan spesifikasi sebagai berikut:
-   **Server:** Sebuah server TCP yang berjalan di port `45000`.
-   **Konkurensi:** Server harus dapat melayani banyak client secara simultan. Ini diimplementasikan menggunakan arsitektur **thread-per-connection**.
-   **Protokol Aplikasi:** Sebuah protokol sederhana berbasis teks didefinisikan untuk komunikasi:
    -   Client mengirim `TIME\r\n` untuk meminta waktu saat ini.
    -   Server merespons dengan format `JAM hh:mm:ss\r\n`.
    -   Client mengirim `QUIT\r\n` untuk mengakhiri sesi koneksi.

## Arsitektur & Implementasi

Solusi ini diimplementasikan menggunakan pendekatan Object-Oriented Programming (OOP) di Python untuk meningkatkan keterbacaan dan struktur kode.

### `server_tugas2_oop.py`
Server dibangun dengan dua kelas utama:
1.  `TimeServer(threading.Thread)`: Kelas ini bertindak sebagai *listener* utama. Tugasnya adalah menerima koneksi masuk pada port yang ditentukan dan mendelegasikan setiap koneksi baru ke sebuah thread pekerja.
2.  `ClientThread(threading.Thread)`: Kelas ini adalah *handler* untuk setiap client. Setiap instance dari kelas ini berjalan di thread-nya sendiri dan bertanggung jawab penuh untuk menangani seluruh siklus komunikasi dengan satu client, mulai dari membaca perintah hingga mengirim respons dan menutup koneksi.

Model **thread-per-connection** ini memungkinkan server untuk tetap responsif dan siap menerima koneksi baru, bahkan saat sedang aktif melayani client lain.

### `client_tugas2.py`
Sebuah program client sederhana yang digunakan untuk menguji fungsionalitas server. Client ini memungkinkan pengguna untuk mengirim perintah `TIME` atau `QUIT` secara interaktif dan menampilkan respons dari server.

## Pembuktian Konkurensi

Kemampuan server untuk menangani koneksi secara konkuren dibuktikan dengan menjalankan dua atau lebih instance `client_tugas2.py` dari mesin yang berbeda (Mesin-2 dan Mesin-3) secara bersamaan. Hasil pengujian menunjukkan bahwa:
-   Client kedua dapat terhubung dan mendapatkan respons dari server tanpa harus menunggu client pertama memutuskan koneksi.
-   Log pada terminal server menunjukkan pembuatan thread baru untuk setiap koneksi yang masuk, yang mengkonfirmasi bahwa setiap client dilayani secara paralel.

Ini secara efektif menunjukkan keunggulan model multithreading dibandingkan model iteratif (seperti pada Tugas 1) dalam menangani banyak pengguna.

## Cara Menjalankan

1.  **Siapkan Lingkungan:** Pastikan lingkungan lab Docker dengan tiga mesin (mesin-1, mesin-2, mesin-3) sudah berjalan.
2.  **Clone Repositori:** Clone repositori (https://github.com/rm77/progjar) ke dalam direktori `work/` pada setiap mesin.
3.  **Jalankan Server:** Di terminal **Mesin-1**, jalankan server:
    ```bash
    python3 server_tugas2_oop.py
    ```
4.  **Jalankan Client:** Di terminal **Mesin-2** dan **Mesin-3**, jalankan client:
    ```bash
    python3 client_tugas2.py
    ```
5.  **Interaksi:** Ketik `TIME` untuk meminta waktu atau `QUIT` untuk keluar pada terminal client.

**Nama:** Muhammad Rifqi Ma'ruf  
**NRP:** 5025221060  