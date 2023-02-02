import urllib.request

i=1
while i<31:
    a=i
    url = "https://www.laststicker.ru/i/cards/51/"+str(a)+".jpg"
    r = urllib.request.urlopen(url)
    with open(f"{str(a)}.jpg", "wb") as f:
        f.write(r.read())
        f.close()
    i+=1
