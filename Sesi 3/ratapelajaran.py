nilai = 0;
nilai2 = []
nama = input('Masukan nama: ')
p1 = int(input('Masukan nilai pelajaran IPA: '))
nilai += p1
nilai2.append(int(p1))
p2 = int(input('Masukan nilai pelajaran IPS: '))
nilai += p2
nilai2.append(int(p2))
p3 = int(input('Masukan nilai pelajaran MTK: '))
nilai += p3
nilai2.append(int(p3))
p4 = int(input('Masukan nilai pelajaran English: '))
nilai += p4
nilai2.append(int(p4))
p5 = int(input('Masukan nilai pelajaran Indonesia: '))
nilai += p5
nilai2.append(int(p5))

rata2 = nilai / 5
print('Nilai rata rata', nama, 'adalah', rata2)

if rata2 < 75 or nilai2 == 100:
    print('Kamu tidak lulus')
    if p1 or p2 or p3 or p4 or p5 < 49:
        print('Kamu tidak lulus')
        if nilai2 == 100:
            print('Kamu tidak lulus')
else:
    print("Kamu tidak lulus")