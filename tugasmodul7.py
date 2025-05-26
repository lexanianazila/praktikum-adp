
print("""
pilihannya ini yaa :
1. Tabel Perkalian Modulo n
2. Menghitung Jumlah Σx
3. Menghitung Faktorial n!
4. Menghitung Total dan Rata-rata Data
5. Keluar
""")

while True :

    pilihan_menu = int(input("pilihan menu km = "))

    if pilihan_menu==1 :
        print ('')
        def tabel_perkalian_modulo():
            while True:
                n = int(input("input nilai n nya yaa (0 < n ≤ 10): "))
                if 0 < n <= 10:
                    break
                else:
                    print("error babe, input lgi yaa")
            print(f"tabel perkalian modulo n = {n} :")
            print("  |", end="")
            for i in range(n):
                print(f"{i:>3}", end="")
            print ('')
            print( "----" * (n))
            for i in range(n):
                print(f"{i:>2}|", end="")
                for j in range(n):
                    perkalian_modulo = (i * j) % n
                    print(f"{perkalian_modulo:>3}", end="")
                print()
        tabel_perkalian_modulo()

        print ('')
    
    elif pilihan_menu==2 :
        print ('')
        def hitung_sigma_x():
            while True:
                batas_bawah = int(input("batas bawah: "))
                batas_atas = int(input("batas atas: "))
                if batas_atas < batas_bawah:
                    print("batas atasnya tu harus lebih besar dari batas bawah yaa, input ulang lgi yukk")
                else:
                    break
            counter = 0
            for x in range(batas_bawah, batas_atas + 1):
                counter += x
            print ('\n')
            print(f"nah jadii Σx dari {batas_bawah} sampai {batas_atas} nya {counter}")
        hitung_sigma_x()

        print ('')

    elif pilihan_menu==3 :
        print('')
        def hitung_faktorial():
            while True:
                n = int(input("input dulu nilai n nya (n ≥ 0): "))
                if n < 0:
                    print("n nya harus ≥ 0 yaa, input ulang oke?")
                else:
                    break
            faktorial = 1
            for i in range(1, n + 1):
                faktorial *= i
            print(f"{n}! = {faktorial}")
        hitung_faktorial()

        print ('')

    elif pilihan_menu==4 :
        def total_dan_rata_rata():
            while True:
                n = int(input("banyak data (n): "))
                if n <= 0:
                    print("jumlah data harus lebih dari 0 yaa, ulang lgi inputnya")
                else:
                    break
            data = []
            for i in range(n):
                while True:
                    nilai = float(input(f"Data ke-{i+1}: "))
                    data.append(nilai)
                    break
            total = sum(data)
            rata_rata = total / n
            print('')
            print("Data yang dimasukkan:")
            print("-" * 22)
            print("| No |     Nilai     |")
            print("-" * 22)
            for i in range(len(data)):
                print(f"| {i+1:<2} | {data[i]:^13} |")
            print("-" * 22)
            print(f"Total     = {total}")
            print(f"Rata-rata = {rata_rata}")
        total_dan_rata_rata()

        print ('')

    elif pilihan_menu==5 :
        print("thankyou dah make program soft spoken ini yaa")
        break

    else :
        print("pilihannya cm ampe 5, ulg lgi yaa")
        print ('')
    