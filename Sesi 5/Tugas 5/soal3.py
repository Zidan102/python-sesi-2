nilai = int(input("masukan nilai ujian kamu: "))
if nilai >80 and nilai <= 100:
    a = "A"
    print("Grade kamu adalah %s, karena nilai kamu %s" % (a, nilai))
elif nilai >= 70 and nilai <= 79:
    b = "B"
    print("Grade kamu adalah %s, karena nilai kamu %s" % (b, nilai))
elif nilai >= 60 and nilai <=69:
    c = "C"
    print("Grade kamu adalah %s, karena nilai kamu %s" % (c, nilai))
elif nilai >= 50 and nilai <= 59:
    d = "D"
    print("Grade kamu adalah %s, karena nilai kamu %s" % (d, nilai))
else:
    print("Grade kamu adalah E, karena nilai kamu %s" % (nilai))