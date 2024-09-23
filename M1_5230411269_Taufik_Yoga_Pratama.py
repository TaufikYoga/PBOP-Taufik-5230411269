# Menghitung luas bangun tabung

def hitung_luas_tabung(r, t):
    pi = 3.14
    result = 2 * pi * r * (r + t)
    return result

tabung = hitung_luas_tabung(7, 10)
print(f"Luas tabung: {tabung}")