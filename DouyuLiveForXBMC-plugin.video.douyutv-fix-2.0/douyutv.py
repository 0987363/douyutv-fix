# -*- coding: utf-8 -*-
# douyutv.py
import sys

import urllib
import DouyuAPI
import xbmcplugin
import xbmcgui
import urlparse

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
    url = build_url({"action": "category", "cateId": "0"})
    listitem = xbmcgui.ListItem(" => 正在直播 <=")
    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder=True)
    data = api.loadCategory()
    for game in data:
        url = build_url({"action": "category", "cateId": game["cate_id"]})
        listitem = xbmcgui.ListItem(label=game["game_name"], iconImage=game["game_src"],
                                    thumbnailImage=game["game_src"], path=url)
        xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder=True)
    xbmcplugin.endOfDirectory(handle)
elif action[0] == "category":
    cateId = args.get('cateId', "0")
    limit = 10
    offset = args.get('offset', "0")
    o = int(offset[0], 0)
    try:
        if cateId[0] == "0":
            data = api.loadLive(o)
        else:
            data = api.loadRooms(cateId[0], o)

        data2 = sorted(data, key=lambda k: k['online'], reverse=True)

        for game in data2:
            #print "online:" + str(game["online"])
            url = build_url({"action": "play", "room_id": game["room_id"]})
            listitem = xbmcgui.ListItem(label = urllib.unquote(game["game_name"]) + " - " + urllib.unquote(game["room_name"]), iconImage=game["room_src"], thumbnailImage=game["room_src"], path=url)
            xbmcplugin.addDirectoryItem(handle, url, listitem)
        url = build_url({"action": "category", "cateId": cateId[0], "offset": int(o + limit)})
        listitem = xbmcgui.ListItem(label="下一页", path=url)
        xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder=True)
        xbmcplugin.endOfDirectory(handle)

    except Exception as e:
        xbmcgui.Dialog().ok("ERROR", str(e[0]))
elif action[0] == "play":
    roomId = args.get('room_id', "0")
    data = api.loadRoom(roomId[0])  # helper.request("room/" + roomId[0])
    rtmp_url = data["rtmp_url"]
    rtmp_live = data["rtmp_live"]
    #rtmp_live = data["rtmp_multi_bitrate"]["middle2"]
    videoUrl = rtmp_url + "/" + rtmp_live
    #print "item:", videoUrl

    item = xbmcgui.ListItem("Test")
    item.setProperty("SWFPlayer", "http://staticlive.douyutv.com/common/simplayer/WebRoom.swf?v=3134.4")
    item.setProperty("PlayPath", videoUrl)
    item.setInfo("video", {'title': urllib.unquote(data["room_name"]), 'writer': data["nickname"]})
    player = xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(videoUrl, item)



