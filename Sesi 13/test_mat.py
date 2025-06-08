import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("filexlsx/data-score-group.xlsx")
grade_counts = df['Grade'].value_counts().sort_index()

# Membuat diagram batang
grades = list(grade_counts.keys())
counts = list(grade_counts.values())

plt.figure(figsize=(8, 5))
plt.bar(grades, counts, color='skyblue', edgecolor='black')

plt.title("Distribusi Grade Mahasiswa")
plt.xlabel("Grade")
plt.ylabel("Jumlah Mahasiswa")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
