# (Soal) Buatlah program Python yang menghitung usia seseorang berdasarkan tahun lahir dan tahun sekarang, lalu menghitung dan menampilkan usia orang tersebut

#header
print(41*"=")
print("Studi Kasus 2 : Menghitung Usia Seseorang")
print(41*"=")

#variabel
Tahun_lahir = int(input("Masukkan tahun kelahiran anda : \n"))
Tahun_sekarang = int(input("Masukkan tahun saat ini : \n"))

Usia = Tahun_sekarang - Tahun_lahir

#output
print(f"Usia anda saat ini adalah {Usia} \n")
print("Operasi Berhasil, Terimakasih Karena Sudah Mau Mencoba >.<")
