
counter = 0
n = int(input("masukkan nilai n (minimal n = 4) = "))
while n < 4 :
    print("error")
    n = int(input("masukkan nilai n (minimal n = 4) = "))

for i in range(n):
    for j in range(n):
        if n % 2 != 0 and i == n // 2 and j == n // 2 :
            print("HORE", end="\t")
        elif i == j:
            print("1", end="\t")
        elif i + j == n - 1:
            print("2", end="\t")
        else:
            print("BOOM", end="\t")
            counter += 1
    print("")
print("total BOOM =", counter)
