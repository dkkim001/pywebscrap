import sys
import io
import urllib.request as req
from urllib.parse import urlencode

#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

API = "https://api.ipify.org"

valuse = {'format': 'json'}

print('before', valuse)
params = urlencode(valuse)
print('after', params)

url = API + "?" + params
print("요청 url", url)
