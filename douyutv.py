# -*- coding: utf-8 -*-
# douyutv.py
import sys

import urllib
import DouyuAPI
import xbmcplugin
import xbmcgui
import urlparse
import realurl

base_url = sys.argv[0]
handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
api = DouyuAPI.DouyuAPI()

action = args.get('action', None)

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)


def onControl(self, control):
    if control == self.list:
        item = self.list.getSelectedItem()
        item.setLabel('Casino Royale')

if action is None:
    url = build_url({"action": "live", "cate_id": "0"})
    print "url:" + url
    listitem = xbmcgui.ListItem(" => 正在直播 <=")
    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder=True)

    data = api.loadCategory()
    for game in data:
        url = build_url({"action": "category", "short_name": game["short_name"], "cate_id":game["cate_id"]})
        print "url:" + url
        listitem = xbmcgui.ListItem(label=game["cate_name"],path=url)
        xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder=True)
    xbmcplugin.endOfDirectory(handle)
    exit(0)

if action[0] == "live":
    cateId = args.get('cate_id', "0")
    tagId = args.get('tag_id', "0")
    offset = args.get('offset', "0")
    o = int(offset[0], 0)
    limit = 12

    print "cattleid:",cateId[0]
    print "tagid:", tagId[0]

    if cateId[0] != "0":
        data = api.loadFirstLive(cateId[0], o)
    elif tagId[0] != "0":
        data = api.loadSecendLive(tagId[0], o)
    else:
        data = api.loadLive(o)

    data2 = sorted(data, key=lambda k: k['online'], reverse=True)

    for game in data2:
        url = build_url({"action": "play", "room_id": game["room_id"], "room_name": game["room_name"].encode('utf-8'), "nickname": game["nickname"].encode('utf-8')})
        listitem = xbmcgui.ListItem(label = urllib.unquote(game["game_name"]) + " - " + urllib.unquote(game["nickname"]) + " - " + urllib.unquote(game["room_name"]), iconImage=game["room_src"], thumbnailImage=game["room_src"], path=url)
        xbmcplugin.addDirectoryItem(handle, url, listitem)

    url = build_url({"action": "live", "offset": int(o + limit)})
    listitem = xbmcgui.ListItem(label="下一页", path=url)
    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder=True)
    xbmcplugin.endOfDirectory(handle)
    exit(0)

if action[0] == "category":
    cateId = args.get('cate_id', "0")
    shortName = args.get('short_name', "0")

    url = build_url({"action": "live", "cate_id": cateId[0]})
    print "cat rooms url:" + url
    listitem = xbmcgui.ListItem(" => 正在直播 <=")
    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder=True)

    data = api.loadSubCategory(shortName[0])
    for game in data:
        url = build_url({"action": "live", "tag_id": game["tag_id"]})
        print "sub rooms url:" + url
        listitem = xbmcgui.ListItem(label=game["tag_name"],path=url)
        xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder=True)
    xbmcplugin.endOfDirectory(handle)

    exit(0)

if action[0] == "play":
    roomId = args.get('room_id', "0")[0]
    roomName = args.get('room_name', "unknown")[0]
    nickname = args.get('nickname', "unknown")[0]

    videoUrl = realurl.get_real_url(roomId)

    item = xbmcgui.ListItem("Test")
    item.setProperty("PlayPath", videoUrl)
    item.setInfo("video", {'title': nickname + " - " + roomName, 'writer': nickname})
    player = xbmc.Player().play(videoUrl + "11223344", item)

