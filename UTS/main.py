from perpustakaan import Perpustakaan, katalog_perpustakaan
from buku import Buku

if __name__ == "__main__":
    perpus = Perpustakaan()

    while True:
        print("\n=== SISTEM INFORMASI PERPUSTAKAAN ===")
        print("1. Tampilkan Daftar Buku")
        print("2. Peminjaman Buku")
        print("3. Pengembalian Buku")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            perpus.show_katalog(katalog_perpustakaan)
        elif pilihan == '2':
            item_id = input("Masukkan ID buku yang ingin dipinjam: ")
            perpus.peminjaman(katalog_perpustakaan, item_id)
        elif pilihan == '3':
            item_id = input("Masukkan ID buku yang ingin dikembalikan: ")
            tanggal_pinjam = input("Masukkan tanggal pinjam (YYYY-MM-DD): ")
            tanggal_kembali = input("Masukkan tanggal kembali (YYYY-MM-DD): ")
            perpus.pengembalian(katalog_perpustakaan, item_id, tanggal_pinjam, tanggal_kembali)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem informasi perpustakaan!")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")