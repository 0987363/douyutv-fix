# -*- coding: utf-8 -*-
import APIHelper
import random
import os


class DouyuAPI(APIHelper.APIHelper):
    def __init__(self):
        APIHelper.APIHelper.__init__(self)

    def loadCategory(self):
        return self.request("/category/")

    def loadSubCategory(self, shortName):
        return self.request("/category/short/" + shortName + "/sub")

    def loadCateRoom(self, cateId, offset=0, limit=12):
        return self.request("/room/category/" + cateId, {"offset": str(offset), "limit": str(limit)})

    def loadTagRoom(self, tagID, offset=0, limit=12):
        return self.request("/room/tag/" + tagID, {"offset": str(offset), "limit": str(limit)})

    def loadRoom(self,offset=0,limit=12):
        return self.request("/room/", {"offset": str(offset), "limit": str(limit)})

    def loadSource(self, roomID, offset=0,limit=12):
        return self.request("/room/id/" + roomID, {"offset": str(offset), "limit": str(limit)})


