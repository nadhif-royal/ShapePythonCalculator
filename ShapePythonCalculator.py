# Mini Project - Kalkulator Bangun Datar dan Bangun Ruang
# by Nadhif Rif'at Rasendriya

print("Kalkulator Bangun Datar dan Bangun Ruang!")
print('''Pilih Kategori: 
      1. Bangun Datar
      2. Bangun Ruang''')

kategori = int(input("Pilihanmu: "))

if kategori == 1:
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
        luas = sisi * sisi
        print(f"Luas Persegi: {luas}")

    elif operasi == 2:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        luas = panjang * lebar
        print(f"Luas Persegi Panjang: {luas}")

    elif operasi == 3:
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = 0.5 * alas * tinggi
        print(f"Luas Segitiga: {luas}")

    elif operasi == 4:
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = alas * tinggi
        print(f"Luas Jajar Genjang: {luas}")

    elif operasi == 5:
        jari_jari = float(input("Masukkan jari-jari: "))
        luas = 3.14 * jari_jari**2
        print(f"Luas Lingkaran: {luas}")

    elif operasi == 6:
        sisi_atas = float(input("Masukkan panjang sisi atas: "))
        sisi_bawah = float(input("Masukkan panjang sisi bawah: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
        print(f"Luas Trapesium: {luas}")

    elif operasi == 7:
        diagonal1 = float(input("Masukkan panjang diagonal pertama: "))
        diagonal2 = float(input("Masukkan panjang diagonal kedua: "))
        luas = 0.5 * diagonal1 * diagonal2
        print(f"Luas Belah Ketupat: {luas}")

    elif operasi == 8:
        diagonal1 = float(input("Masukkan panjang diagonal pertama: "))
        diagonal2 = float(input("Masukkan panjang diagonal kedua: "))
        luas = 0.5 * diagonal1 * diagonal2
        print(f"Luas Layang-Layang: {luas}")

    else:
        print("Error!")

elif kategori == 2:
    print("\nOperasi Bangun Ruang:")
    print("1. Kubus")
    print("2. Balok")

    operasi = input("\nPilih operasi (1/2): ")

    if operasi == "1":
        sisi = float(input("Masukkan panjang sisi: "))
        volume = sisi**3
        print(f"Volume Kubus: {volume}")

    elif operasi == "2":
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        volume = panjang * lebar * tinggi
        print(f"Volume Balok: {volume}")
      
    else:
        print("Error!")

else:
    print("Error!")
