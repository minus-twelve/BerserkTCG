from urllib.request import Request, urlopen

i=1
while i<31:
    a=i
    url = "https://www.laststicker.ru/i/cards/51/"+str(a)+".jpg"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    r = urlopen(req)
    with open(f"{str(a)}.jpg", "wb") as f:
        f.write(r.read())
        f.close()
    i+=1
