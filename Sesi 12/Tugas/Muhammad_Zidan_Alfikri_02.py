import pandas as pd

df = pd.read_excel('Sesi 12/Tugas/data_penjualan.xlsx')
df["Total Harga"] = df["Harga Satuan"] * df["Jumlah"]
df.to_excel('Sesi 12/Tugas/data_penjualan_updated_Total.xlsx', index=False)
print(df)