class KomponenHarga:
    def __init__ (self, subtotal):
        self.subtotal = subtotal
        self.totalakhir = subtotal

class PajakPPN(KomponenHarga):
    def __init__ (self, subtotal):
        super().__init__(subtotal)
        self.nilaipajak = self.subtotal * 0.1 # Float (nilai pajak dan sub total) 
        self.totalakhir += self.nilaipajak

class TransaksiPOS(PajakPPN):
    def __init__ (self, pelanggan, meja):
        super().__init__(0)
        self.pelanggan = pelanggan
        self.meja = meja
        self.daftarpesanan = []

    def tambah_item(self, nama_menu, harga, jumlah):
        self.daftarpesanan.append((nama_menu, harga, jumlah))
        self.subtotal += harga * jumlah
        self.totalakhir += harga * jumlah
    
    def cetak_struk(self):
        print()
        print(f"=============================================")
        print(f"       STRUK PEMBAYARAN - MEJA {self.meja}   ")
        print(f"=============================================")
        print(f'Pelanggan: {self.pelanggan}')
        print("----------------------------------------------")
        print()
        print("Daftar Pesanan:")
        # for nama_menu, harga, jumlah in self.daftarpesanan:
        #     print(f"{nama_menu}:                     x {jumlah}    Rp {harga}")
        for nama_menu, harga, jumlah in self.daftarpesanan:
            total_item = harga * jumlah 
            print(f"{nama_menu:<25} x {jumlah:>2}   Rp {total_item:>10,}")
        print("---------------------------------------------"   )
        print(f"Subtotal                  : Rp       {self.subtotal}")
        print("---------------------------------------------")
        print(f"PPN (10%)                 : Rp       {self.nilaipajak}")
        print("---------------------------------------------")
        print(f"Total Akhir               : Rp       {self.totalakhir}")
        print(f"=============================================")
    
     def proses_pembayaran(self):
        self.nilaipajak = self.subtotal * 0.1 # Float (sub total dan total akhr)
        self.totalakhir = self.subtotal + self.nilaipajak

        bayar = float(input("Masukkan jumlah pembayaran: Rp "))
        if bayar < self.totalakhir:
            print("Pembayaran tidak cukup. Silakan coba lagi.")
            self.proses_pembayaran()
        else:
            kembalian = bayar - self.totalakhir
            print(f"Kembalian: Rp {kembalian}")


#MAIN PROGRAM

print("=== OOP KASIR ===")

nama = input("Masukkan nama pelanggan: ")
meja = int(input("Masukkan nomor meja: "))
transaksi = TransaksiPOS(nama, meja)

while True:
    print()
    print("----- INPUT PESANAN -----")
    nama_menu = input("Masukkan nama menu (atau 'selesai' untuk selesai): ")

    if nama_menu.lower() == 'selesai':
        break

    harga = int(input("Masukkan harga menu: "))
    jumlah = int(input("Masukkan jumlah pesanan: "))
    transaksi.tambah_item(nama_menu, harga, jumlah)

transaksi.proses_pembayaran()
transaksi.cetak_struk()
