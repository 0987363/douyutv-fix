# -*- coding: utf-8 -*-
__author__ = 'hexpang'
import APIHelper
import random
import os
import time
import md5


class DouyuAPI(APIHelper.APIHelper):
    def __init__(self):
        APIHelper.APIHelper.__init__(self)

    def GetStringMD5(self, str):  
        m = md5.new()  
        m.update(str)  
        return m.hexdigest()  

    def loadCategory(self):
        return self.request("game")

    def loadRooms(self, cateId, offset=0, limit=10):
        return self.request("live/" + cateId, {"offset": str(offset), "limit": str(limit)})

    def loadRoom(self,roomId):
        t = str(int(time.time()))
        md5_url = "room/" + roomId + "?aid=android&cdn=ws&client_sys=android&time=" + t + "1231"
        return self.request2("http://www.douyutv.com/api/v1/room/" + roomId + "?aid=android&auth=" + self.GetStringMD5(md5_url) + "&cdn=ws&client_sys=android&time=" + t)
    #return self.request("room/" + roomId)

    def loadLive(self,offset=0,limit=10):
        return self.request("live", {"offset": str(offset), "limit": str(limit)})

