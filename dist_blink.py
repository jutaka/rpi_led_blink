import webiopi

#--
# 近づくとドキドキ
#--

webiopi.setDebug()

GPIO = webiopi.GPIO
DIST_PIN = 16        # 距離センサのVo
LED_PIN  = 21        # LEDのVin

def setup():
        webiopi.debug("Setup start")
        GPIO.setFunction( DIST_PIN, GPIO.IN )
        GPIO.setFunction( LED_PIN, GPIO.OUT )
        webiopi.debug("Setup end")

def loop():
        GPIO.digitalWrite( LED_PIN, True )
        value = GPIO.input( DIST_PIN )
        webiopi.debug("value is " + str(value))

        if value == True:
                webiopi.sleep( 0.7 )
                GPIO.digitalWrite( LED_PIN, False )
                webiopi.sleep( 0.7 )
        else:
                webiopi.sleep( 3.0 )
                GPIO.digitalWrite( LED_PIN, False )
                webiopi.sleep( 1.0 )