from oop import KomponenHarga
from oop import PajakPPN
from oop import TransaksiPOS

def main():
    
    print("=== OOP KASIR ===")

nama = input("Masukkan nama pelanggan: ")
meja = int(input("Masukkan nomor meja: "))
transaksi = TransaksiPOS(nama, meja)

while True:
    print("----- INPUT PESANAN -----")
    nama_menu = input("Masukkan nama menu (atau 'selesai' untuk selesai): ")

    if nama_menu.lower() == 'selesai':
        break

    harga = int(input("Masukkan harga menu: "))
    jumlah = int(input("Masukkan jumlah pesanan: "))
    transaksi.tambah_item(nama_menu, harga, jumlah)

transaksi.proses_pembayaran()
transaksi.cetak_struk()
       
if __name__ == "__main__":
    main()