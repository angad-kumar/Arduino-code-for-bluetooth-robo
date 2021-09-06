import subprocess
import socket
from RPLCD.i2c import CharLCD
import time
lcd = CharLCD('PCF8574', 0x27)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)
front = (
  0b00100,
  0b01010,
  0b10001,
  0b00000,
  0b00100,
  0b01010,
  0b00000,
  0b00100
)
def main():
    try:
        cmd = "iwconfig wlan0 | grep -i signal | /usr/bin/awk '{print $4}' | /usr/bin/cut -d'=' -f2"
        output = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]
        print(output.strip()) # For single line output.
        quality =int( 2 *(int(output.strip()) + 90))
        print(quality)
        lcd.clear()
        lcd.cursor_pos = (0,15)
        lcd.create_char(0, front)
        lcd.write_string(unichr(0))
        lcd.cursor_pos = (0,16)
        lcd.write_string(str(quality))
        lcd.write_string('%')
#       lcd.clear()
        time.sleep(5)
        lcd.clear()
    except:
        lcd.cursor_pos = (0,0)
        lcd.write_string('No Internet')
#lcd.cursor_pos(3,16)
#lcd.write_string('WiFi')
while(1):
        main()