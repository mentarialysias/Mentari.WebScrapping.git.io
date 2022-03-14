# import packages requests dan beautiful



from datetime import datetime
from typing import TextIO

import requests
from bs4 import BeautifulSoup


#request ke website
page = requests.get("https://republika.co.id/")

#Extract konten menjadi objek BeautifulSoup
obj = BeautifulSoup(page.text,'html.parser');

#print ('Menampilkan Objek HTML')
#print ('=================================================================')
#print(obj)

#print('\nMenampilkan title browser dengan tag ')
#print ('=================================================================')
#print(obj.title)

print ('\nMenampilkan title browser')
print ('=================================================================')
print(obj.title.text)

#print ('\nMenampilkan headline berdasarkan div class')
#print ('=================================================================')
#print (obj.find_all('div', class_='bungkus_txt_headline_center'))

print ('\nMenampilkan semua teks headline')
print ('=================================================================')
for headline in obj.find_all('div', class_='bungkus_txt_headline_center'):
    print(headline.find('h2').text)

print('\nMenampilkan Kategori')
print ('=================================================================')
for kategori in obj.find_all('div',class_='teaser_conten1_center'):
   print(kategori.find('h1').text)

print ('\nMenampilkan Waktu Publish')
print('=================================================================')
for waktu in obj.find_all('div', class_='date'):
    print(waktu.text)

tanggal_scrap = datetime.now()
str(tanggal_scrap)
print(tanggal_scrap)

print('\nMenyimpan headline pada file text')
print('=================================================================')
f =  open('D:\\headline.txt','w')
for headline in obj.find_all('div', class_='bungkus_txt_headline_center'):
    f.write(headline.find('h2').text)
    f.write('\n')
#f.write('\n')
for kategori in obj.find_all('div', class_='teaser_conten1_center'):
    f.write(kategori.find('h1').text)
    f.write('\n')
#f.write('\n')
for waktu in obj.find_all('div', class_='date'):
    f.write(waktu.text)
    f.write('\n')
#f.write('\n')
f.write(str(tanggal_scrap))
f.close()

import json
data = []
f = open('D:\\headline.json','w')
for headline in obj.find_all('div', class_='bungkus_txt_headline_center'):
    data.append({"Judul ": headline.find('h2').text, "Kategori ":kategori.find('h1').text, "Publish_Time ": waktu.text, "Waktu_Scrapping": str(tanggal_scrap)})
    f.write('\n')

jdumps = json.dumps(data)
f.writelines(jdumps)
f.close()


