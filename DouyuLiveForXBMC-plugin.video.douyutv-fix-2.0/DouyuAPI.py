# -*- coding: utf-8 -*-
__author__ = 'hexpang'
import APIHelper
import random
import os
import time


class DouyuAPI(APIHelper.APIHelper):
    def __init__(self):
        APIHelper.APIHelper.__init__(self)

    def loadCategory(self):
        return self.request("game")

    def loadRooms(self, cateId, offset=0, limit=10):
        return self.request("live/" + cateId, {"offset": str(offset), "limit": str(limit)})

    def loadRoom(self,roomId):
        return self.request2("http://www.douyutv.com/api/v1/room/" + roomId + "?aid=android&auth=" + "".join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(32))) + "&cdn=ws&client_sys=android&time=" + str(int(time.time())))
    #return self.request("room/" + roomId)

    def loadLive(self,offset=0,limit=10):
        return self.request("live", {"offset": str(offset), "limit": str(limit)})
