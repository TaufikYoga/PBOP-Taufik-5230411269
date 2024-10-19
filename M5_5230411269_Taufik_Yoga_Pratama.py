all_song_list = [
    {
        "Judul": "Lemon",
        "Penyanyi": "Kenshi Yonezu",
        "Genre": "J-Song"
    },
    {
        "Judul": "Paprika",
        "Penyanyi": "Foorin",
        "Genre": "J-Song"
    },
    {
        "Judul": "Silhouette",
        "Penyanyi": "Kana-Boon",
        "Genre": "J-Song"
    },
    {
        "Judul": "Pretender",
        "Penyanyi": "Official HIGE DANDism",
        "Genre": "J-Song"
    },
    {
        "Judul": "Gurenge",
        "Penyanyi": "LiSA",
        "Genre": "J-Song"
    },
    {
        "Judul": "Dynamite",
        "Penyanyi": "BTS",
        "Genre": "K-Song"
    },
    {
        "Judul": "Lovesick Girls",
        "Penyanyi": "BLACKPINK",
        "Genre": "K-Song"
    },
    {
        "Judul": "Gangnam Style",
        "Penyanyi": "PSY",
        "Genre": "K-Song"
    },
    {
        "Judul": "Shape of You",
        "Penyanyi": "Ed Sheeran",
        "Genre": "E-Song"
    },
    {
        "Judul": "Feel Special",
        "Penyanyi": "TWICE",
        "Genre": "K-Song"
    },
    {
        "Judul": "Any Song",
        "Penyanyi": "Zico",
        "Genre": "K-Song"
    },
    {
        "Judul": "Blinding Lights",
        "Penyanyi": "The Weeknd",
        "Genre": "E-Song"
    },
    {
        "Judul": "Rolling in the Deep",
        "Penyanyi": "Adele",
        "Genre": "E-Song"
    },
    {
        "Judul": "Bad Guy",
        "Penyanyi": "Billie Eilish",
        "Genre": "E-Song"
    },
    {
        "Judul": "Uptown Funk",
        "Penyanyi": "Mark Ronson ft. Bruno Mars",
        "Genre": "E-Song"
    }
]


japanese_song_list = [
    {
        "Judul": "Lemon",
        "Penyanyi": "Kenshi Yonezu",
        "Genre": "J-Song"
    },
    {
        "Judul": "Paprika",
        "Penyanyi": "Foorin",
        "Genre": "J-Song"
    },
    {
        "Judul": "Silhouette",
        "Penyanyi": "Kana-Boon",
        "Genre": "J-Song"
    },
    {
        "Judul": "Pretender",
        "Penyanyi": "Official HIGE DANDism",
        "Genre": "J-Song"
    },
    {
        "Judul": "Gurenge",
        "Penyanyi": "LiSA",
        "Genre": "J-Song"
    }
]
korean_song_list = [
    {
        "Judul": "Dynamite",
        "Penyanyi": "BTS",
        "Genre": "K-Song"
    },
    {
        "Judul": "Lovesick Girls",
        "Penyanyi": "BLACKPINK",
        "Genre": "K-Song"
    },
    {
        "Judul": "Gangnam Style",
        "Penyanyi": "PSY",
        "Genre": "K-Song"
    },
    {
        "Judul": "Feel Special",
        "Penyanyi": "TWICE",
        "Genre": "K-Song"
    },
    {
        "Judul": "Any Song",
        "Penyanyi": "Zico",
        "Genre": "K-Song"
    }
]
english_song_list = [
    {
        "Judul": "Shape of You",
        "Penyanyi": "Ed Sheeran",
        "Genre": "E-Song"
    },
    {
        "Judul": "Blinding Lights",
        "Penyanyi": "The Weeknd",
        "Genre": "E-Song"
    },
    {
        "Judul": "Rolling in the Deep",
        "Penyanyi": "Adele",
        "Genre": "E-Song"
    },
    {
        "Judul": "Bad Guy",
        "Penyanyi": "Billie Eilish",
        "Genre": "E-Song"
    },
    {
        "Judul": "Uptown Funk",
        "Penyanyi": "Mark Ronson ft. Bruno Mars",
        "Genre": "E-Song"
    }
]

def hapus_lagu(list, judul):
    for i, lagu in enumerate(list):
        if lagu["Judul"] == judul:
            del list[i]
            print(f"Lagu '{judul}' telah dihapus.")
            return
    print(f"Lagu '{judul}' tidak ditemukan.")

def cari_lagu(list_musik, penyanyi):
    hasil = []
    for lagu in list_musik:
        if lagu["Penyanyi"] == penyanyi:
            hasil.append(lagu)
    if hasil:
        print(" ")
        print("Judul              Penyanyi          Genre")
        print("==========================================")
        for musik in hasil:
            print(f"{musik['Judul']}          {musik['Penyanyi']}           {musik['Genre']}")
    else:
        print(f"Lagu dengan penyanyi {penyanyi}' tidak ditemukan.")


def main_menu():
    try:
        print("========== Playlist Music ==========")
        print("1. Japanese Song")
        print("2. Korean Song")
        print("3. English Song")
        print("4. Display All")
        print("5. Search Music")
        print("0. Keluar")
        inputan_user = int(input("Masukan Pilihan Menu: "))
        return inputan_user
    except ValueError:
            if inputan_user != int:
                print("Inputan harus angka")
                
def song_menu():
    try:
        print("========== Song ==========")
        print("1. Display Song")
        print("2. Add Song")
        print("3. Delete Song")
        print("0. Kembali")
        inputan_user = int(input("Masukan Pilihan Sub Menu Japanese Song: "))
        return inputan_user
    except ValueError:
            if inputan_user != int:
                print("Inputan harus angka")
                
class Music:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre
        
    def display_all(self):
        print(">> List Song")
        print(" ")
        print(f"Total Songs = {len(all_song_list)}")
        print(" ")
        print("Judul              Penyanyi          Genre")
        print("==========================================")
        # for lagu in all_song_list:
        #     print(f"{lagu['Judul']}          {lagu['Penyanyi']}          {lagu['Genre']}")
        lagu_terurut = sorted(all_song_list, key=lambda x: x["Judul"])
        
        for lagu in lagu_terurut:
            # print(f"Judul: {lagu['Judul']} Penyanyi: {lagu['Penyanyi']}, Genre: {lagu['Genre']}")
            print(f"{lagu['Judul']}          {lagu['Penyanyi']}          {lagu['Genre']}")
            
    def japanese_song(self):
        while True:
            inputan_user = song_menu()
            if inputan_user == 1:
                print(">> Japanese List Song")
                print(" ")
                print(f"Total Songs = {len(japanese_song_list)}")
                print(" ")
                print("Judul              Penyanyi          Genre")
                print("==========================================")
                for lagu in japanese_song_list:
                    print(f"{lagu['Judul']}          {lagu['Penyanyi']}          {lagu['Genre']}")
            elif inputan_user == 2:
                try:
                    judul = input("Masukan Judul Lagu: ")
                    penyanyi = input("Masukan Penyanyi Lagu: ")
                    genre = "J-Song"
                    japanese_song_list.append({"Judul": judul, "Penyanyi": penyanyi, "Genre": genre})
                    all_song_list.append({"Judul": judul, "Penyanyi": penyanyi, "Genre": genre})
                    print("Lagu berhasil ditambahkan")
                except ValueError:
                    if judul != str and penyanyi != str and genre != str:
                        print("Inputan harus berupa huruf")
            elif inputan_user == 3:
                try:
                    print("============ Delete Japanese Song ============")
                    judul = input("Masukkan judul musik yang ingin dihapus: ")
                    hapus_lagu(japanese_song_list, judul)
                    hapus_lagu(all_song_list, judul)
                except ValueError:
                    if judul != str:
                        print("Inputan harus berupa huruf")
            elif inputan_user == 0:
                break
            else:
                print("Masukkan angka 1/2/3/0")
            
                    
    def korean_song(self):
        while True:
            inputan_user = song_menu()
            if inputan_user == 1:
                print(">> Korean List Song")
                print(" ")
                print(f"Total Songs = {len(korean_song_list)}")
                print(" ")
                print("Judul              Penyanyi          Genre")
                print("==========================================")
                for lagu in korean_song_list:
                    print(f"{lagu['Judul']}          {lagu['Penyanyi']}          {lagu['Genre']}")
            elif inputan_user == 2:
                try:
                    judul = input("Masukan Judul Lagu: ")
                    penyanyi = input("Masukan Penyanyi Lagu: ")
                    genre = "K-Song"
                    korean_song_list.append({"Judul": judul, "Penyanyi": penyanyi, "Genre": genre})
                    all_song_list.append({"Judul": judul, "Penyanyi": penyanyi, "Genre": genre})
                    print("Lagu berhasil ditambahkan")
                except ValueError:
                    if judul != str and penyanyi != str and genre != str:
                        print("Inputan harus berupa huruf")
            elif inputan_user == 3:
                    try:
                        print("============ Delete Korean Song ============")
                        judul = input("Masukkan judul musik yang ingin dihapus: ")
                        hapus_lagu(korean_song_list, judul)
                        hapus_lagu(all_song_list, judul)
                    except ValueError:
                        if judul != str:
                            print("Inputan harus berupa huruf")
            elif inputan_user == 0:
                break
            else:
                print("Masukkan angka 1/2/3/0")
    
    def english_song(self):
        while True:
            inputan_user = song_menu()
            if inputan_user == 1:
                print(">> English List Song")
                print(" ")
                print(f"Total Songs = {len(english_song_list)}")
                print(" ")
                print("Judul              Penyanyi          Genre")
                print("==========================================")
                for lagu in english_song_list:
                    print(f"{lagu['Judul']}          {lagu['Penyanyi']}          {lagu['Genre']}")
            elif inputan_user == 2:
                try:
                    judul = input("Masukan Judul Lagu: ")
                    penyanyi = input("Masukan Penyanyi Lagu: ")
                    genre = "E-Song"
                    english_song_list.append({"Judul": judul, "Penyanyi": penyanyi, "Genre": genre})
                    all_song_list.append({"Judul": judul, "Penyanyi": penyanyi, "Genre": genre})
                    print("Lagu berhasil ditambahkan")
                except ValueError:
                    if judul != str and penyanyi != str and genre != str:
                        print("Inputan harus berupa huruf")
            elif inputan_user == 3:
                    try:
                        print("============ Delete English Song ============")
                        judul = input("Masukkan judul musik yang ingin dihapus: ")
                        hapus_lagu(english_song_list, judul)
                        hapus_lagu(all_song_list, judul)
                    except ValueError:
                        if judul != str:
                            print("Inputan harus berupa huruf")
            elif inputan_user == 0:
                break
            else:
                print("Masukkan angka 1/2/3/0")
                
    def search_musik(self):
        input_penyanyi = input("Masukkan Penyanyi yg Ingin Di Cari: ")
        cari_lagu(all_song_list, input_penyanyi)
            

coba = Music("judul", "penyanyu", "genre")

def main():
    while True:
        inputan1 = main_menu()
        if inputan1 == 1:
            coba.japanese_song()
        elif inputan1 == 2:
            coba.korean_song()
        elif inputan1 == 3:
            coba.english_song()
        elif inputan1 == 4:
            coba.display_all()
        elif inputan1 == 5:
            coba.search_musik()
        elif inputan1 == 0:
            break
        else:
            print("Masukkan angka 1/2/3/0")
            
main()
