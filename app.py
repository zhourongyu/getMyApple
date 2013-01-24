# -*- coding: utf-8 -*-

import web,codecs
import httplib, urllib, simplejson
from web.contrib.template import render_jinja

urls = ("/.*", "hello")
app = web.application(urls, globals())


render = render_jinja(
        'templates',   # 设置模板路径.
        encoding = 'utf-8', # 编码.
    )

class hello:
    def GET(self):
    	params = urllib.urlencode({'sn': 'c39grpwedp0n', 'key': '05D0437977124766B7AF884C0EF3BA6E'}) 
    	headers = {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
    	conn = httplib.HTTPConnection("sn.appvv.com") 
    	conn.request("POST", "/tools/newSnData.php", params, headers) 
    	response = conn.getresponse()
    	print response.status, response.reason 
    	data = response.read().decode('utf-8')
    	res = simplejson.loads(data)
        

        dump_str = simplejson.dumps(res, ensure_ascii=False, encoding='utf-8')
        print type(dump_str)
       
        out_f = open('out.dat', 'w', 0)
        out_f.write(dump_str.encode('utf-8'))

        ##in_str = open('out.dat', 'r').read().decode('utf-8')
        ##print type(in_str)
        ddata = simplejson.loads(dump_str)
        ##print ddata
    	conn.close()
    	return render.hello(name=ddata['ProductDetails'])

if __name__ == "__main__":
    app.run()