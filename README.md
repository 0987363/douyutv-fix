## 斗鱼直播 for XBMC
================

### Important: 
```
1. Install node or other javascript runtime to host system. 
2. Add EXECJS_RUNTIME environment to system.
```

#### Example in coreelec:
```
1. install Entware
    login to ssh, and run: installentware
2. install node
    login to ssh, and run: opkg update; opkg install node
3. add EXECJS_RUNTIME to kodi
    a. mkdir -p /storage/.kodi/addons/node.js/profile.d
    b. cd /storage/.kodi/addons/node.js
    c. echo "export EXECJS_RUNTIME=/opt/bin/node" >profile.d/node.js.profile
4. reboot
```

#### Execjs support javascript runtime:
```
register(runtime_names.PyV8,           pyv8runtime.PyV8Runtime())
register(runtime_names.Node,           external_runtime.node())
register(runtime_names.JavaScriptCore, external_runtime.jsc())
register(runtime_names.SpiderMonkey,   external_runtime.spidermonkey())
register(runtime_names.JScript,        external_runtime.jscript())
register(runtime_names.PhantomJS,      external_runtime.phantomjs())
register(runtime_names.SlimerJS,       external_runtime.slimerjs())
register(runtime_names.Nashorn,        external_runtime.nashorn())
```


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




### old version:

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
