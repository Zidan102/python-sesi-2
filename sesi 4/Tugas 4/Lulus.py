n1 = int(input("Masukan nilai pertama: "))
n2 = int(input("Masukan nilai ke2: "))
n3 = int(input("Masukan nilai ke3: "))

rata_rata = (n1 + n2 + n3) / 3
bawah_70 = 0;
nilai_sempurna = 0;

if n1 == 100:
    nilai_sempurna += 1
if n2 == 100:
    nilai_sempurna += 1
if n3 == 100:
    nilai_sempurna += 1
if n1 < 70:
    bawah_70 += 1
if n2 < 70:
    bawah_70 += 1
if n3 < 70:
    bawah_70 += 1

if rata_rata >= 75:
    print('Kamu lulus dengan nilai rata rata %s' % (rata_rata))
elif nilai_sempurna >= 1:
    print("Kamu lulus dengan %s nilai sempurna" % (nilai_sempurna))
elif bawah_70 < 1:
    print('Kamu lulus dengan %s nilai dibawah 70' % (bawah_70))

else:
    print("Kamu tidak lulus")