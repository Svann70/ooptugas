class komponen_harga:
    def __init__ (self, subtotal):
        self.subtotal = subtotal
        self.totalakhir = subtotal


class PajakPPN(komponen_harga):
    def __init__ (self, subtotal):
        super().__init__(subtotal)
        self.nilaipajak = self.subtotal * 0.1
        self.totalakhir += self.nilaipajak

class TransaksiPOS(PajakPPN):
    def __init__ (self, pelanggan, meja):
        super().__init__(0)
        self.pelanggan = pelanggan
        self.meja = meja
        self.daftarpesanan = []

    def tambah_pesanan(self, nama_menu, harga, jumlah):
        self.daftarpesanan.append((nama_menu, harga, jumlah))
        self.subtotal += harga * jumlah
        self.totalakhir += harga * jumlah
    
    def tampilkan_struk(self):
        print()
        print(f"==================================")
        print(f"     STRUK PEMBAYARAN - {self.meja}     ")
        print(f"==================================")
        print(f'Pelanggan: {self.pelanggan}')
        print("----------------------------")
        print("Daftar Pesanan:")
        for nama_menu, harga, jumlah in self.daftarpesanan:
            print(f"- {nama_menu}: Rp {harga} x {jumlah} = Rp {harga * jumlah}")
        print("----------------------------")
        print(f"Subtotal: Rp {self.subtotal}")
        print("----------------------------")
        print(f"Pajak PPN (10%): Rp {self.nilaipajak}")
        print("----------------------------")
        print(f"Total Akhir: Rp {self.totalakhir}")
    
    def proses_pembayaran(self):
        self.nilaipajak = self.subtotal * 0.1
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
    print("----- INPUT PESANAN -----")
    nama_menu = input("Masukkan nama menu (atau 'selesai' untuk selesai): ")

    if nama_menu.lower() == 'selesai':
        break

    harga = int(input("Masukkan harga menu: "))
    jumlah = int(input("Masukkan jumlah pesanan: "))
    transaksi.tambah_pesanan(nama_menu, harga, jumlah)

transaksi.proses_pembayaran()
transaksi.tampilkan_struk()