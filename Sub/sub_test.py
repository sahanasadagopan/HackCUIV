import time
import json
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory

pnconf = PNConfiguration()
pnconf.publish_key = "pub-c-0dee2dd3-f22e-4d01-b741-ebe89f355b68"
pnconf.subscribe_key = "sub-c-3f7513e0-19a9-11e8-95aa-1eb18890f15d"
pnconf.enable_subscribe = True

pubnub = PubNub(pnconf)

class MySubscribeCallback(SubscribeCallback):
	def presence(self, pubnub, presence):
		pass
	def message(self, pubnub, message):
		print (str(message.message))
		print(str(message.channel))
	def status(self, pubnub, status):
		print(status)
	def onResponse( data, channel ):
    		print("Channel: %s | Req: %s" % (channel,data))
listner = MySubscribeCallback()

pubnub.add_listener(listner)
pubnub.subscribe().channels('echo-server').execute()
time.sleep(60)
