#SISTEM INFORMASI PERPUSTAKAAN

class Buku:
    def __init__(self, item_id, judul, penulis, status):
        self.__item_id = item_id
        self.__judul = judul
        self.__penulis = penulis
        self.__status = True 
    
    #getter
    def get_item_id(self):
        return self.__item_id
    
    def get_judul(self):
        return self.__judul
    
    def get_penulis(self):
        return self.__penulis
    
    def get_status(self):
        return self.__status
    
    #setter
    def set_item_id(self, item_id):
        self.__item_id = item_id

    def set_judul(self, judul):
        self.__judul = judul

    def set_penulis(self, penulis):
        self.__penulis = penulis

    def set_status(self, status):
        self.__status = status

    #denda
    def hitung_denda(self, hari_terlambat):
        if hari_terlambat > 0:
            denda_per_hari = 5000
            total_denda = hari_terlambat * denda_per_hari
            return total_denda
        else:
            return 0
        

    
    