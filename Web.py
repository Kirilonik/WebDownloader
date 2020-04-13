#! python3
# WebXKCD - Скрипт который загружает все комиксы XKCD.

import os
import requests
import bs4

url = "https://xkcd.ru/"
os.chdir("D://")
os.makedirs("xkcd", exist_ok=True)

while not url.endswith("#"):
    print("Загружается страница %s..." % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "lxml")
    comicElem = soup.select(".main img")  #
    if not comicElem:
        print("Не удалось загрузить изображение")
    else:
        comicUrl = comicElem[0].get("src")
        #
        print("Загружается изображение %s..." % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()
        #
        imageFile = open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb")
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    #
    prevLink = soup.select('a[class="nav"]')[1]
    url = "https://xkcd.ru" + prevLink.get('href')
print("Done...")
