#Naufal Haidar Azhar 19.1A.21 (19240761)

# (Soal) Seorang pengguna memiliki sejumlah uang. Dia membeli beberapa barang dengan harga yang sudah ditentukan. Buatlah program Pythonn yang menghitung sisa uang setelah belanja. Program meminta input total uang yang dimiliki dan total biaya belanja. Tampilkan sisa uang setelah pembelian

#header
print(52*"=")
print("Studi Kasus 1 : Menghitung Sisa Uang Setelah Belanja")
print(52*"=")

#variabel
Uang = int(input("Masukkan uang pertama anda (Rp) = "))
Barang = int(input("Masukkan harga barang yang anda beli (Rp) = "))

Sisa = Uang - Barang

#output
print(f"Sisa uang anda setelah membeli barang tersebut adalah Rp {Sisa} \n")
print("Operasi Berhasil, Terimakasih Karena Sudah Mau Mencoba >.<")
