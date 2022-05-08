import math
i = input().strip()
j = 1
sumapol = 0
while j <= int(i):
    x = []
    x.append((input().strip().split()))
    if(len(x[0]) == 1):
        r = x[0][0]
        pole = math.pi * float(r) * float(r)
    if(len(x[0]) == 2):
        a = x[0][0]
        b = x[0][1]
        pole = float(a) * float(b)
    if(len(x[0]) == 3):
        a = x[0][0]
        b = x[0][1]
        c = x[0][2]
        p = (float(a) + float(b) + float(c))/2
        pole = math.sqrt(p * (p - float(a)) * (p - float(b)) * (p - float(c)))
    if(len(x[0]) >= 4):
        sumapol = 0
        break
    sumapol = sumapol + pole
    j += 1
    
if(sumapol == 0): print("Błąd: można podać maksymalnie 3 liczby")
else: print(round(sumapol, 1))