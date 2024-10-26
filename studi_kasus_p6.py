class Order:
    def __init__(self, id, name, details):
        self._id = id
        self.name = name
        self.details = details

    def set_order(self, name: str, details: str):
        self.name = name
        self.details = details

    def get_order_details(self) -> str:
        return f"ID Pesanan: {self._id}, Nama Pesanan: {self.name}, Rincian: {self.details}"

    def get_id(self) -> int:
        return self._id


class Delivery(Order):
    def __init__(self, id, order: Order, information, date, address):
        self._id = id
        self.order = order  
        self.information = information
        self.date = date
        self.address = address

    def process_delivery(self):
        print(f"Memproses pengiriman untuk {self.order.name} ke {self.address} pada tanggal {self.date}.")

    def get_delivery_info(self) -> str:
        return (f"ID Pengiriman: {self._id}, "
                f"Nama Pesanan: {self.order.name}, "
                f"Informasi: {self.information}, "
                f"Tanggal: {self.date}, "
                f"Alamat: {self.address}")

    def get_id(self) -> int:
        return self._id


def main_menu():
    orders = []
    deliveries = []
    while True:
        print("\n=== Menu ===")
        print("1. Buat Pesanan")
        print("2. Buat Pengiriman")
        print("3. Proses Pengiriman")
        print("4. Lihat Rincian Pesanan")
        print("5. Lihat Semua Pesanan")
        print("6. Lihat Semua Pengiriman")
        print("7. Keluar")
        
        try:
            choice = input("Pilih opsi: ")
            
            if choice == '1':
                id = len(orders) + 1
                name = input("Masukkan nama pesanan: ")
                details = input("Masukkan rincian pesanan: ")
                orders.append(Order(id, name, details))
                print("Pesanan berhasil dibuat.")
            
            elif choice == '2':
                if not orders:
                    print("Tidak ada pesanan yang tersedia. Buat pesanan terlebih dahulu.")
                    continue
                
                order_id = int(input("Masukkan ID pesanan untuk pengiriman: ")) - 1
                if 0 <= order_id < len(orders):
                    id = len(deliveries) + 1
                    information = input("Masukkan informasi pengiriman: ")
                    date = input("Masukkan tanggal pengiriman: ")
                    address = input("Masukkan alamat pengiriman: ")
                    deliveries.append(Delivery(id, orders[order_id], information, date, address))
                    print("Pengiriman berhasil dibuat.")
                else:
                    print("ID pesanan tidak valid.")
            
            elif choice == '3':
                delivery_id = int(input("Masukkan ID pengiriman: ")) - 1
                
                if 0 <= delivery_id < len(deliveries):
                    deliveries[delivery_id].process_delivery()
                else:
                    print("ID pengiriman tidak valid.")
            
            elif choice == '4':
                order_id = int(input("Masukkan ID pesanan: ")) - 1
                
                if 0 <= order_id < len(orders):
                    print(orders[order_id].get_order_details())
                else:
                    print("ID pesanan tidak valid.")
            
            elif choice == '5':
                print("\n=== Semua Pesanan ===")
                for order in orders:
                    print(f"ID Pesanan: {order.get_id()}, Nama: {order.name}")
            
            elif choice == '6':
                print("\n=== Semua Pengiriman ===")
                for delivery in deliveries:
                    print(delivery.get_delivery_info())
            
            elif choice == '7':
                print("Keluar")
                break
            
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang benar.")

main_menu()
