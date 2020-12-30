## 斗鱼直播 for Kodi
================

#### Install:
```
1. deploy docker in any server, example nas or vps
    docker run -it -p 8080:80 heifeng/media-agent 
2. download douyutv-fix from
    https://github.com/0987363/douyutv-fix/releases
3. unzip douyutv-fix.zip
    modify APIHelper.py, update self.baseUrl="http://127.0.0.1:8080/v1/douyu" to your api service address
4. zip douyutv-fix.zip
5. install douyutv-fix.zip
```

+ **v4**
  + 将real-url解析库移到服务器端, 方便使用
  + 移除node,python依赖
  + 需配合 https://github.com/0987363/agent 使用，也可使用docker部署 docker run -it -p 8080:80 heifeng/media-agent

v3.3
add kodi v19 support

v3.0
fixed new auth player, thanks https://github.com/wbt5/real-url

v2.4
fixed some bug

v2.3
fixed some bug

v2.2
fixed play, 2015.10.29

v2.1
add list room by online, and remove unused code

v2.0
fixed play, code based on HexPang@github.com/HexPang/DouyuLiveForXBMC, thanks




### old version, thanks HexPang:

说明
----------------
> 针对XBMC开发的插件,界面待优化.欢迎探讨.

> 之前没接触过Python,代码较渣,请谅解.

下载
----------------
1. v1.0.1-2014-08-31 [下载](https://github.com/HexPang/DouyuLiveForXBMC/archive/v1.0.1.zip)

更新内容
----------------
1. 暂无
