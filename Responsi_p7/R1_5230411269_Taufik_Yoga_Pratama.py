class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk):
        self._kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk

class Snack(Produk):
    def __init__(self, kode_produk, nama_produk, jenis_produk, nama_snack, harga):
        super().__init__(kode_produk, nama_produk, jenis_produk)
        self.nama_snack = nama_snack
        self.harga = harga

    def show(self):
        print(f"===== Snack =====\nKode: {self._kode_produk}   Nama: {self.nama_snack}    Jenis: {self.jenis_produk}    Harga: {self.harga}")

class Makanan(Produk):
    def __init__(self, kode_produk, nama_produk, jenis_produk, nama_makanan, harga):
        super().__init__(kode_produk, nama_produk, jenis_produk)
        self.nama_makanan = nama_makanan
        self.harga = harga

    def show(self):
        print(f"===== Makanan =====\nKode: {self._kode_produk}   Nama: {self.nama_makanan}    Jenis: {self.jenis_produk}    Harga: {self.harga}")

class Minuman(Produk):
    def __init__(self, kode_produk, nama_produk, jenis_produk, nama_minuman, harga):
        super().__init__(kode_produk, nama_produk, jenis_produk)
        self.nama_minuman = nama_minuman
        self.harga = harga

    def show(self):
        print(f"===== Minuman =====\nKode: {self._kode_produk}   Nama: {self.nama_minuman}    Jenis: {self.jenis_produk}    Harga: {self.harga}")

class Transaksi:
    def __init__(self, no_transaksi, detail):
        self.no_transaksi = no_transaksi
        self.detail = detail

class Pegawai:
    def __init__(self, NIK, nama, alamat):
        self._NIK = NIK
        self.nama = nama
        self.alamat = alamat

class Struk:
    def __init__(self, no_transaksi, nama_pegawai, jumlah_produk, total_harga):
        self.no_transaksi = no_transaksi
        self.nama_pegawai = nama_pegawai
        self.jumlah_produk = jumlah_produk
        self.total_harga = total_harga

produk_list = []
pegawai_list = []

def tambah_produk():
    kode_produk = input("Masukkan kode produk: ")
    nama_produk = input("Masukkan nama produk: ")
    jenis_produk = input("Masukkan jenis produk (makanan/minuman/snack): ").lower()
    
    while True:
        try:
            harga = int(input("Masukkan harga produk: "))
            break
        except ValueError:
            print("Input tidak valid. Harga harus berupa angka.")
    
    if jenis_produk == "snack":
        produk = Snack(kode_produk, nama_produk, jenis_produk, nama_produk, harga)
    elif jenis_produk == "makanan":
        produk = Makanan(kode_produk, nama_produk, jenis_produk, nama_produk, harga)
    elif jenis_produk == "minuman":
        produk = Minuman(kode_produk, nama_produk, jenis_produk, nama_produk, harga)
    else:
        print("Jenis produk tidak valid.")
        return
    
    produk_list.append(produk)
    print("Produk berhasil ditambahkan.")

def edit_produk():
    kode_produk = input("Masukkan kode produk yang ingin diedit: ")
    for produk in produk_list:
        if produk._kode_produk == kode_produk:
            produk.nama_produk = input("Masukkan nama produk baru: ")
            
            while True:
                try:
                    produk.harga = int(input("Masukkan harga produk baru: "))
                    break
                except ValueError:
                    print("Input tidak valid. Harga harus berupa angka.")
            
            print("Produk berhasil diupdate.")
            return
    print("Produk tidak ditemukan.")

def tambah_pegawai():
    while True:
        try:
            NIK = int(input("Masukkan NIK pegawai (angka): "))
            break
        except ValueError:
            print("Input tidak valid. NIK harus berupa angka.")
    
    nama = input("Masukkan nama pegawai: ")
    alamat = input("Masukkan alamat pegawai: ")
    
    pegawai = Pegawai(NIK, nama, alamat)
    pegawai_list.append(pegawai)
    print("Pegawai berhasil ditambahkan.")

def menu():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Lihat Produk")
        print("2. Tambah Produk")
        print("3. Edit Produk")
        print("4. Hapus Produk")
        print("5. Lihat Pegawai")
        print("6. Tambah Pegawai")
        print("7. Edit Pegawai")
        print("8. Hapus Pegawai")
        print("9. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            lihat_produk()
        elif pilihan == "2":
            tambah_produk()
        elif pilihan == "3":
            edit_produk()
        elif pilihan == "4":
            hapus_produk()
        elif pilihan == "5":
            lihat_pegawai()
        elif pilihan == "6":
            tambah_pegawai()
        elif pilihan == "7":
            edit_pegawai()
        elif pilihan == "8":
            hapus_pegawai()
        elif pilihan == "9":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def lihat_produk():
    if not produk_list:
        print("Belum ada produk.")
    for produk in produk_list:
        produk.show()

def lihat_pegawai():
    if not pegawai_list:
        print("Belum ada pegawai.")
    print("===== Pegawai =====")
    for pegawai in pegawai_list:
        print(f"NIK: {pegawai._NIK}, Nama: {pegawai.nama}, Alamat: {pegawai.alamat}")

def hapus_produk():
    kode_produk = input("Masukkan kode produk yang ingin dihapus: ")
    for produk in produk_list:
        if produk._kode_produk == kode_produk:
            produk_list.remove(produk)
            print("Produk berhasil dihapus.")
            return
    print("Produk tidak ditemukan.")

def edit_pegawai():
    while True:
        try:
            NIK = int(input("Masukkan NIK pegawai yang ingin diedit: "))
            break
        except ValueError:
            print("Input tidak valid. NIK harus berupa angka.")
    
    for pegawai in pegawai_list:
        if pegawai._NIK == NIK:
            pegawai.nama = input("Masukkan nama pegawai baru: ")
            pegawai.alamat = input("Masukkan alamat pegawai baru: ")
            print("Pegawai berhasil diupdate.")
            return
    print("Pegawai tidak ditemukan.")

def hapus_pegawai():
    while True:
        try:
            NIK = int(input("Masukkan NIK pegawai yang ingin dihapus: "))
            break
        except ValueError:
            print("Input tidak valid. NIK harus berupa angka.")
    
    for pegawai in pegawai_list:
        if pegawai._NIK == NIK:
            pegawai_list.remove(pegawai)
            print("Pegawai berhasil dihapus.")
            return
    print("Pegawai tidak ditemukan.")

menu()