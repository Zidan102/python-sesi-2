import pandas as pd

# Baca file Excel
score = pd.read_excel("filexlsx/data-score.xlsx")

# Periksa daftar kolom yang ada dalam file Excel
print(score.columns)

# Periksa beberapa baris pertama dari file Excel
print(score.head())

# Pastikan bahwa nama kolom "Score" sesuai dengan yang digunakan dalam kode Python
if "Score" in score.columns:
    score['new_score'] = score["Score"].apply(updateScore)
    score['grade'] = score['new_score'].apply(grade)
    score.to_excel("filexlsx/data-score-updated.xlsx", index=False)
else:
    print("Kolom 'Score' tidak ada dalam file Excel.")
