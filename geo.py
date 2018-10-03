import requests

full_address = input()
 #東京都庁の住所である
url = 'http://www.geocoding.jp/api/'
payload = {'q': full_address}
result = requests.get(url, params=payload)
result.text
import xmltodict #ない場合はpip install xmltodictすると入手できます
resultdict = xmltodict.parse(result.text)
resultdict
print(resultdict["result"]["coordinate"]["lat"])
print(resultdict["result"]["coordinate"]["lng"])
