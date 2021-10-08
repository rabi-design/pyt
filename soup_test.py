 # from soup import Soup
import amazon


# url = "https://lightgauge.net/language/python/add-module-path/"
# sou = Soup()
# print(sou.main())
dri, m = amazon.amazon("B016Y20WRS")
print(m.find("span", class_ = "a-size-large product-title-word-break").text.replace("\n", ""))
dri.close()
dri.quit()
