import webiopi

#--
#  Raspberry PI B+ でLチカ
#--
#
# o GPIOの右端の端子を利用
#   □□□□.......□□□□■ <- GPIO#21
#   □□□□.......□□□□■ <- Ground
# 
# o webiopiから利用
# 

webiopi.setDebug()

GPIO = webiopi.GPIO
LEDPIN = 21

def setup():
        webiopi.debug("Setup start")
        GPIO.setFunction( LEDPIN, GPIO.OUT )
        webiopi.debug("Setup end")

def loop():
        GPIO.digitalWrite( LEDPIN, True )
        webiopi.sleep( 3.0 )
        GPIO.digitalWrite( LEDPIN, False )
        webiopi.sleep( 1.0 )