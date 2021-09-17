from soup import soup


url = "https://lightgauge.net/language/python/add-module-path/"
soup = soup()
print(soup.bs(url).title)
