import DouyuAPI
import realurl


real_url = realurl.get_real_url(99999)
print('address:\n' + real_url)
exit(0)

helper = DouyuAPI.DouyuAPI()
result = helper.loadLive()
print result
print "Done"
