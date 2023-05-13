import pandas as pd
from datetime import datetime


def dakika_saniye_salise_to_milisaniye(veri):
    parcalar = veri.split(":")
    dakika = int(parcalar[0])
    saniye, salise = map(int, parcalar[1].split("."))
    
    milisaniye = dakika * 60 * 1000 + saniye * 1000 + salise * 10
    return milisaniye

def milisaniye_to_dakika_saniye_salise(milisaniye):
    dakika = milisaniye // 60000
    saniye = (milisaniye // 1000) % 60
    salise = (milisaniye // 10) % 100
    
    veri = "{:02d}:{:02d}.{:03d}".format(dakika, saniye, salise)
    return veri

df = pd.read_csv('izmiryarislari.csv')
df['Tarih'] = pd.to_datetime(df['Tarih'], format='%d/%m/%Y')
df = df.set_index('Tarih')
df['Ganyan'] = df['Ganyan'].str.replace('"','')
df['Ganyan'] = df['Ganyan'].str.replace(',','.').astype(float)
df['Taşıdığı Ağırlık'] = df['Taşıdığı Ağırlık'].str.replace(',','.')
df['Taşıdığı Ağırlık'] = df['Taşıdığı Ağırlık'].apply(lambda x: sum(float(i) for i in x.split('+')) if '+' in x else float(x))
df["Derece"] = df["Derece"].str.replace("0:00.00", "0:00:00")
df["Derece"] = pd.to_datetime(df["Derece"], format="%M:%S:%f").dt.time
# df["Derece"] = df["Derece"].apply(lambda x: x.minute * 60 * 1000 + x.second * 1000 + x.microsecond // 1000)


# df[['At İsmi', 'Orijin Baba', 'Orijin Anne', 'Sahip', 'İl', 'Pist Tipi', 'Grup', 'Klasifikasyon', 'Jokey', 'Antrenör']] = df[['At İsmi', 'Orijin Baba', 'Orijin Anne', 'Sahip', 'İl', 'Pist Tipi', 'Grup', 'Klasifikasyon', 'Jokey', 'Antrenör']].astype(str)

print(df.dtypes)
df[['Sıralama', 'Kulvar', 'At İsmi', 'Derece', 'Mesafe', 'Pist Tipi', 'Ganyan', 'Taşıdığı Ağırlık']].to_excel("izmiratismi.xlsx")