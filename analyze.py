import requests
import sys

url = 'https://www.virustotal.com/vtapi/v2/url/report?apikey='
api_key = '53a75f13da30d296d3d18070c365e0b3412b80a8d903d1f66a0660be8ed2d79f'
website = sys.argv[1]

url = url + api_key + '&resource=' + website
info = requests.get(url)
data = info.json()

count = data['positives']
total = data['total']
print(count,'/',total,'Antivirus software detected virus')

if (count == 0):
    print('Safe')
else:
    print('Unsafe')