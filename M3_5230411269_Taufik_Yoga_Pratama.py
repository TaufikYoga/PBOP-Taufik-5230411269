makanan = [
    ["Mie ayam", 10000],
    ["Nasi goreng", 12000],
    ["Gado-gado", 8000]
]

minuman = [
    ["Jus jeruk", 5000],
    ["Jus apel", 6000],
    ["Kopi", 4000]
]

class DaftarMenu:
    def __init__(self, makanan, minuman):
        self.makanan = makanan
        self.minuman = minuman

    def displayMakanan(self):
        print("===== Daftar Menu Makanan =====")
        for i in self.makanan:
            print(f"{i[0]} harga: {i[1]}")

    def displayMinuman(self):
        print("===== Daftar Menu Minuman =====")
        for i in self.minuman:
            print(f"{i[0]} harga: {i[1]}")

    def tambahMenuMakanan(self):
        try:
            nama = str(input("Masukkan nama makanan: "))
            harga = int(input("Masukkan harga makanan: "))
            self.makanan.append([nama, harga])
        except ValueError:
            if nama != str:
                print("Nama harus berupa string")
            elif harga != int:
                print("Harga harus berupa integer")
    def tambahMenuMinuman(self):
        try:
            nama = input("Masukkan nama minuman: ")
            harga = int(input("Masukkan harga minuman: "))
            self.minuman.append([nama, harga])
        except ValueError:
            if nama != str:
                print("Nama harus berupa string")
            elif harga != int:
                print("Harga harus berupa integer")


daftarMenu = DaftarMenu(makanan, minuman)
def main():
    status = True
    while status:
        print("========== Pilih Menu ==========")
        print("1. Tampilkan Menu Makanan")
        print("2. Tampilkan Menu Minuman")
        print("3. Tambah Menu")
        print("0. Keluar")
        inputanUsr = input("Masukkan menu (1/2/3/4): ")
        if inputanUsr == "1":
            daftarMenu.displayMakanan()
        elif inputanUsr == "2":
            daftarMenu.displayMinuman()
        elif inputanUsr == "3":
            statusAdd = True
            while statusAdd:
                print("========== Pilih Menu ==========")
                print("1. Tambah Menu Makanan")
                print("2. Tambah Menu Minuman")
                print("0. Kembali")
                inputanTambah = input("Masukkan pilihan: ")
                if inputanTambah == "1":
                    daftarMenu.tambahMenuMakanan()
                elif inputanTambah == "2":
                    daftarMenu.tambahMenuMinuman()
                elif inputanTambah == "0":
                    statusAdd = False
                else:
                    print("Inputan salah, masukkan angk1 1/2/3/4")
        elif inputanUsr == "0":
            status = False
        else:
            print("Input salah masukkan angka 1/2/3/4")

main()