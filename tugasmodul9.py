
import time, os
from termcolor import colored

def happy_eid(teks, panjang=30, langkah=20, durasi=20):
    warna = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    isi = ' ' * panjang + teks + ' ' * panjang
    indeks = list(range(len(isi) - panjang)) + list(range(len(isi) - panjang, -1, -1))
    jeda = durasi / langkah
    for i in indeks[:langkah]:
        os.system('cls')
        gerak = isi[i:i + panjang]
        baris = ''
        warna_tiap_huruf = 0
        for j in gerak:
            baris += colored(j, warna[warna_tiap_huruf % len(warna)])
            warna_tiap_huruf += 1
        print(baris)
        time.sleep(jeda)

happy_eid("Happy Eid", panjang=30, langkah=20, durasi=20)
