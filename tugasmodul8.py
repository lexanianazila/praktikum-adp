def baca(data_praktikan):
    praktikan = {}
    with open(data_praktikan, "r") as file_yg_dibaca:
        for baris in file_yg_dibaca:
            kata_sementara = ""
            list_kata = []
            for karakter in baris:
                if karakter == "," or karakter == "\n":
                    if kata_sementara != "":
                        list_kata.append(kata_sementara.strip())
                        kata_sementara = ""
                else:
                    kata_sementara += karakter
            if len(list_kata) == 5:
                nim, nama, pretest, posttest, tugas = list_kata
                praktikan[nim] = {
                    "nama": nama,
                    "pretest": float(pretest),
                    "posttest": float(posttest),
                    "tugas": float(tugas)
                }
    return praktikan

def hitung_simpan_data(praktikan, nama_file):
    for data in praktikan.values():
        data["total"] = data["pretest"] * 0.35 + data["posttest"] * 0.35 + data["tugas"] * 0.30
    with open(nama_file, "w") as file_tulis:
        for nim, data in praktikan.items():
            file_tulis.write(
                f"{nim},{data['nama']},{data['pretest']},{data['posttest']},{data['tugas']},{data['total']:.2f}\n"
            )

def nilai_akhir(praktikan):
    nilai_total = []
    for data in praktikan.values():
        nilai_total.append(data["total"])
    tertinggi = max(nilai_total)
    terendah = min(nilai_total)
    rata = sum(nilai_total) / len(nilai_total)
    nim_tertinggi = nim_terendah = None
    rata_terakhir = 0
    for nim, data in praktikan.items():
        total = data["total"]
        if total == tertinggi:
            nim_tertinggi = nim
        if total == terendah:
            nim_terendah = nim
        if total < rata:
            rata_terakhir += 1
    print(f"Praktikan dengan nilai tertinggi yaitu {praktikan[nim_tertinggi]['nama']} ({nim_tertinggi}) dengan nilai {tertinggi:.2f}")
    print(f"Sedangkan praktikan dengan nilai terendah yaitu {praktikan[nim_terendah]['nama']} ({nim_terendah}) dengan nilai {terendah:.2f}")
    print(f"Rata-rata nilai akhir semua praktikan yaitu {rata:.2f}")
    print(f"Banyak praktikan yang mendapat nilai di bawah rata-rata ada {rata_terakhir} praktikan")

data_para_praktikan = baca("data_pratikan.txt")
hitung_simpan_data(data_para_praktikan, "data_nilai_akhir.txt")
nilai_akhir(data_para_praktikan)
