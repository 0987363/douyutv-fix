# -*- coding: utf-8 -*-
# 斗鱼接口
import urllib2
import json
import md5
import time


class APIHelper:
    def __init__(self):
        self.baseUrl = "http://capi.douyucdn.cn/api/v1/"

    def GetStringMD5(self, str):  
 #       print "gen:" + str
        m = md5.new()  
        m.update(str)  
        return m.hexdigest()  

    def request(self, action, param=None):
        t = str(int(time.time()))

        reqUrl = self.baseUrl + action
        if param != None:
            for k, v in enumerate(param):
                reqUrl = reqUrl + "&" + v + "=" + param[v]
        print "requrl:" + reqUrl

        try:
            response = urllib2.urlopen(reqUrl, timeout=10).read()
            jsonObject = json.loads(response)
            data = jsonObject["data"]
            return data
        except Exception, e:
            print "Error:" + str(e)
        return None

