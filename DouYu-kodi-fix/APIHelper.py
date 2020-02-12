# -*- coding: utf-8 -*-
# 斗鱼接口
import urllib2
import urllib
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
        reqUrl = self.baseUrl + action
        if param != None:
            reqUrl = reqUrl + "?" + urllib.urlencode(param)
        print "requrl:" + reqUrl

        try:
            header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
            request = urllib2.Request(reqUrl, headers = header)
            response = urllib2.urlopen(request, timeout=10).read()
            jsonObject = json.loads(response)
            data = jsonObject["data"]
            return data
        except Exception, e:
            print "Error:" + str(e)
        return None

