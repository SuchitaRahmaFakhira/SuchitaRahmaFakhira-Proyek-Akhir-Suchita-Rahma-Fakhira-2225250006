# Test Case: Generator dan Evaluasi Soal Operasi Hitung Campuran

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat menghasilkan soal operasi hitung campuran secara acak, memeriksa jawaban pengguna, memvalidasi input, menghitung skor akhir, dan menyimpan hasil latihan dengan benar.

## 2. Daftar Test Case

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
<td>Soal `5 + 3 * 2`, jawaban pengguna `11`.</td>
<td>Program menyatakan jawaban benar dan menambah jumlah jawaban benar.</td>
</tr>
<tr>
<td>TC02</td>
<td>Jawaban salah</td>
<td>Soal `5 + 3 * 2`, jawaban pengguna `16`.</td>
<td>Program menyatakan jawaban salah.</td>
</tr>
<tr>
<td>TC03</td>
<td>Normal</td>
<td>Soal `12 / 3 + 2`, jawaban pengguna `6`.</td>
<td>Program menyatakan jawaban benar dan menambah jumlah jawaban benar.</td>
</tr>
<tr>
<td>TC04</td>
<td>Batas</td>
<td>Pengguna memasukkan jumlah soal `1`.</td>
<td>Program menerima masukan dan menghasilkan satu soal.</td>
</tr>
<tr>
<td>TC05</td>
<td>Invalid</td>
<td>Pengguna memasukkan jumlah soal `0`.</td>
<td>Program menolak masukan dan meminta jumlah soal yang valid.</td>
</tr>
<tr>
<td>TC06</td>
<td>Invalid</td>
<td>Pengguna memasukkan teks `abc` ketika diminta jumlah soal.</td>
<td>Program menampilkan pesan kesalahan dan meminta masukan angka yang valid.</td>
</tr>
<tr>
<td>TC07</td>
<td>Normal</td>
<td>Semua soal dijawab dengan benar.</td>
<td>Nilai akhir yang ditampilkan adalah 100.</td>
</tr>
<tr>
<td>TC08</td>
<td>Penyimpanan</td>
<td>Pengguna menyelesaikan latihan.</td>
<td>Hasil latihan berhasil disimpan ke file teks.</td>
</tr>
</table>

## 3. Kesimpulan

Program dinyatakan memenuhi pengujian apabila setiap skenario menghasilkan keluaran sesuai dengan hasil yang diharapkan. Pengujian aktual dilakukan setelah implementasi program selesai.

Hasil aktual setiap pengujian akan dicatat dan dibandingkan dengan hasil yang diharapkan untuk mengetahui apakah program berjalan sesuai kebutuhan.