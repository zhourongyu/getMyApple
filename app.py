# -*- coding: utf-8 -*-

import httplib, urllib, simplejson
import sys
from flask import Flask, request, redirect, url_for, render_template,Markup

app = Flask(__name__)
app.config.from_object(__name__)
@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/')
def getId():
    return render_template('query.html')

@app.route('/getinfo', methods=['GET', 'POST'])
def getinfo():
    if request.method == 'POST' and "meid" in request.form:
        meid = request.form["meid"]
        #params = urllib.urlencode({'sn': meid, 'key': '05D0437977124766B7AF884C0EF3BA6E'}) 
        params = urllib.urlencode({'sn': meid}) 
        headers = {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
        conn = httplib.HTTPConnection("sn.appvv.com") 
        ##conn.request("POST", "/tools/newSnData.php", params, headers) 
        conn.request("POST", "/tools/newSn.htm", params, headers) 
        response = conn.getresponse()
        print response.status, response.reason 
        if response == 200 :
            data = response.read().decode('utf-8')
            #print data
            res = simplejson.loads(data)
            print res
            dump_str = simplejson.dumps(res, ensure_ascii=False, encoding='utf-8')
            ddata = simplejson.loads(dump_str)

            conn.close()
            if ddata['ErrorCode'] == 0 :
                print dump_str
                return render_template('appInfo.html',info=ddata['ProductDetails'])
            else:
                error = "IMEI/MEID/序列号 不存在..."
                return render_template('query.html',error=error.decode("utf-8"))
        
if __name__ == "__main__":
    app.run(debug=True)