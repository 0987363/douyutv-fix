# -*- coding: utf-8 -*-
# 窗体
import xbmc
import xbmcplugin
import xbmcgui
import urllib
import DouyuAPI

__author__ = 'hexpang'

ACTION_PREVIOUS_MENU = 10
ACTION_SELECT_ITEM = 7
XBFONT_CENTER_X = 0x00000002


class XWindow(xbmcgui.Window):
    def __init__(self):
        self.Page = 1
        #self.category = None
        self.cateList = {}
        self.PAGE_DOWN = None
        self.PAGE_UP = None
        self.logo = xbmcgui.ControlImage(50, 20, 170, 54, "http://staticlive.douyutv.com/common/douyu/images/logo.png")
        self.addControl(self.logo)
        self.api = DouyuAPI.DouyuAPI()
        self.addControl(
            xbmcgui.ControlImage(0, 0, 1920, 1080,
                                 "http://www.sucai.com.cn/bizhi/flashAll/20120221/1329788727cqeHgz.jpg"))
        self.category = self.api.loadCategory()
        self.cateBtnList = []
        self.cateWidth = 140
        self.cateHeight = 195
        self.width = self.getWidth()
        self.height = self.getHeight()
        self.PAGE_UP = xbmcgui.ControlButton(0, self.height - 120, self.width, int(30), "上一页", alignment=2,
                                                 textColor="0xFF0000FF")
        self.addControl(self.PAGE_UP)
        self.PAGE_DOWN = xbmcgui.ControlButton(0, self.height - 90, self.width, int(30), "下一页",
                                                   alignment=2,
                                                   textColor="0xFF0000FF")
        self.addControl(self.PAGE_DOWN)
        self.loadCategory(self.Page)
        self.cateWidth = int(self.width * 0.8)
        self.cateHeight = int(self.height * 0.8)
        print "XWindow Init..."

    def loadCategory(self, Page=1):
        screenx = self.width
        screeny = self.height
        listSize_width = int(screenx * 0.8)
        listSize_height = int(screeny * 0.8)
        center_x = screenx / 2 - listSize_width / 2
        center_y = ((screeny - 170 - 150) / 2) - listSize_height / 2
        column = int(listSize_width / self.cateWidth)
        row = 2  # listSize_height / cateHeight
        PageShow = column * row
        x = center_x
        y = center_y + self.cateHeight
        index_x = 0
        index_y = 1
        # self.list = xbmcgui.ControlList(center_x, center_y, listSize_width, listSize_height)
        # self.list.setItemHeight(cateHeight)
        # self.addControl(self.list)
        while len(self.cateBtnList) > 0:
            btn = self.cateBtnList[0]
            del self.cateBtnList[0]
            self.removeControl(btn)
        cateIndex = Page * PageShow - PageShow


        print "Load Page " + str(Page) + " Index From " + str(cateIndex) + " To " + str(int(cateIndex + PageShow))
        for index in range(cateIndex, cateIndex + PageShow + 2):
            if index > len(self.category):
                break
            catelog = self.category[index]

            btn = xbmcgui.ControlButton(int(x), int(y), self.cateWidth, self.cateHeight,
                                        catelog["game_name"], catelog["game_src"],
                                        catelog["game_src"], int(0), self.cateHeight, int(2), font="font14",
                                        textColor="0xFFFFFFFF", disabledColor="0xFFFF3300",
                                        shadowColor='0xFF000000', focusedColor='0xFFFF0000')
            self.addControl(btn)
            self.cateBtnList.append(btn)
            self.cateList.setdefault(btn.getId(), catelog)
            x += self.cateWidth + 5
            index_x += 1
            if index_x > column:
                index_x = 0
                x = center_x
                y += self.cateHeight + 30
                index_y += 1
            if index_y > row:
                continue

    def onControl(self, control):
        if control == self.PAGE_DOWN:
            self.Page += 1
            self.loadCategory(self.Page)
        elif control == self.PAGE_UP:
            if self.Page > 1:
                self.Page -= 1
                self.loadCategory(self.Page)
        elif control.getId() in self.cateList:
            data = self.cateList.get(control.getId())
            self.message(data["game_name"])
        else:
            self.message('you pushed the button ')


    def onClick(self, controlId):
        self.message('you pushed the button ' + str(controlId))


    def message(self, message):
        dialog = xbmcgui.Dialog()
        dialog.ok(" My message title", message)