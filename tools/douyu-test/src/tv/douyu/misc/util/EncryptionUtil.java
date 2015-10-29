package tv.douyu.misc.util;

//import android.text.TextUtils;
//import com.harreke.easyapp.frameworks.base.ApplicationFramework;
import com.harreke.easyapp.requests.RequestBuilder;
import com.harreke.easyapp.utils.StringUtil;

public class EncryptionUtil
{
    public static RequestBuilder a(RequestBuilder paramRequestBuilder)
    {
     //   CMessage.a().b(ApplicationFramework.getInstance());
        paramRequestBuilder.addQuery("aid", "android").addQuery("client_sys", "android").addQuery("time", "1446022056");
        StringBuilder localStringBuilder = new StringBuilder(paramRequestBuilder.getPath() + "?" + paramRequestBuilder.getQueryString());
        localStringBuilder.append("1231");
        String str = paramRequestBuilder.getBodyString();
        System.out.println("body:" + str);
    //    if (!TextUtils.isEmpty(str)) {
       //     localStringBuilder.append("&").append(str);
    //    }
 //       paramRequestBuilder.addQuery("auth", StringUtil.toMD5(localStringBuilder.toString()));
        System.out.println(localStringBuilder.toString());
        System.out.println("md5:"+ StringUtil.toMD5(localStringBuilder.toString()));
         return paramRequestBuilder;
    }
}


/* Location:              /Users/abc/work/douyu_apk/douyu_client_9_0v1_0_2/classes-dex2jar.jar!/tv/douyu/misc/util/EncryptionUtil.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */
