import requests


url = 'http://192.168.3.126:9999/WebUser/SyncHeart'
data = {'username':'mpp0130','pwd':'Mp123456','cpwd':'Mp123456'}
req = requests.post(url,data)