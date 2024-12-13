import mysql.connector

# ========== Step 1 membuat database ==========

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = ""
# )

# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE penjualan")

# ========== Step 2 membuat tabel tabel ==========

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "penjualan"
# )

# mycursor = mydb.cursor()

# Untuk tabel tarnsaksi
# mycursor.execute("CREATE TABLE transaksi (no_transaksi VARCHAR(20) NOT NULL PRIMARY KEY, detail_transaksi TEXT, nik VARCHAR(16), kode_produk VARCHAR(10))")

# Untuk tabel prduk
# mycursor.execute("CREATE TABLE produk (kode_produk VARCHAR(10) NOT NULL PRIMARY KEY, nama_produk VARCHAR(50), harga DECIMAL(10,2), jenis_produk VARCHAR(30))")

# Untuk tabel struk
# mycursor.execute("CREATE TABLE struk (no_struk VARCHAR(20) NOT NULL PRIMARY KEY, nama_pegawai VARCHAR(50), no_transaksi VARCHAR(20), nama_produk VARCHAR(50), jumlah_produk INT, total_harga DECIMAL(10,2))")

# Untuk tabel pegawai
# mycursor.execute("CREATE TABLE pegawai (nik VARCHAR(16) NOT NULL PRIMARY KEY, nama VARCHAR(50), alamat VARCHAR(100))")

# ========== Step 3 membuat relasi antar tabel ==========

# Relasi tabel pegawai dengan tabel transaksi
# mycursor.execute("ALTER TABLE transaksi ADD FOREIGN KEY (nik) REFERENCES pegawai (nik)")

# Relasi tabel struk dengan tabel transaksi
# mycursor.execute("ALTER TABLE struk ADD FOREIGN KEY (no_transaksi) REFERENCES transaksi (no_transaksi)")

# Relasi tabel struk dengan tabel transaksi
# mycursor.execute("ALTER TABLE transaksi ADD FOREIGN KEY (kode_produk) REFERENCES produk (kode_produk)")

# ========== Step 4 membuat program ==========

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="penjualan"
)

cursor = db.cursor()

# Fungsi untuk menambahkan transaksi
def tambah_transaksi():
    # Note: sudah ada data dummy pada tabel pegawai, struk, dan produk
    nik = input("Masukkan NIK Pegawai: ")
    kode_produk = input("Masukkan Kode Produk: ")
    no_transaksi = input("Masukkan Nomor Transaksi: ")
    detail_transaksi = input("Masukkan Detail Transaksi: ")

    try:
        query = "INSERT INTO transaksi (nik, kode_produk, no_transaksi, detail_transaksi) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nik, kode_produk, no_transaksi, detail_transaksi))
        db.commit()
        print("Transaksi berhasil ditambahkan!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Fungsi untuk membaca semua transaksi
def display_transaksi():
    try:
        query = "SELECT * FROM transaksi"
        cursor.execute(query)
        results = cursor.fetchall()
        if cursor.rowcount == 0:
            print("Tidak ada data transaksi.")
        else:
            print("Data Transaksi:")
            for row in results:
                print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Fungsi untuk memperbarui transaksi
def update_transaksi():
    no_transaksi = input("Masukkan Nomor Transaksi yang ingin diubah: ")
    detail_transaksi = input("Masukkan Detail Transaksi baru: ")

    try:
        query = "UPDATE transaksi SET detail_transaksi = %s WHERE no_transaksi = %s"
        cursor.execute(query, (detail_transaksi, no_transaksi))
        db.commit()
        if cursor.rowcount > 0:
            print("Transaksi berhasil diperbarui!")
        else:
            print("Nomor Transaksi tidak ditemukan.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Fungsi untuk menghapus transaksi
def delete_transaksi():
    no_transaksi = input("Masukkan Nomor Transaksi yang ingin dihapus: ")

    try:
        query = "DELETE FROM transaksi WHERE no_transaksi = %s"
        cursor.execute(query, (no_transaksi,))
        db.commit()
        if cursor.rowcount > 0:
            print("Transaksi berhasil dihapus!")
        else:
            print("Nomor Transaksi tidak ditemukan.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


while True:
    print("\nMenu CRUD Transaksi:")
    print("1. Tambah Transaksi")
    print("2. Lihat Semua Transaksi")
    print("3. Ubah Transaksi")
    print("4. Hapus Transaksi")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        # Note: sudah ada data dummy pada tabel pegawai, struk, dan produk
        tambah_transaksi()
    elif pilihan == "2":
        display_transaksi()
    elif pilihan == "3":
        update_transaksi()
    elif pilihan == "4":
        delete_transaksi()
    elif pilihan == "5":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
