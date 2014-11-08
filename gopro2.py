import requests

url = 'http://10.5.5.9/gp/gpExec?p1=gpStreamA9&c1=restart'

r = requests.post(url)
print r.content