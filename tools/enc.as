package
{
    import flash.utils.ByteArray;

    public class Enc extends Object
    {

        private static const a:int = 0;

        private static const b:int = 1;

        public static var KEY:String = "dkrltl0%4*@jrky#@$";

        private static var aa:Enc;

        public function Enc() {
            super();
        }

        public static function get bb() : Enc {
            if(aa == null) {
                aa = new Enc();
            }
            return aa;
        }

        public function func1(param1:ByteArray) : ByteArray {
            return this.func3(param1,a);
        }

        public function func2(param1:ByteArray) : ByteArray {
            return this.func3(param1,b);
        }

        private function func3(param1:ByteArray, param2:int) : ByteArray {
            // swf, 1
            var _loc3_:ByteArray = null;
            var _loc5_:* = 0;
            var _loc6_:* = 0;
            var _loc7_:* = 0;
            var _loc4_:ByteArray = new ByteArray();
            while(_loc7_ < param1.length) {
                if(_loc5_ >= KEY.length) {  //18
                    _loc5_ = 0;
                    _loc6_++;
                    if(_loc6_ >= 50) {
                        _loc3_ = new ByteArray();
                        _loc4_.writeBytes(param1,50 * KEY.length,param1.length - 50 * KEY.length);
                        break;
                    }
                }
                if(param2 == a) {
                    _loc4_.writeByte(param1[_loc7_] + KEY.charCodeAt(_loc5_));
                } else if(param2 == b) {
                    _loc4_.writeByte(param1[_loc7_] - KEY.charCodeAt(_loc5_));
                }
                _loc7_++;
                _loc5_++;
            }
            _loc4_.position = 0;
            return _loc4_;
        }
    }
}
