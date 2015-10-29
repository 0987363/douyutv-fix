package
{
   import flash.display.Sprite;
   import flash.net.URLStream;
   import flash.display.Loader;
   import flash.events.Event;
   import flash.net.URLRequest;
   import flash.events.ProgressEvent;
   import flash.utils.ByteArray;
   
   public class WebRoomDecrypt extends Sprite
   {
       
      private var url:URLStream;
      
      private var load:Loader;
      
      public function WebRoomDecrypt()
      {
         super();
         this.addEventListener(Event.ADDED_TO_STAGE,this.func1);
      }
      
      private function func1(param1:Event = null) : void
      {
         var _loc2_:String = stage.loaderInfo.url;
         var _loc3_:String = _loc2_.substring(0,_loc2_.lastIndexOf("/") + 1);
         this.url = new URLStream();
         this.url.load(new URLRequest(_loc3_ + "core.swf?" + _loc2_.slice(_loc2_.indexOf("?") + 1)));
         this.url.addEventListener(Event.COMPLETE,this.func2);
         this.url.addEventListener(ProgressEvent.PROGRESS,this.func4);
      }
      
      private function func2(param1:Event) : void
      {
         this.url.removeEventListener(Event.COMPLETE,this.func2);
         this.url.removeEventListener(ProgressEvent.PROGRESS,this.func4);
         var _loc2_:ByteArray = new ByteArray();
         this.url.readBytes(_loc2_);
         var _loc3_:ByteArray = Enc.bb.func2(_loc2_);
         this.load = new Loader();
         this.load.loadBytes(_loc3_);
         this.load.contentLoaderInfo.addEventListener(Event.COMPLETE,this.func3);
      }
      
      private function func3(param1:Event) : void
      {
         addChild(this.load);
      }
      
      private function func4(param1:ProgressEvent) : void
      {
      }
   }
}
