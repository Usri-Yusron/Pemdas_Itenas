import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# jawaban pertanyaan 1
# membuat fungsi lambda dan menaruhnya di dalam variabel
Peningkatan_Gaji = lambda x: x * 0.05

# Loop for untuk mengaplikasikan fungsi lambda pada setiap baris DataFrame
for index, row in df.iterrows():
    df.at[index, 'Peningkatan Gaji'] = Peningkatan_Gaji(row['Gaji'])  
    
# jawaban pertanyaan 2
for index, row in df.iterrows():
    df.at[index, 'Ringkasa perubahan'] = 'Gaji Setelah dikali dengan 5 (5% = 0,05)'
print(df)
    
# # jawaban pertanyaan 3 dan 4
# Membuat kolom baru 'Gaji Baru' dengan kondisi berdasarkan 'Usia'
df['Gaji Baru'] = df.apply(lambda x: x['Peningkatan Gaji'] * 2 if x['Usia'] > 30 else x['Peningkatan Gaji'] * 1, axis=1)
print(df)