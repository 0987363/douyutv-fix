# -*- coding: utf-8 -*-
import requests

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

class APIHelper:
    def __init__(self):
        self.baseUrl = "http://capi.douyucdn.cn/api/v1/"

    def request(self, action, param=None):
        reqUrl = self.baseUrl + action
        if param != None:
            reqUrl = reqUrl + "?" + urlencode(param)

        header = {
            "User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
        }
        response = requests.get(url=reqUrl, headers=header)
        jsonObject = response.json()

#        jsonObject = json.loads(response)
        data = jsonObject["data"]
        return data

