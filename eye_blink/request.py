import http.client
hR = "/buzz"
conn = http.client.HTTPConnection("199.106.103.54", 5000)
conn.connect()
conn.request("POST", hR)
response = conn.getresponse()
data = response.read()
print (data)
conn.close()
