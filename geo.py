import requests
print("場所を入力してください")
full_address = input()

url = 'http://www.geocoding.jp/api/'
payload = {'q': full_address}
result = requests.get(url, params=payload)
result.text
import xmltodict #ない場合はpip install xmltodictすると入手できます
resultdict = xmltodict.parse(result.text)
resultdict
print("緯度")
print(resultdict["result"]["coordinate"]["lat"])
print("経度")
print(resultdict["result"]["coordinate"]["lng"])
