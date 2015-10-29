# -*- coding: utf-8 -*-
# 斗鱼接口
import urllib2
import json


class APIHelper:
    def __init__(self):
        self.baseUrl = "http://api.douyutv.com/api/client"
        self.client_sys = "android"

    def request(self, action, param=None):
        reqUrl = self.baseUrl + "/" + action
        reqUrl = reqUrl + "?" + "client_sys=" + self.client_sys
        #print "requrl:" + reqUrl
        if param != None:
            for k, v in enumerate(param):
                reqUrl = reqUrl + "&" + v + "=" + param[v]
        try:
            response = urllib2.urlopen(reqUrl, timeout=10).read()
            jsonObject = json.loads(response)
            data = jsonObject["data"]
            return data
        except Exception, e:
            print "Error:" + str(e)
        return None

    def request2(self, reqUrl, param=None):
        print "requrl:" + reqUrl
        if param != None:
            for k, v in enumerate(param):
                reqUrl = reqUrl + "&" + v + "=" + param[v]
        try:
            response = urllib2.urlopen(reqUrl, timeout=10).read()
            jsonObject = json.loads(response)
            data = jsonObject["data"]
            return data
        except Exception, e:
            print "Error:" + str(e)
        return None
