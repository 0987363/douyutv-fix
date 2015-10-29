package com.harreke.easyapp.requests;

//import android.support.annotation.NonNull;
//import android.text.TextUtils;
//import com.harreke.easyapp.utils.LogUtil;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

public class RequestBuilder
{
  private final String TAG = "RequestBuilder";
  private Map<String, String> mBodyMap = new TreeMap();
  private Map<String, String> mHeaderMap = new TreeMap();
  private String mHost;
  private RequestMethod mMethod;
  private Map<String, String> mMultiPartMap = new TreeMap();
  private String mPath;
  private Map<String, String> mQueryMap = new TreeMap();
  private String mTag;
  
  public RequestBuilder( RequestMethod paramRequestMethod, String paramString)
  {
    this.mMethod = paramRequestMethod;
    this.mTag = paramString;
  }
  
  public RequestBuilder( String paramString)
  {
    this.mMethod = RequestMethod.GET;
    this.mTag = ("load_" + paramString.hashCode());
    this.mHost = paramString;
    this.mPath = "";
  }
  
  private String buildString( Map<String, String> paramMap)
  {
    Iterator localIterator = paramMap.keySet().iterator();
    StringBuilder localStringBuilder = new StringBuilder();
    if (localIterator.hasNext())
    {
      String str = (String)localIterator.next();
      localStringBuilder.append(str).append("=").append((String)paramMap.get(str));
      while (localIterator.hasNext())
      {
        str = (String)localIterator.next();
        localStringBuilder.append("&").append(str).append("=").append((String)paramMap.get(str));
      }
    }
    return localStringBuilder.toString();
  }
  
  public final RequestBuilder addBody( String paramString,  Object paramObject)
  {
    paramObject = String.valueOf(paramObject);
    try
    {
      this.mBodyMap.put(paramString, URLEncoder.encode((String)paramObject, "utf-8"));
      return this;
    }
    catch (UnsupportedEncodingException localUnsupportedEncodingException)
    {
      this.mBodyMap.put(paramString, paramObject);
    }
    return this;
  }
  
  public final RequestBuilder addHeader( String paramString,  Object paramObject)
  {
    paramObject = String.valueOf(paramObject);
    try
    {
      this.mHeaderMap.put(paramString, URLEncoder.encode((String)paramObject, "utf-8"));
      return this;
    }
    catch (UnsupportedEncodingException localUnsupportedEncodingException)
    {
      this.mHeaderMap.put(paramString, paramObject);
    }
    return this;
  }
  
  public final RequestBuilder addMultiPart( String paramString,  Object paramObject)
  {
    paramObject = String.valueOf(paramObject);
    try
    {
      this.mMultiPartMap.put(paramString, URLEncoder.encode((String)paramObject, "utf-8"));
      return this;
    }
    catch (UnsupportedEncodingException localUnsupportedEncodingException)
    {
      this.mMultiPartMap.put(paramString, paramObject);
    }
    return this;
  }
  
  public final RequestBuilder addQuery( String paramString,  Object paramObject)
  {
    paramObject = String.valueOf(paramObject);
    try
    {
      this.mQueryMap.put(paramString, URLEncoder.encode((String)paramObject, "utf-8"));
      return this;
    }
    catch (UnsupportedEncodingException localUnsupportedEncodingException)
    {
  //    this.mQueryMap.put(paramString, paramObject);
    }
    return this;
  }
  
  public void clear()
  {
    clearHeader();
    clearQuery();
    clearBody();
  }
  
  public void clearBody()
  {
    this.mBodyMap.clear();
  }
  
  public void clearHeader()
  {
    this.mHeaderMap.clear();
  }
  
  public void clearQuery()
  {
    this.mQueryMap.clear();
  }
  
  public String getBaseUrl()
  {
    StringBuilder localStringBuilder = new StringBuilder().append(this.mHost);
   // if (TextUtils.isEmpty(this.mPath)) {}
    for (String str = "";; str = "/" + this.mPath) {
      return str;
    }
  }
  
  public final Map<String, String> getBody()
  {
    return this.mBodyMap;
  }
  
  public final String getBodyString()
  {
    return buildString(this.mBodyMap);
  }
  
  public final Map<String, String> getHeader()
  {
    return this.mHeaderMap;
  }
  
  public final String getHeaderString()
  {
    return buildString(this.mHeaderMap);
  }
  
  public String getHost()
  {
    return this.mHost;
  }
  
  public final RequestMethod getMethod()
  {
    return this.mMethod;
  }
  
  public final Map<String, String> getMultiPart()
  {
    return this.mMultiPartMap;
  }
  
  public final String getMultiPartString()
  {
    return buildString(this.mMultiPartMap);
  }
  
  public String getPath()
  {
    return this.mPath;
  }
  
  public final Map<String, String> getQuery()
  {
    return this.mQueryMap;
  }
  
  public final String getQueryString()
  {
    return buildString(this.mQueryMap);
  }
  
  public String getTag()
  {
    return this.mTag;
  }
  
  public final String getUrl()
  {
    String str = getQueryString();
    StringBuilder localStringBuilder = new StringBuilder().append(getBaseUrl());
  //  if (TextUtils.isEmpty(str)) {}
    for (str = "";; str = "?" + str) {
      return str;
    }
  }
  
  public final void print()
  {
    String str = "";
  //  switch (RequestBuilder.1.$SwitchMap$com$harreke$easyapp$requests$RequestMethod[this.mMethod.ordinal()])
 //   {
 //   }
    for (;;)
    {
   //   LogUtil.e("RequestBuilder/" + this.mTag, str);
      return;
      str = "GET " + getUrl();
      continue;
      str = "POST " + getUrl() + "\nHeaders:\n" + getHeaderString() + "\nBodies:\n" + getBodyString() + "\nMultiParts:\n" + getMultiPartString();
    }
  }
  
  public final RequestBuilder setBaseUrl(String paramString1, String paramString2)
  {
    this.mHost = paramString1;
    this.mPath = paramString2;
    return this;
  }
}


/* Location:              /Users/abc/work/douyu_apk/douyu_client_9_0v1_0_2/classes-dex2jar.jar!/com/harreke/easyapp/requests/RequestBuilder.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */