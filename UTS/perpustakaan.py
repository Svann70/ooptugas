from buku import Buku

class Perpustakaan(Buku):
    def __init__(self, nama_cabang = "Perpustakaan Pusat"):
        super().__init__(item_id=None, judul=None, penulis=None)
        self.__nama_cabang = nama_cabang

    def show_katalog(self, katalog):
        print("\n" + "="*70)
        print("ID   | JUDUL BUKU        | PENULIS               | STATUS")
        print("-"*70)

        for key, value in katalog.items():
            buku = value["item"]
            status = "Tersedia" if value["tersedia"] else "Dipinjam"
            print(f"{buku.get_item_id():<4} | {buku.get_judul():<18} | {buku.get_penulis():<20} | [{status}]")

        print("="*70)

    def peminjaman(self, katalog, item_id):
        if item_id not in katalog:
            print(f"[GAGAL] Buku dengan ID '{item_id}' tidak ditemukan")
            return False
        
        if not katalog[item_id]["tersedia"]:
            print("[GAGAL] Buku sedang dipinjam")
            return False
        
        katalog[item_id]["tersedia"] = False
        print(f"[SUKSES] Berhasil meminjam : {katalog[item_id]['item'].get_judul()}")
        return True
    
    def pengembalian(self, katalog, item_id, tanggal_pinjam, tanggal_kembali):
        if item_id not in katalog:
            print(f"[GAGAL] Buku dengan ID '{item_id}' tidak ditemukan")
            return False
        
        if katalog[item_id]["tersedia"]:
            print(f"[GAGAL] Buku '{katalog[item_id]['item'].get_judul()}' tidak sedang dipinjam")
            return False
        
        #konversi tanggal ke format datetime
        