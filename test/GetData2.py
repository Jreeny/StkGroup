
import requests
import json

url = 'http://87.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406526563715394427_1631116233755&pn=1&pz=10000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23&fields=f12,f14'

response = requests.get(url).text
data_json = response.split('(', 1)[1].rsplit(')', 1)[0]

data = json.loads(data_json)
diff = data['data']['diff']

for stock in diff:
    print(stock['f12'], stock['f14'])
