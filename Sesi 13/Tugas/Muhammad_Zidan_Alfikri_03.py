import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Sesi 13/Tugas/Data_Penduduk.xlsx')
q1 = df['Penghasilan_Per_Bulan'].quantile(0.25)
q2 = df['Penghasilan_Per_Bulan'].quantile(0.50)
q3 = df['Penghasilan_Per_Bulan'].quantile(0.75)

def kategorikan_pendapatan(pendapatan):
    if pendapatan < q1:
        return 'Sangat Rendah'
    elif q1 <= pendapatan < q2:
        return 'Rendah'
    elif q2 <= pendapatan < q3:
        return 'Menengah'
    else:
        return 'Tinggi'
    
df['Kategori_Pendapatan'] = df['Penghasilan_Per_Bulan'].apply(kategorikan_pendapatan)
kategori_pendapatan = df['Kategori_Pendapatan'].value_counts()
plt.pie(kategori_pendapatan, labels=kategori_pendapatan.index, autopct='%1.1f%%', startangle=140)
plt.title('Persentase Kategori Pendapatan Penduduk')
plt.axis('equal')
plt.show()