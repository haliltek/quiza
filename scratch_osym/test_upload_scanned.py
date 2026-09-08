import urllib.request, re, urllib.parse, http.cookiejar, sys, requests

sys.stdout.reconfigure(encoding='utf-8')

s = requests.Session()
r = s.get('http://142.93.104.78:8088/')
csrf_name_m = re.search(r'name="(csrf_cookie_name|[^"]+)"\s+value="([a-f0-9]{32})"', r.text)
token_name = csrf_name_m.group(1)
token_val = csrf_name_m.group(2)

post_data = {
    'username': 'halil@quiza.com',
    'password': 'admin123',
    token_name: token_val
}
res = s.post('http://142.93.104.78:8088/loginMe', data=post_data)
print("Login status:", res.status_code)

with open('C:/Users/Halil/Downloads/17099548-Yargi-Kpss-Deneme-Sinavi.pdf', 'rb') as f:
    files = {'pdf_file': ('17099548-Yargi-Kpss-Deneme-Sinavi.pdf', f, 'application/pdf')}
    data = {'category_id': '32', 'badge': 'Yargi KPSS Deneme 15'}
    res = s.post('http://142.93.104.78:8088/book-import/preview', files=files, data=data)
    print("Scanned PDF Preview status:", res.status_code)
    print("Response body:", res.text[:400])
