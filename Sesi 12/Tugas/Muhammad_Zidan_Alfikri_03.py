import pandas as pd

df = pd.read_excel('Sesi 12/Tugas/data_penjualan.xlsx')
df_elektronik = df[df['Kategori'] == 'Elektronik']
df_elektronik.to_excel('Sesi 12/Tugas/elektronik.xlsx', index=False)