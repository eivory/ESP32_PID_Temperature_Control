import machine, display, utime, math
from machine import Pin, ADC
import rolling_avg #user defined function

#display setup
tft = display.TFT() 
tft.init(tft.ST7789,bgr=False,rot=tft.LANDSCAPE, miso=17,backl_pin=4,backl_on=1, mosi=19, clk=18, cs=5, dc=16)
tft.setwin(40,52,320,240)
tft.clear()
tft.set_fg(0xFFFFFF)
hz = 1 #display refresh Hz

#thermister setup
thm = ADC(Pin(36))         # https://randomnerdtutorials.com/esp32-esp8266-analog-readings-micropython/
thm.atten(ADC.ATTN_11DB)       #Full range: 3.3v
off = 42 # I vary from the tutorial here because I get negative valuse at room temperature if I don't.

#display loop 
while True:
    adc_val = thm.read() #reads pin 36 thermistor value 
    therm_v = (adc_val/4095)*3.3 
    tr = (((therm_v - 1.22) / .005)+ off) # tr=temp_raw , https://learn.adafruit.com/ad8495-thermocouple-amplifier/python-circuitpython
    text = str(rolling_avg.ra(tr,hz*40))
    tft.text(120-int(tft.textWidth(text)/2), 67-int(tft.fontSize()[1]/2), text, 0xFFFFFF) #centers variable text on display.
    utime.sleep(1/hz)
    tft.text(120-int(tft.textWidth(text)/2), 67-int(tft.fontSize()[1]/2), text, 0x000000)
    print(rolling_avg.ra(tr,hz*40))