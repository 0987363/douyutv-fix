# -*- coding: utf-8 -*-
import XWindow
#import urlparse
#import sys
#import DouyuAPI

__author__ = 'hexpang'
#base_url = sys.argv[0]
#handle = int(sys.argv[1])
#args = urlparse.parse_qs(sys.argv[2][1:])
#api = DouyuAPI.DouyuAPI()
#action = args.get('action', None)
douyuUI = XWindow.XWindow()
douyuUI.doModal()
del douyuUI
print "Douyu.py close.."