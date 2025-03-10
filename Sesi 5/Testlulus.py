biaya = input('Apakah sudah lunas biaya semester?(Y/T) ')
syarat_lulus = 0;
if biaya == 'y' or 'Y':
    syarat_lulus += 1
ujian = input('apa nilai rata rata ujian kmu?(A/B/C/D/E) ')
if ujian == 'A' or 'B' or 'C':
    syarat_lulus += 1
if syarat_lulus == 2:
    print('Syarat lulus kmu terpenuhi')
    print("Kamu Lulus!")
else:
    print('Kamu tidak lulus')