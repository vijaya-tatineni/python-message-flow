'''
Created on Nov 17, 2017

@author: vijaya.tatineni
'''

import urllib
import json
import os
from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/webhook', methods= ['POST'])

def webhook():
    req = request.get_json(silent = True, force= True)
    print("Request:")
    print(json.dumps(req, index=4))
    res = getWebhookResponse(req)
    res = json.dumps(res, index=4)
    print(res)
    r = make_response(res)
    r.headers['Content Type']= 'application/json'
    return r

def getWebhookResponse(req):
    if req.get("result").get("action") != 'installs':
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    name= parameters.get("client-name")
    client = {'ATT' : '490', 'Memories' : '20', 'Bell' : '40', 'Sprint' : '100'}   
    speech = "The app installs for " + name + "is " + str(client[name])
    print ("Response :")
    print(speech)
    return {
        'speech' : speech,
        'display text' : speech,
        'source' : "ClientAnalytics"
        }
    
if __name__ == '__main__':
    port = int(os.getenv('PORT',8000))
    print("starting app on port %d " %(port))
    #app.run(debug=True, port = port, host='0.0.0.0')
    app.run()
    
    
