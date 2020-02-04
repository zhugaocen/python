import urllib.request
import urllib.parse

url ='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

data = {}
data['i'] = 'I love Fishc.com!'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15806969343623'
data['sign'] = '352c4126a9ed37552626f45be3dc82fb'
data['ts'] = '1580696934362'
data['bv'] = '9915c65c9e78cfd742d6a24e66b85108'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'

data = urllib.parse.urlencode(data).encode('uft-8')
response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
print(html)
