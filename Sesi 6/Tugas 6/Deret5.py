a = b = 1

for i in range(8):
    print(a,end=" ")
    if i >= 1:
        a, b = b, a+b