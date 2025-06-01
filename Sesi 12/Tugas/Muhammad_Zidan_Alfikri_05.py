import pandas as pd

df = pd.read_excel('Sesi 12/Tugas/data_penjualan_updated_Total.xlsx')
df_sorted = df.sort_values(by="Total Harga", ascending=False)
df_sorted.to_excel("Sesi 12/Tugas/data_penjualan_terurut.xlsx", index=False)