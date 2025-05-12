
print ('\n')
nilai_x = list(range(-7,8))
fungsi_f = []
for i in nilai_x :
    if x>0 :
        fungsi_f.append(x**3-x)
    elif x<0 :
        fungsi_f.append(1/x**2)
    else :
        fungsi_f.append(1)
print("|-----|------------------------|")
print("|  x  |          f(x)          |")
print("|-----|------------------------|")
for i in range(len(nilai_x)) :
    print(f"| {nilai_x[i] : 3} | {fungsi_f[i] : 22} |")
print("|-----|------------------------|")