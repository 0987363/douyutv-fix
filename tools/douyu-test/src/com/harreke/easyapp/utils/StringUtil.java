package com.harreke.easyapp.utils;

//import android.text.SpannableStringBuilder;
import java.security.MessageDigest;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class StringUtil
{
  public static String escape(String paramString)
  {
    String str = paramString;
    if (paramString != null)
    {
      str = paramString;
      if (paramString.length() > 0) {
        str = paramString.replace("&amp;", "&").replace("&ldquo;", "“").replace("&rdquo;", "”").replace("&middot;", "•").replace("&mdash;", "-").replace("&quot;", "\"").replace("&gt;", ">").replace("&lt;", "<").replace("&nbsp;", " ").replace("&deg;", "°");
      }
    }
    return str;
  }
  
  public static Matcher getMatcher(String paramString, CharSequence paramCharSequence)
  {
    return Pattern.compile(paramString).matcher(paramCharSequence);
  }
  
  /*
  public static String getString(SpannableStringBuilder paramSpannableStringBuilder, int paramInt1, int paramInt2)
  {
    char[] arrayOfChar = new char[paramInt2 - paramInt1];
    paramSpannableStringBuilder.getChars(paramInt1, paramInt2, arrayOfChar, 0);
    return new String(arrayOfChar);
  }
  
  public static String getString(StringBuilder paramStringBuilder, int paramInt1, int paramInt2)
  {
    char[] arrayOfChar = new char[paramInt2 - paramInt1];
    paramStringBuilder.getChars(paramInt1, paramInt2, arrayOfChar, 0);
    return new String(arrayOfChar);
  }
  */
  
  public static String indentNumber(int paramInt)
  {
    if (paramInt < 10000) {
      return String.valueOf(paramInt);
    }
    String str = String.valueOf(paramInt / 10000.0F);
    return str.substring(0, str.indexOf(".") + 2) + "万";
  }
  
  public static boolean isEmpty(String paramString)
  {
    return (paramString == null) || (paramString.trim().length() == 0) || ("null".equals(paramString));
  }
  
  public static boolean isEmpty(String paramString1, String paramString2)
  {
    return (paramString1 == null) || (paramString2 == null) || (paramString1.trim().length() == 0) || (paramString2.trim().length() == 0);
  }
  
  public static boolean isValidMail(String paramString)
  {
    return getMatcher("\\w+@(\\w+.)+[a-z]{2,3}", paramString).matches();
  }
  
  public static int toInt(String paramString)
  {
    try
    {
      int i = Integer.valueOf(paramString).intValue();
      return i;
    }
    catch (NumberFormatException paramString) {}
    return -1;
  }
  
  public static String toMD5(String paramString)
  {
    int i = 0;
    if ((paramString != null) && (paramString.length() > 0)) {
      try
      {
        StringBuilder localStringBuilder = new StringBuilder();
        MessageDigest localMessageDigest = MessageDigest.getInstance("MD5");
        localMessageDigest.update(paramString.getBytes());
        byte[] bb = localMessageDigest.digest();
        System.out.println("md5:" + byteArrayToHex(bb));
        int j = bb.length;
        while (i < j)
        {
          localStringBuilder.append(String.format("%02x", new Object[] { Byte.valueOf(bb[i]) }));
          i += 1;
        }
        paramString = localStringBuilder.toString();
        return paramString;
      }
      catch (Exception paramString1)
      {
        return "catch";
      }
    }
    return "failed";
  }


public static String byteArrayToHex(byte[] byteArray) {  
    char[] hexDigits = {'0','1','2','3','4','5','6','7','8','9', 'A','B','C','D','E','F' };  
    char[] resultCharArray =new char[byteArray.length * 2];  
    int index = 0;  

    for (byte b : byteArray) {  
       resultCharArray[index++] = hexDigits[b>>> 4 & 0xf];  
       resultCharArray[index++] = hexDigits[b& 0xf];  
    }  
    return new String(resultCharArray);  
}
}



/* Location:              /Users/abc/work/douyu_apk/douyu_client_9_0v1_0_2/classes-dex2jar.jar!/com/harreke/easyapp/utils/StringUtil.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */