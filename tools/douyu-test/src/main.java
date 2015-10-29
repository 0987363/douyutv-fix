
import com.harreke.easyapp.requests.RequestBuilder;
import com.harreke.easyapp.requests.RequestMethod;
import tv.douyu.misc.util.EncryptionUtil;

public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		EncryptionUtil.a(new RequestBuilder(RequestMethod.GET, "room").setBaseUrl("http://www.douyutv.com/api/v1", "room/" + "319721"));

	}
}
