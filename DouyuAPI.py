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
        return self.request("getColumnList")

    def loadSubLive(self, cateId, offset=0, limit=12):
        print "start load sub channel live"
        return self.request("live/" + cateId, {"offset": str(offset), "limit": str(limit)})

    def loadSubCategory(self, subId):
        print "start load sub category"
        return self.request("getColumnDetail" + {"shortName": subId})

    def loadLive(self,offset=0,limit=12):
        print "start load all live"
        return self.request("live", {"offset": str(offset), "limit": str(limit)})

