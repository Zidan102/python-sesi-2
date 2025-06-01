import pandas as pd

df = pd.read_excel('Sesi 12/Tugas/data_penjualan.xlsx')
df["Total Harga"] = df["Harga Satuan"] * df["Jumlah"]
rekap = df.groupby("Kategori")["Total Harga"].sum().reset_index()
rekap.columns = ["Kategori", "Total Penjualan"]
rekap.to_excel("Sesi 12/Tugas/rekap_penjualan.xlsx", index=False)