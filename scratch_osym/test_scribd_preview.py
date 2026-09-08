import urllib.request, re, urllib.parse, http.cookiejar, sys

sys.stdout.reconfigure(encoding='utf-8')

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
resp = opener.open('http://142.93.104.78:8088/')
html = resp.read().decode('utf-8')

csrf_name_m = re.search(r'name="(csrf_cookie_name|[^"]+)"\s+value="([a-f0-9]{32})"', html)
token_name = csrf_name_m.group(1)
token_val = csrf_name_m.group(2)

post_data = {
    'username': 'halil@quiza.com',
    'password': 'admin123',
    token_name: token_val
}
req = urllib.request.Request('http://142.93.104.78:8088/loginMe', data=urllib.parse.urlencode(post_data).encode('utf-8'))
res = opener.open(req)
print(f"Login HTTP Status: {res.status}")

preview_data = {
    'url': 'https://www.scribd.com/document/822952525/HAKİMLİK-AKADEMİSİ-HMGS-I-DARE-HUKUKU-SORU-BANKASI',
    'category_id': '11',
    'badge': 'HMGS İdare'
}
req2 = urllib.request.Request('http://142.93.104.78:8088/book-import/preview', data=urllib.parse.urlencode(preview_data).encode('utf-8'))
res2 = opener.open(req2)
print("Scribd Preview HTTP Status:", res2.status)
body = res2.read().decode('utf-8')
print("Scribd Preview Response Body:", body[:1000])
