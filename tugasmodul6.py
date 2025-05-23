
titik = []

print("masukkan titik koordinat")
for i in range(3):
    x = float(input(f"x{i+1}: "))
    y = float(input(f"y{i+1}: "))
    titik.append((x, y))

print("ada tiga titik, yaitu :", titik)

ab = ((titik[1][0] - titik[0][0])**2 + (titik[1][1] - titik[0][1])**2)**0.5
bc = ((titik[2][0] - titik[1][0])**2 + (titik[2][1] - titik[1][1])**2)**0.5
ac = ((titik[2][0] - titik[0][0])**2 + (titik[2][1] - titik[0][1])**2)**0.5

if ab==bc or bc==ac or ab==ac :
    print("ketiga titik tersebut membentuk segitiga sama kaki")
else :
    print("ketiga titik tersebut tidak membentuk segitiga sama kaki")