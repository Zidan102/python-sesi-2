nilai = int(input('Masukan nilai: '))

if nilai >= 85:
    grade = "A"
if nilai >= 75:
    grade = "B"
if nilai >= 65:
    grade = "C"
if nilai >= 55:
    grade = "D"

print('dengan nilai %s maka grade kmu adalah %' %(nilai, grade))