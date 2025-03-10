

print ('\n')
print(
    """ DAFTAR PAKET MAKANAN
    ze's caffe
    ayam : 20000
    sapi : 35000
    cumi cumi : 45000
    """
    )
print ('\n')

nama = str(input("pesanan atas nama = "))
pesanan = str(input("paket makanan yang diinginkan (ayam/sapi/cumi) = ")).lower()
jmlh = int(input("jumlah paket = " ))
harga_ayam = jmlh*20000
harga_sapi = jmlh*35000
harga_cumi_cumi = jmlh*45000
ongkir_1 = 0
ongkir_2 = 7000
ongkir_3 = 15000

if pesanan==(f"ayam") :
    print("harga pesanan =", harga_ayam)
elif pesanan==(f"sapi") :
    print("harga pesanan =", harga_sapi)
elif pesanan==(f"cumi") :
    print("harga pesanan =", harga_cumi_cumi)

jarak = float(input("jarak lokasi ke outlet = "))

if jarak<1 and pesanan==(f"ayam") :
    print("ongkir = ", ongkir_1)
elif 1<=jarak<=3 and pesanan==(f"ayam") :
    print("ongkir = ", ongkir_2)
elif jarak>3 and pesanan==(f"ayam") :
    print("ongkir = ", ongkir_3)
elif jarak<1 and pesanan==(f"sapi") :
    print("ongkir = ", ongkir_1)
elif 1<=jarak<=3 and pesanan==(f"sapi") :
    print("ongkir = ", ongkir_2)
elif jarak>3 and pesanan==(f"sapi") :
    print("ongkir = ", ongkir_3)
elif jarak<1 and pesanan==(f"cumi") :
    print("ongkir = ", ongkir_1)
elif 1<=jarak<=3 and pesanan==(f"cumi") :
    print("ongkir = ", ongkir_2)
elif jarak>3 and pesanan==(f"cumi") :
    print("ongkir = ", ongkir_3)

if jarak<1 and pesanan==(f"ayam") :
    print("total pesanan = ", harga_ayam+0)
elif 1<=jarak<=3 and pesanan==(f"ayam") :
    print("total pesanan = ", harga_ayam+7000)
elif jarak>3 and pesanan==(f"ayam") :
    print("total pesanan = ", harga_ayam+15000)
elif jarak<1 and pesanan==(f"sapi") :
    print("total pesanan = ", harga_sapi+0)
elif 1<=jarak<=3 and pesanan==(f"sapi") :
    print("total pesanan = ", harga_sapi+7000)
elif jarak>3 and pesanan==(f"sapi") :
    print("total pesanan = ", harga_sapi+15000)
elif jarak<1 and pesanan==(f"cumi") :
    print("total pesanan = ", harga_cumi_cumi+0)
elif 1<=jarak<=3 and pesanan==(f"cumi") :
    print("total pesanan = ", harga_cumi_cumi+7000)
elif jarak>3 and pesanan==(f"cumi") :
    print("total pesanan = ", harga_cumi_cumi+15000) 

print ('\n')

print(
    """
===========================
    STRUK PEMBELANJAAN
        ze's caffe
===========================
"""
)
print(" nama = ", nama)
print(" pilihan pesanan = ", pesanan)
print(" jumlah pesanan =", jmlh)
if pesanan==(f"ayam") :
    print(" harga pesanan =", harga_ayam)
elif pesanan==(f"sapi") :
    print(" harga pesanan =", harga_sapi)
elif pesanan==(f"cumi_cumi") :
    print(" harga pesanan =", harga_cumi_cumi)
print(" jarak ke outlet = ", jarak)
if jarak<1 and pesanan==(f"ayam") :
    print(" ongkir = ", ongkir_1)
elif 1<=jarak<=3 and pesanan==(f"ayam") :
    print(" ongkir = ", ongkir_2)
elif jarak>3 and pesanan==(f"ayam") :
    print(" ongkir = ", ongkir_3)
elif jarak<1 and pesanan==(f"sapi") :
    print(" ongkir = ", ongkir_1)
elif 1<=jarak<=3 and pesanan==(f"sapi") :
    print(" ongkir = ", ongkir_2)
elif jarak>3 and pesanan==(f"sapi") :
    print(" ongkir = ", ongkir_3)
elif jarak<1 and pesanan==(f"cumi") :
    print(" ongkir = ", ongkir_1)
elif 1<=jarak<=3 and pesanan==(f"cumi") :
    print(" ongkir = ", ongkir_2)
elif jarak>3 and pesanan==(f"cumi") :
    print(" ongkir = ", ongkir_3)
if jarak<1 and pesanan==(f"ayam") :
    print(" total pesanan = ", harga_ayam+0)
elif 1<=jarak<=3 and pesanan==(f"ayam") :
    print(" total pesanan = ", harga_ayam+7000)
elif jarak>3 and pesanan==(f"ayam") :
    print(" total pesanan = ", harga_ayam+15000)
elif jarak<1 and pesanan==(f"sapi") :
    print(" total pesanan = ", harga_sapi+0)
elif 1<=jarak<=3 and pesanan==(f"sapi") :
    print(" total pesanan = ", harga_sapi+7000)
elif jarak>3 and pesanan==(f"sapi") :
    print(" total pesanan = ", harga_sapi+15000)
elif jarak<1 and pesanan==(f"cumi") :
    print(" total pesanan = ", harga_cumi_cumi+0)
elif 1<=jarak<=3 and pesanan==(f"cumi") :
    print(" total pesanan = ", harga_cumi_cumi+7000)
elif jarak>3 and pesanan==(f"cumi") :
    print(" total pesanan = ", harga_cumi_cumi+15000) 
print(
    """
============================
terimakasih telah berbelanja
      di caffe kami ><
         ze's caffe
============================
"""
)
