import requests 

res = requests.get('https://ipinfo.io/')
data = res.json()
city = data['city']
location = data['loc'].split(',')
lat = location[0]
lon = location[1]
print("Lat is : ", lat)
print("Lon is : ", lon)
print("City is :", city)
