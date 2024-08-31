import requests
import http

# simple
response = requests.get('http://localhost:3000', allow_redirects=False)
response.raise_for_status()
txt = response.text

# less simple
conn = http.client.HTTPConnection('http://localhost:3000')

conn.request('GET', "/")

response = conn.getresponse()

# what if response is not status 200?
if response.status != 200:
    raise Exception("response status not 200")

# TODO code to handle redirect


text = response.read()