# Tugas Akhir Praktikum Algoritma Pemrograman


"""
Kasir Bhoyo Resto

Program ini berfungsi untuk melakukan pencetakan bon transaksi pembelian di Resto Bhoyo . Program akan 
meminta memasukan identitas customer, kemudian menghitung biaya dari pembelian makanan di resto Bhoyo  tersebut dan
mencetak bon hasil transaksi.
"""
import datetime

identitas = ["Nama Pelanggan", "Alamat", "No Telepon",]
data = []

tanggal = datetime.datetime.now()

print(30*"="+"""
Nama\t: Ari Setiawan 
NIM\t: 2270231089
Program\t: Kasir Bhoyo Resto
""" + 30*"=" + "\n")

menu = {
        "Fried Chiken"  :15000,
        "Burger Beef"   :23000,
        "Frech Fries"   :8000,
        "Jasmine Tea"   :5000,
        "Ice Coca Cola" :10000
}
print("============== Daftar Menu ==============")
for i in menu:
    print("Daftar Menu :", i,"\t Harga : ",menu[i])

print("==========================================")


for x in range(len(identitas)):
    val = input("Masukkan " + identitas[x] + ": ")
    data.append(val)
beli = input("Pilih Menu : ")
jumlah = int(input("jumlah Pesanan : "))
Bayar = jumlah * menu[beli]

if Bayar > 100000:
    dikon = Bayar*15/100
    total = Bayar 
    
else :
    total = Bayar

print("\n"+8*"=" + "Bhoyo Resto" + 8*"="+"\n") 

print("Tanggal : " + tanggal.strftime("%d - %m - %Y %X"))    

print ("============== Daftar Menu ==============")
print ("Menu Yang Di Pesan           : ",beli)
print ("Jumlah Yang Dipesan          : ",jumlah)
print ("Total Biaya                  : ",Bayar)
print ("Total Yang Harus Di Bayar    : ",total)    




