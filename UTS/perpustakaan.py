from datetime import datetime
from buku import Buku

class Perpustakaan(Buku):
    def __init__(self, nama_cabang = "Perpustakaan Pusat"):
        super().__init__(item_id=None, judul=None, penulis=None)
        self.__nama_cabang = nama_cabang

    def show_katalog(self, katalog_perpustakaan):
        print("\n" + "="*70)
        print("ID   | JUDUL BUKU        | PENULIS               | STATUS")
        print("-"*70)

        for key, value in katalog_perpustakaan.items():
            buku = value["item"]
            status = "Tersedia" if value["tersedia"] else "Dipinjam"
            print(f"{buku.get_item_id():<4} | {buku.get_judul():<18} | {buku.get_penulis():<20} | [{status}]")

        print("="*70)

    def peminjaman(self, katalog_perpustakaan, item_id):
        if item_id not in katalog_perpustakaan:
            print(f"[GAGAL] Buku dengan ID '{item_id}' tidak ditemukan")
            return False

        if not katalog_perpustakaan[item_id]["tersedia"]:
            print("[GAGAL] Buku sedang dipinjam")
            return False
        
        katalog_perpustakaan[item_id]["tersedia"] = False
        print(f"[SUKSES] Berhasil meminjam : {katalog_perpustakaan[item_id]['item'].get_judul()}")
        return True
    
    def pengembalian(self, katalog_perpustakaan, item_id, tanggal_pinjam, tanggal_kembali):
        if item_id not in katalog_perpustakaan:
            print(f"[GAGAL] Buku dengan ID '{item_id}' tidak ditemukan")
            return False
        
        if katalog_perpustakaan[item_id]["tersedia"]:
            print(f"[GAGAL] Buku '{katalog_perpustakaan[item_id]['item'].get_judul()}' tidak sedang dipinjam dan tersedia di perpustakaan")
            return False
        
        #konversi tanggal ke format datetime
        DateFormat1 = datetime.strptime(tanggal_pinjam, "%Y-%m-%d")
        DateFormat2 = datetime.strptime(tanggal_kembali, "%Y-%m-%d")

        totalHari = (DateFormat2 - DateFormat1).days
        batasHari = 7

        print(f"[SUKSES] Berhasil mengembalikan : {katalog_perpustakaan[item_id]['item'].get_judul()}")
        if totalHari > batasHari:
            denda = katalog_perpustakaan[item_id]["item"].hitung_denda(totalHari - batasHari)
            print(f"[INFO] Terlambat {totalHari - batasHari} hari. Total denda: Rp {denda}")
        else:
            print(f"[INFO] Dikembalikan tepat waktu. Tidak ada denda.")
        
        katalog_perpustakaan[item_id]["tersedia"] = True
        return True
    
#dict obj 
katalog_perpustakaan = {
    "B01": {"item": Buku("B01", "Filosofi Teras", "Henry Manampiring"), "tersedia": True},
    "B02": {"item": Buku("B02", "Laskar Pelangi", "Andrea Hirata"), "tersedia": True},
    "B03": {"item": Buku("B03", "Bumi Manusia", "Pramoedya Ananta Toer"), "tersedia": True},
    "B04": {"item": Buku("B04", "Negeri 5 Menara", "A. Fuadi"), "tersedia": True},
    "B05": {"item": Buku("B05", "Cantik Itu Luka", "Eka Kurniawan"), "tersedia": True},
    "B06": {"item": Buku("B06", "Pulang", "Leila S. Chudori"), "tersedia": True},
    "B07": {"item": Buku("B07", "Hujan Bulan Juni", "Sapardi Djoko Damono"), "tersedia": True},
    "B08": {"item": Buku("B08", "Garis Waktu", "Fiersa Besari"), "tersedia": True}
}

