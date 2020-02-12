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

    def loadSubCategory(self, shortName):
        print "start load sub category"
        return self.request("getColumnDetail", {"shortName": shortName})

    def loadSecendLive(self, tagId, offset=0, limit=12):
        print "start load second channel live"
        return self.request("live/" + tagId, {"offset": str(offset), "limit": str(limit)})

    def loadFirstLive(self, cateId, offset=0, limit=12):
        print "start load first channel live"
        return self.request("getColumnRoom/" + cateId, {"offset": str(offset), "limit": str(limit)})

    def loadLive(self,offset=0,limit=12):
        print "start load all live"
        return self.request("live", {"offset": str(offset), "limit": str(limit)})


