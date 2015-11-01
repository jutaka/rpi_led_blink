#!/usr/bin/python
# -*0 coding: utf-8 -*-

#--
# WebIOpi用スクリプト
#--
# o Lチカ
# o 距離センサーで近づくとドキドキ
# o シャットダウンボタン

import webiopi
import syslog
import time
import os

webiopi.setDebug()

GPIO = webiopi.GPIO
DIST_PIN =  4        # 距離センサのVo
LED_PIN  = 21        # LEDのVin
SHUT_PIN = 24        # シャットダウンボタン

def setup():
	webiopi.debug("Setup start")
	GPIO.setFunction( DIST_PIN, GPIO.IN )
	GPIO.setFunction( LED_PIN, GPIO.OUT )
	GPIO.setFunction( SHUT_PIN, GPIO.IN )
	webiopi.debug("Setup end")

def loop():
	GPIO.digitalWrite( LED_PIN, True )
	value = GPIO.input( DIST_PIN )
	webiopi.debug("value is " + str(value))

	if GPIO.input( SHUT_PIN ):
		is_cancel = False
		for i in range(10):
			if GPIO.input( SHUT_PIN ):
				webiopi.debug("push continue.")
			else:
				is_cancel = True
				webiopi.debug("push canceled.!! ")
				break
			webiopi.sleep( 0.05 )

		if is_cancel == False:
			webiopi.debug("SHUTDOWN_BTN pushed. !!!!")
			count = 16
			while count > 0:
				count = count - 1
				GPIO.digitalWrite( LED_PIN, True )
				webiopi.sleep( 0.3 )
				GPIO.digitalWrite( LED_PIN, False )
				webiopi.sleep( 0.3 )

			# シャットダウン
			os.system("sudo shutdown -h now")

	# 点滅どきどき
	if value == True:
		webiopi.sleep( 0.7 )
		GPIO.digitalWrite( LED_PIN, False )
		webiopi.sleep( 0.7 )
	# 点滅通常
	else:
		webiopi.sleep( 3.0 )
		GPIO.digitalWrite( LED_PIN, False )
		webiopi.sleep( 1.0 )