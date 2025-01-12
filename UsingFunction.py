# Mini Project - Kalkulator Bangun Datar dan Bangun Ruang (Using Function)
# by Nadhif Rif'at Rasendriya

def kalkulator_bangun_datar():
    print("\nOperasi Bangun Datar:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Jajar Genjang")
    print("5. Lingkaran")
    print("6. Trapesium")
    print("7. Belah Ketupat")
    print("8. Layang-Layang")
    
    operasi = int(input("\nPilih operasi (1-8): "))

    if operasi == 1:
        sisi = float(input("Masukkan panjang sisi: "))
        print(f"Luas Persegi: {luas_persegi(sisi)}")

    elif operasi == 2:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        print(f"Luas Persegi Panjang: {luas_persegi_panjang(panjang, lebar)}")

    elif operasi == 3:
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        print(f"Luas Segitiga: {luas_segitiga(alas, tinggi)}")

    elif operasi == 4:
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        print(f"Luas Jajar Genjang: {luas_jajar_genjang(alas, tinggi)}")

    elif operasi == 5:
        jari_jari = float(input("Masukkan jari-jari: "))
        print(f"Luas Lingkaran: {luas_lingkaran(jari_jari)}")

    elif operasi == 6:
        sisi_atas = float(input("Masukkan panjang sisi atas: "))
        sisi_bawah = float(input("Masukkan panjang sisi bawah: "))
        tinggi = float(input("Masukkan tinggi: "))
        print(f"Luas Trapesium: {luas_trapesium(sisi_atas, sisi_bawah, tinggi)}")

    elif operasi == 7 or operasi == 8:
        diagonal1 = float(input("Masukkan panjang diagonal pertama: "))
        diagonal2 = float(input("Masukkan panjang diagonal kedua: "))
        print(f"Luas Bangun: {luas_diagonal(diagonal1, diagonal2)}")

    else:
        print("Operasi tidak valid!")

def kalkulator_bangun_ruang():
    print("\nOperasi Bangun Ruang:")
    print("1. Kubus")
    print("2. Balok")

    operasi = int(input("\nPilih operasi (1/2): "))

    if operasi == 1:
        sisi = float(input("Masukkan panjang sisi: "))
        print(f"Volume Kubus: {volume_kubus(sisi)}")

    elif operasi == 2:
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        print(f"Volume Balok: {volume_balok(panjang, lebar, tinggi)}")

    else:
        print("Operasi tidak valid!")

# Function
def luas_persegi(sisi):
    return sisi * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi

def luas_lingkaran(jari_jari):
    return 3.14 * jari_jari**2

def luas_trapesium(sisi_atas, sisi_bawah, tinggi):
    return 0.5 * (sisi_atas + sisi_bawah) * tinggi

def luas_diagonal(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2


def volume_kubus(sisi):
    return sisi**3

def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

print("Kalkulator Bangun Datar dan Bangun Ruang!")
print('''Pilih Kategori: 
      1. Bangun Datar
      2. Bangun Ruang''')

kategori = int(input("Pilihanmu: "))

if kategori == 1:
    kalkulator_bangun_datar()
elif kategori == 2:
    kalkulator_bangun_ruang()
else:
    print("Kategori tidak valid!")
