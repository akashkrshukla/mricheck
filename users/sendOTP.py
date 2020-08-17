import http.client

def initMsg(mobile, password):
    conn = http.client.HTTPConnection("api.msg91.com")
    mobile=str(mobile)
    welcome="Hi%20."+ mobile + "."
    conn.request("GET", "/api/sendhttp.php?country=91&sender=TRSOTP&route=4&mobiles=91"+mobile+"&authkey=205408ANCc7X5kKD5c38f99f&message="+ 'Thank you Registration successful')
    res = conn.getresponse()
    data = res.read()
    r_code=data.decode("utf-8")
    return r_code
