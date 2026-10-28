# PROPOSAL PROYEK

# GENERATOR DAN EVALUASI SOAL OPERASI HITUNG CAMPURAN

## Identitas Mahasiswa

* Nama: Suchita Rahma Fakhira
* NIM: 2225250006
* Kelas: 3B

## 1. Judul Proyek

Generator dan Evaluasi Soal Operasi Hitung Campuran.

## 2. Latar Belakang

Operasi hitung campuran merupakan materi matematika yang melibatkan beberapa operasi aritmetika, seperti penjumlahan, pengurangan, perkalian, dan pembagian. Dalam menyelesaikan soal operasi hitung campuran, siswa perlu memahami urutan pengerjaan operasi agar memperoleh hasil yang benar.

Dalam proses pembelajaran, siswa membutuhkan latihan soal yang bervariasi untuk meningkatkan pemahaman dan keterampilan berhitung. Oleh karena itu, dirancang program sederhana menggunakan bahasa pemrograman Python yang dapat menghasilkan soal operasi hitung campuran serta mengevaluasi jawaban pengguna.

Program ini diharapkan dapat membantu pengguna berlatih secara mandiri, mengetahui kebenaran jawaban, dan memahami hasil evaluasi dari latihan yang dikerjakan. Program dikembangkan dengan struktur modul agar kode lebih terorganisasi dan mudah dipelihara.

## 3. Pengguna dan Tujuan

### 3.1 Pengguna

Pengguna utama program ini adalah siswa atau pengguna yang ingin berlatih menyelesaikan soal operasi hitung campuran.

### 3.2 Tujuan

1. Membantu pengguna berlatih mengerjakan soal operasi hitung campuran.
2. Menghasilkan soal latihan sesuai kemampuan program.
3. Menghitung jawaban yang benar berdasarkan aturan operasi matematika.
4. Memeriksa kebenaran jawaban yang dimasukkan pengguna.
5. Menampilkan hasil evaluasi latihan secara jelas.

## 4. Ruang Lingkup

### 4.1 Fitur Wajib

1. Program menghasilkan soal operasi hitung campuran.
2. Program menampilkan soal kepada pengguna.
3. Program memproses perhitungan operasi hitung campuran.
4. Program menerima jawaban pengguna sesuai mekanisme input yang diterapkan.
5. Program mengevaluasi jawaban pengguna.
6. Program menampilkan hasil evaluasi.

### 4.2 Fitur Tambahan

Program dapat dikembangkan dengan menambahkan pembahasan langkah penyelesaian soal, penyimpanan hasil latihan, atau variasi tingkat kesulitan apabila fitur tersebut sesuai dengan implementasi dan waktu pengembangan.

### 4.3 Batasan Proyek

1. Program dikembangkan menggunakan bahasa pemrograman Python.
2. Program dirancang sebagai aplikasi sederhana.
3. Soal berfokus pada operasi hitung campuran.
4. Hasil perhitungan harus mengikuti aturan prioritas operasi matematika.
5. Program menangani masukan yang tidak valid sesuai kemampuan implementasinya.
6. Program tidak menggunakan database atau layanan eksternal dalam rancangan dasar.
7. Fitur yang tersedia dibatasi pada fungsi yang dikembangkan dalam proyek.

## 5. Analisis Kebutuhan

### 5.1 Kebutuhan Fungsional

<table>
    <tr>
        <th>ID</th>
        <th>Kebutuhan</th>
        <th>Prioritas</th>
    </tr>
    <tr>
        <td>F01</td>
        <td>Program dapat menghasilkan soal operasi hitung campuran.</td>
        <td>Wajib</td>
    </tr>
    <tr>
        <td>F02</td>
        <td>Program dapat memproses perhitungan soal.</td>
        <td>Wajib</td>
    </tr>
    <tr>
        <td>F03</td>
        <td>Program dapat menentukan jawaban yang benar.</td>
        <td>Wajib</td>
    </tr>
    <tr>
        <td>F04</td>
        <td>Program dapat mengevaluasi jawaban pengguna.</td>
        <td>Wajib</td>
    </tr>
    <tr>
        <td>F05</td>
        <td>Program dapat menampilkan hasil evaluasi.</td>
        <td>Wajib</td>
    </tr>
    <tr>
        <td>F06</td>
        <td>Program dapat menangani masukan yang tidak valid.</td>
        <td>Wajib</td>
    </tr>
</table>

### 5.2 Kebutuhan Nonfungsional

1. Program dapat dijalankan menggunakan Python.
2. Kode program disusun dalam beberapa modul agar mudah dipahami.
3. Nama fungsi dan variabel menggambarkan kegunaannya dengan jelas.
4. Program memberikan keluaran yang mudah dipahami pengguna.
5. Program dapat diuji menggunakan skenario pengujian yang telah disusun.
6. Program dapat dikembangkan dan diperbaiki tanpa mengubah keseluruhan struktur program.

## 6. IPO (Input, Process, Output)

### 6.1 Input

1. Masukan atau pilihan pengguna untuk menjalankan latihan sesuai fitur program.
2. Jawaban pengguna apabila program meminta jawaban.
3. Data atau parameter yang diperlukan untuk menghasilkan soal.

### 6.2 Process

1. Program menerima masukan yang diperlukan.
2. Program memvalidasi masukan apabila diperlukan.
3. Program menghasilkan soal operasi hitung campuran.
4. Program menentukan hasil perhitungan yang benar.
5. Program menampilkan soal kepada pengguna.
6. Program menerima jawaban pengguna sesuai alur program.
7. Program membandingkan jawaban pengguna dengan jawaban yang benar.
8. Program menghitung hasil evaluasi.
9. Program menampilkan hasil pengolahan.

### 6.3 Output

1. Soal operasi hitung campuran.
2. Hasil perhitungan yang benar.
3. Informasi hasil pemeriksaan jawaban.
4. Hasil evaluasi latihan sesuai fitur yang tersedia.

## 7. Algoritma

### 7.1 Pseudocode

MULAI
Tampilkan judul program
Siapkan proses pembuatan soal
Hasilkan soal operasi hitung campuran
Tentukan jawaban yang benar
berdasarkan aturan operasi matematika
Tampilkan soal kepada pengguna
Terima jawaban pengguna
Periksa validitas jawaban
JIKA jawaban tidak valid
    Tampilkan pesan kesalahan
    Minta jawaban yang valid
SELESAI JIKA
Bandingkan jawaban pengguna
dengan jawaban yang benar
JIKA jawaban pengguna sama dengan jawaban benar
    Tampilkan informasi bahwa jawaban benar
JIKA TIDAK
    Tampilkan informasi bahwa jawaban salah
SELESAI JIKA
Tampilkan hasil evaluasi
SELESAI

Pseudocode tersebut merupakan gambaran umum alur program. Detail algoritma disesuaikan dengan fungsi dan mekanisme yang diterapkan pada kode Python.

### 7.2 Dasar Evaluasi

Evaluasi dilakukan dengan membandingkan jawaban pengguna dengan jawaban yang benar dari soal yang dihasilkan program.

Apabila program menggunakan nilai atau skor untuk menilai latihan, perhitungannya harus mengikuti mekanisme penilaian yang benar-benar diterapkan dalam implementasi.

## 8. Struktur Program

Struktur folder proyek disusun berdasarkan rancangan program sederhana dan disesuaikan dengan file yang tersedia.

proyek-akhir-Suchita-Rahma-Fakhira/
|
|-- README.md
|-- proposal.md
|-- .gitignore
|
|-- src/
|   |-- main.py
|   |-- data_io.py
|   |-- analisis.py
|   `-- utilitas.py
|
|-- tests/
|   `-- test_case.md
|
`-- output/
    `-- .gitkeep

### 8.1 Tanggung Jawab Modul

* main.py: mengatur alur utama program dan menghubungkan fungsi dari modul lainnya.
* data_io.py: menangani proses masukan dan keluaran data sesuai kebutuhan program.
* analisis.py: menangani proses analisis, perhitungan, atau evaluasi soal sesuai implementasi.
* utilitas.py: menyediakan fungsi pendukung yang digunakan oleh modul lain.
* tests/test_case.md: mendokumentasikan skenario pengujian dan hasil yang diharapkan.
* README.md: menjelaskan deskripsi, tujuan, fitur, struktur, dan cara menjalankan proyek.
* proposal.md: menyimpan dokumen rancangan proyek.
* .gitignore: menentukan file atau folder yang tidak perlu dimasukkan ke Git.
* output/.gitkeep: menjaga agar folder output tetap tercatat dalam repository.

## 9. Struktur Data

<table>
    <tr>
        <th>Struktur Data</th>
        <th>Penggunaan</th>
        <th>Alasan</th>
    </tr>
    <tr>
        <td>Integer</td>
        <td>Menyimpan bilangan bulat yang digunakan dalam soal dan hasil perhitungan.</td>
        <td>Sesuai untuk operasi aritmetika bilangan bulat.</td>
    </tr>
    <tr>
        <td>String</td>
        <td>Menyimpan teks soal, pesan, dan informasi yang ditampilkan kepada pengguna.</td>
        <td>Memudahkan penyajian informasi.</td>
    </tr>
    <tr>
        <td>Variabel numerik</td>
        <td>Menampung operand, jawaban, dan hasil perhitungan.</td>
        <td>Memudahkan proses perhitungan matematika.</td>
    </tr>
    <tr>
        <td>Boolean</td>
        <td>Menyatakan kondisi benar atau salah apabila digunakan dalam pemeriksaan jawaban.</td>
        <td>Memudahkan pengambilan keputusan.</td>
    </tr>
    <tr>
        <td>List atau Dictionary</td>
        <td>Menyimpan kumpulan soal atau informasi soal apabila diterapkan dalam kode.</td>
        <td>Memudahkan pengelompokan dan pengolahan data.</td>
    </tr>
</table>

## 10. Test Case

<table>
    <tr>
        <th>ID</th>
        <th>Kategori</th>
        <th>Input/Kondisi</th>
        <th>Hasil yang Diharapkan</th>
    </tr>
    <tr>
        <td>TC01</td>
        <td>Normal</td>
        <td>Ekspresi 2 + 3 * 4</td>
        <td>Hasil perhitungan adalah 14 sesuai prioritas perkalian.</td>
    </tr>
    <tr>
        <td>TC02</td>
        <td>Normal</td>
        <td>Ekspresi (2 + 3) * 4</td>
        <td>Hasil perhitungan adalah 20 karena operasi dalam tanda kurung dikerjakan terlebih dahulu.</td>
    </tr>
    <tr>
        <td>TC03</td>
        <td>Normal</td>
        <td>Ekspresi 10 - 2 * 3</td>
        <td>Hasil perhitungan adalah 4.</td>
    </tr>
    <tr>
        <td>TC04</td>
        <td>Batas</td>
        <td>Ekspresi 5 - 5</td>
        <td>Hasil perhitungan adalah 0.</td>
    </tr>
    <tr>
        <td>TC05</td>
        <td>Invalid</td>
        <td>Ekspresi 5 / 0</td>
        <td>Program menangani kesalahan pembagian dengan nol dan tidak memperlakukannya sebagai hasil valid.</td>
    </tr>
    <tr>
        <td>TC06</td>
        <td>Invalid</td>
        <td>Masukan berupa teks yang tidak sesuai dengan format yang diterima program.</td>
        <td>Program menolak atau menangani masukan tersebut sesuai implementasinya.</td>
    </tr>
    <tr>
        <td>TC07</td>
        <td>Evaluasi</td>
        <td>Jawaban pengguna sama dengan hasil yang benar.</td>
        <td>Program menandai jawaban sebagai benar.</td>
    </tr>
    <tr>
        <td>TC08</td>
        <td>Evaluasi</td>
        <td>Jawaban pengguna berbeda dari hasil yang benar.</td>
        <td>Program menandai jawaban sebagai salah.</td>
    </tr>
</table>

## 11. Pembagian Tugas

<table>
    <tr>
        <th>Peran</th>
        <th>Tanggung Jawab</th>
    </tr>
    <tr>
        <td>Perancang/Koordinator</td>
        <td>Menentukan masalah, tujuan, ruang lingkup, dan rancangan program.</td>
    </tr>
    <tr>
        <td>Programmer</td>
        <td>Mengembangkan kode program dan mengintegrasikan modul.</td>
    </tr>
    <tr>
        <td>Tester/QA</td>
        <td>Menyusun serta menjalankan test case dan memeriksa hasil program.</td>
    </tr>
    <tr>
        <td>Dokumentasi</td>
        <td>Menyusun proposal, README, dan dokumentasi pengujian.</td>
    </tr>
    <tr>
        <td>Pengelola Repository</td>
        <td>Mengelola file proyek dan riwayat perubahan menggunakan Git dan GitHub.</td>
    </tr>
</table>

Nama penanggung jawab seluruh peran: Suchita Rahma Fakhira.

## 12. Jadwal Pelaksanaan

<table>
    <tr>
        <th>Tahap</th>
        <th>Target Kegiatan</th>
    </tr>
    <tr>
        <td>Pertemuan 14</td>
        <td>Menyusun proposal, kebutuhan, IPO, pseudocode, struktur program, struktur data, test case, pembagian tugas, jadwal, dan repository.</td>
    </tr>
    <tr>
        <td>Antara Pertemuan 14–15</td>
        <td>Mengembangkan implementasi program berdasarkan rancangan yang telah disusun.</td>
    </tr>
    <tr>
        <td>Pertemuan 15</td>
        <td>Melakukan integrasi program, pengujian, perbaikan kesalahan, dan penyempurnaan dokumentasi.</td>
    </tr>
    <tr>
        <td>Pertemuan 16</td>
        <td>Menyelesaikan evaluasi akhir, menyiapkan demonstrasi program, dan mempresentasikan hasil proyek.</td>
    </tr>
</table>

## 13. Repository GitHub

Repository Proyek:

https://github.com/SuchitaRahmaFakhira/proyek-akhir-Suchita-Rahma-Fakhira-2225250006.git

Repository GitHub digunakan untuk menyimpan dokumen rancangan, kode program, skenario pengujian, dokumentasi, serta riwayat perubahan proyek.


## Penutup

Proyek Generator dan Evaluasi Soal Operasi Hitung Campuran dirancang sebagai program sederhana berbasis Python untuk membantu pengguna berlatih dan mengevaluasi penyelesaian soal aritmetika. Proposal ini mencakup identifikasi masalah, pengguna dan tujuan, ruang lingkup, kebutuhan fungsional dan nonfungsional, IPO, algoritma, struktur program, struktur data, test case, pembagian tugas, jadwal, dan repository GitHub.

Rancangan ini menjadi dasar pengembangan, pengujian, dan penyempurnaan program pada tahap berikutnya.

## Referensi

Bahan Ajar Algoritma dan Pemrograman, Pertemuan 14: Perancangan Proyek Program Sederhana, Program Studi S1 Pendidikan Matematika, FKIP, Universitas Sultan Ageng Tirtayasa, Tahun Akademik 2026/2027 Ganjil.
