import tkinter as tk
from tkinter import ttk

class AplikasiStopwatch:
    def __init__(self, root):

        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("350x200")


        self.waktu_berjalan = 0
        self.sedang_berjalan = False


        self.label_waktu = tk.Label(self.root, text="0:00:00", font=("Helvetica", 30))  
        self.label_waktu.pack(pady=20)


        bingkai_tombol = tk.Frame(self.root)
        bingkai_tombol.pack(pady=20)


        self.tombol_mulai = ttk.Button(bingkai_tombol, text="Mulai", command=self.mulai)
        self.tombol_mulai.grid(row=0, column=0, padx=10)


        self.tombol_berhenti = ttk.Button(bingkai_tombol, text="Berhenti", command=self.berhenti)
        self.tombol_berhenti.grid(row=0, column=1, padx=10)


        self.tombol_reset = ttk.Button(bingkai_tombol, text="Reset", command=self.reset)
        self.tombol_reset.grid(row=0, column=2, padx=10)


    def perbarui_waktu(self):
        if self.sedang_berjalan:
            self.waktu_berjalan += 1
            menit, detik = divmod(self.waktu_berjalan, 60)
            jam, menit = divmod(menit, 60)
            self.label_waktu.config(text=f"{jam}:{menit:02}:{detik:02}")
            self.root.after(1000, self.perbarui_waktu)


    def mulai(self):
        if not self.sedang_berjalan:
            self.sedang_berjalan = True
            self.perbarui_waktu()


    def berhenti(self):
        self.sedang_berjalan = False


    def reset(self):
        self.sedang_berjalan = False
        self.waktu_berjalan = 0
        self.label_waktu.config(text="0:00:00")


if __name__ == "__main__":
    root = tk.Tk()
    aplikasi = AplikasiStopwatch(root)
    root.mainloop()

