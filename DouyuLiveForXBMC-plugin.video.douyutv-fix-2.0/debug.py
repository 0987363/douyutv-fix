import DouyuAPI

__author__ = 'hexpang'
helper = DouyuAPI.DouyuAPI()
result = helper.loadCategory() #helper.request("login",{"username":"test","password":"test","type":"md5"})
print result
print "Done"