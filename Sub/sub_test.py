import time
import json
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
import RPi.GPIO as GPIO 

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
		data =str( message.message)
		split_data = data.split("""u'""")
		print(split_data)
		byte = str(split_data);
                #byte = split_data[1].split(":");
                if byte.find("left_byte': 15, ")>0:
                    GPIO.setmode(GPIO.BCM)
                    LED = 13
                    GPIO.setup(LED, GPIO.OUT)
                    GPIO.output(LED,GPIO.HIGH)
		elif byte.find("left_byte': 9, ")>0:
		   GPIO.setmode(GPIO.BCM)
                   LED = 19
                   GPIO.setup(LED, GPIO.OUT)
                   GPIO.output(LED,GPIO.HIGH)
		elif byte.find("left_byte': 0, ")>0:
		   GPIO.setmode(GPIO.BCM)
                   LED = 26
                   GPIO.setup(LED, GPIO.OUT)
                   GPIO.output(LED,GPIO.HIGH)
		else:
		   GPIO.setmode(GPIO.BCM)
                   LED1 = 19
		   LED2 = 13
		   LED3 = 26
                   GPIO.setup(LED1, GPIO.OUT)
                   GPIO.output(LED1,GPIO.LOW) 
		   GPIO.setup(LED2, GPIO.OUT)
                   GPIO.output(LED2,GPIO.LOW)
                   GPIO.setup(LED3, GPIO.OUT)
                   GPIO.output(LED3,GPIO.LOW)


	def status(self, pubnub, status):
		print(status)
	def onResponse( data, channel ):
    		print("Channel: %s | Req: %s" % (channel,data))
listner = MySubscribeCallback()

pubnub.add_listener(listner)
pubnub.subscribe().channels('echo-server').execute()
time.sleep(60)
