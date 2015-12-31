# -*- coding: utf-8 -*-
__author__ = 'hexpang'
import APIHelper
import random
import os


class DouyuAPI(APIHelper.APIHelper):
    def __init__(self):
        APIHelper.APIHelper.__init__(self)

    def loadCategory(self):
        print "start load category"
        return self.request("game")

    def loadRooms(self, cateId, offset=0, limit=12):
        print "start load rooms"
        return self.request("live/" + cateId, {"offset": str(offset), "limit": str(limit)})

    def loadRoom(self,roomId):
        print "start load rom"
        return self.request("room/" + roomId)

    def loadLive(self,offset=0,limit=12):
        print "start load live"
        return self.request("live", {"offset": str(offset), "limit": str(limit)})

