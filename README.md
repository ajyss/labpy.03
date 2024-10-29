# input dan outpu dari latihan 1
## input

<img src="latihaan 1.png">

## output

<img scr="LATIHAN 1.png">

## Alur Algoritma Program Bilangan Acak

## Import dan Definisi Fungsi
1. Program dimulai dengan mengimport fungsi `random()` dari modul `random`
2. Mendefinisikan fungsi `tampilkan_bilangan_acak()` tanpa parameter

## Struktur Try-Except
Program menggunakan struktur try-except untuk menangani kemungkinan error saat input:
- `try`: Blok kode utama yang akan dijalankan
- `except ValueError`: Menangani error jika input bukan angka bulat

## Proses Input
1. Program meminta user memasukkan nilai N menggunakan `input()`
2. Input dikonversi ke integer dengan `int()`
3. Jika input bukan angka bulat, akan menghasilkan ValueError dan menampilkan pesan error

## Logika Utama Program
1. Inisialisasi variabel penghitung `i = 1`

2. Loop While (`while i <= n`):
   - Akan terus berjalan selama i belum melebihi n
   - Di setiap iterasi:
     a. Generate bilangan acak dengan `random()`
     b. Cek apakah bilangan < 0.5
     c. Jika < 0.5:
        - Tampilkan bilangan
        - Increment i
     d. Jika >= 0.5:
        - `continue` (kembali ke awal loop tanpa increment i)
        - Bilangan tidak ditampilkan
        - Mencoba generate bilangan baru

3. Setelah loop selesai (i > n):
   - Tampilkan "Selesai"

## Karakteristik Khusus
1. Penggunaan `continue`:
   - Jika bilangan >= 0.5, iterasi saat ini dilewati
   - i tidak bertambah
   - Program mencoba generate bilangan baru
   
2. Increment i:
   - i hanya bertambah jika bilangan < 0.5
   - Memastikan mendapat tepat N bilangan yang < 0.5

## Contoh Alur Eksekusi
Misalkan N = 3:
1. User input "3"
2. i = 1
3. Generate bilangan acak:
   - Jika 0.7 -> continue, i tetap 1
   - Jika 0.3 -> tampilkan, i jadi 2
   - Jika 0.6 -> continue, i tetap 2
   - Jika 0.4 -> tampilkan, i jadi 3
   - Jika 0.2 -> tampilkan, i jadi 4
4. i > 3, loop berhenti
5. Tampilkan "Selesai"

## Output yang Diharapkan
```
Masukkan nilai N: 3
data ke: 1 => 0.234
data ke: 2 => 0.445
data ke: 3 => 0.123
Selesai
```

## Penanganan Error
- Jika input bukan angka (misal "abc"):
  1. Terjadi ValueError
  2. Eksekusi pindah ke blok except
  3. Tampilkan pesan error
  4. Program selesai