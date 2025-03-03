blnj = int(input('Masukan total belanjaan: '))

if blnj >= 100000:
    dis10 = blnj * 0.10
    fnl10 = blnj - dis10
    print("Total belanjaan kmu adalah", fnl10, "karna telah mendapatkan diskon 10%")
elif blnj >= 50000:
    dis5 = blnj * 0.05
    fnl5 = blnj - dis5
    print("Total belanjaan kmu adalah", fnl5, "karna telah mendapatkan diskon 5%")
else:
    print("Total belanjaan kmu adalah %s" %(blnj))