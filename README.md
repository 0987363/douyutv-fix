## 斗鱼直播 for Kodi
================

#### Install:
```
1. deploy docker in any server, example nas or vps
    docker run -it -p 8080:80 heifeng/media-agent 
2. download latest zip from
    https://github.com/0987363/douyutv-fix/releases
3. unzip zip file
    modify APIHelper.py, update self.baseUrl="http://127.0.0.1:8080/v1/douyu" to your api service address
4. zip douyutv-fix.zip
5. install douyutv-fix.zip
```

+ **v4**
  + 将real-url解析库移到服务器端, 方便使用
  + 移除node,python依赖
  + 需配合 https://github.com/0987363/agent 使用，可使用docker部署 docker run -it -p 8080:80 heifeng/media-agent

+ **v3.3**
  + add kodi v19 support

+ **v3.0**
  + fixed new auth player, thanks https://github.com/wbt5/real-url

+ **v2.4**
  + fixed some bug

+ **v2.3**
  + fixed some bug

+ **v2.2**
  + fixed play, 2015.10.29

+ **v2.1**
  + add list room by online, and remove unused code

+ **v2.0**
  + fixed play, code based on HexPang@github.com/HexPang/DouyuLiveForXBMC, thanks




### fork from [HexPang](https://github.com/HexPang/DouyuLiveForXBMC)
