import sys
import json
import subprocess
from Swinger import Swinger

url = sys.argv[1]
url = url.split('/')
url[5] = url[5].replace('.html','')
arg = ' -b ' + url[4] + ' -a ' + url[5]
p = subprocess.check_output('python crawler.py'+arg,shell=True)

datas = url[4]+'-'+url[5]+'.json'
with open(datas,'r') as f:
    data = json.load(f)

s = Swinger()
s.load('LogisticRegression')

for i in data['messages']:
    text = i['push_content']
    print(text,s.swing(text))