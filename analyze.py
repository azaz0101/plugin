import requests
import sys

url = 'https://www.virustotal.com/vtapi/v2/url/report?apikey='
api_key = ''
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
