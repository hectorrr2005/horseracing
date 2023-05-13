from datetime import date, timedelta
import urllib.request
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'atyarisi')
DATACSV_DIR = os.path.join(PROJECT_DIR, 'datacsv')
PROGRAMCSV_DIR = os.path.join(PROJECT_DIR, 'programcsv')


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(2022, 1, 1)
end_date = date(2023, 5, 9)

bugun = date.today().strftime("%d/%m/%Y")
#
tarihler = []
# iller = ['Adana', 'Kocaeli', 'Bursa', '%C4%B0stanbul', '%C4%B0zmir']
iller = ['%C4%B0stanbul']

def tarihliste(start_date, end_date):
    for single_date in daterange(start_date, end_date):
        tarihler.append(single_date.strftime("%d/%m/%Y"))

tarihliste(start_date, end_date)

def ikiTarihArasiDataCek(tarihler, iller):
    for tarih in tarihler:
        date_splitted = tarih.split("/")
        day = date_splitted[0]
        month = date_splitted[1]
        year = date_splitted[2]
        print(f"Gün: {day} Ay: {month} Yıl: {year}")
        for il in iller:
            url = f"https://medya-cdn.tjk.org/raporftp/TJKPDF/{year}/{year}-{month}-{day}/CSV/GunlukYarisSonuclari/{day}.{month}.{year}-{il}-GunlukYarisSonuclari-TR.csv"
            # url = "http://www.tjk.org/TR/YarisSever/Info/GetCSV/GunlukYarisSonuclari?SehirId="+ il +"&QueryParameter_Tarih="+ tarih
            dtarih = tarih.replace("/", "")
            if il == "%C4%B0stanbul":
                dosyaadi = f"csv{dtarih}istanbul.csv"
            elif il == "%C4%B0zmir":
                dosyaadi = f"csv{dtarih}izmir.csv"
            else:
                dosyaadi = f"csv{dtarih}{il}.csv"
            print(url)
            try:
                urllib.request.urlretrieve(url, os.path.join(DATACSV_DIR, dosyaadi))
            except urllib.request.HTTPError:
                continue
    print("İşlem Tamamlandı")

def ikiTarihArasiProgramCek(tarihler, iller):
    for tarih in tarihler:
        for il in iller:
            url = "http://www.tjk.org/TR/YarisSever/Info/GetCSV/GunlukYarisProgrami?SehirId="+ il +"&QueryParameter_Tarih="+ tarih
            dtarih = tarih.replace("/", "")
            dosyaadi = 'csv' + dtarih + '_' + il + '.csv'
            try:
                urllib.request.urlretrieve(url, os.path.join(PROGRAMCSV_DIR, dosyaadi))
            except urllib.request.HTTPError:
                continue
    print("İşlem Tamamlandı")

def bugunDataCek(bugun, iller):
    for il in iller:
        url = "http://www.tjk.org/TR/YarisSever/Info/GetCSV/GunlukYarisSonuclari?SehirId=" + il + "&QueryParameter_Tarih=" + bugun
        dtarih = bugun.replace("/", "")
        dosyaadi = 'csv' + dtarih + '_' + il + '.csv'
        try:
            urllib.request.urlretrieve(url, os.path.join(DATACSV_DIR, dosyaadi))
        except urllib.request.HTTPError:
            continue
    print("İşlem Tamamlandı")

def bugunProgramCek(bugun, iller):
    for il in iller:
        url = "http://www.tjk.org/TR/YarisSever/Info/GetCSV/GunlukYarisProgrami?SehirId=" + il + "&QueryParameter_Tarih=" + bugun
        dtarih = bugun.replace("/", "")

        dosyaadi = 'csv' + dtarih + '_' + il + '.csv'
        try:
            urllib.request.urlretrieve(url, os.path.join(PROGRAMCSV_DIR, dosyaadi))
        except urllib.request.HTTPError:
            print(bugun+' tarihli '+il+' kodlu il için csv bulunamadı.')
            continue
    print("İşlem Tamamlandı")


#url = "http://www.tjk.org/TR/YarisSever/Info/GetCSV/GunlukYarisSonuclari?SehirId=&QueryParameter_Tarih=22/12/2018"

#urllib.request.urlretrieve(url, 'output2.csv')
#bugunDataCek(bugun, iller)
#bugunProgramCek(bugun, iller)
# ikiTarihArasiProgramCek(tarihler, iller)
ikiTarihArasiDataCek(tarihler, iller)