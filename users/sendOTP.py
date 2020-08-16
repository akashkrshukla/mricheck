import http.client

def initMsg(mobile, password):
    conn = http.client.HTTPConnection("api.msg91.com")
    mobile=str(mobile)
    welcome="Welcome%20to%20Skyline%20Golf."
    conn.request("GET", "/api/sendhttp.php?country=91&sender=TRSOTP&route=4&mobiles=91"+mobile+"&authkey=205408ANCc7X5kKD5c38f99f&message="+welcome+"Your%20password%20is%20"+password)
    res = conn.getresponse()
    data = res.read()
    r_code=data.decode("utf-8")
    return r_code
