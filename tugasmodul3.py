
print("""
============================
mulai menggunakan kalkulator
============================
      """)

while True :
    angka_pertama = float(input("input angka pertama = "))
    angka_kedua = float(input("input angka kedua = "))

    print("""
Menu Operasi Bilangan
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian
5. Keluar
""")

    pilihan_operasi = int(input("pilihan operasi bilangan = "))

    if pilihan_operasi==1:
        hasil = angka_pertama+angka_kedua
        print("Hasil = ", hasil)
    elif pilihan_operasi==2:
        hasil = angka_pertama-angka_kedua
        print("Hasil = ", hasil)
    elif pilihan_operasi==3:
        hasil = angka_pertama*angka_kedua
        print("Hasil = ", hasil)
    elif pilihan_operasi==4:
        if angka_kedua==0 :
            print("error")
        else :
            hasil = angka_pertama/angka_kedua
            print("Hasil = ", hasil)
    elif pilihan_operasi==5:
        print("selesai menggunakan kalkulator")
        break
    else :
        print("Pilihan tidak tersedia")
    print ('\n')