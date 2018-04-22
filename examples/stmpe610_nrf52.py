import busio
import board
import digitalio
from adafruit_stmpe610 import Adafruit_STMPE610_SPI
spi=busio.SPI(board.SCK,board.MOSI,board.MISO)
cs = digitalio.DigitalInOut(board.A6)
st=Adafruit_STMPE610_SPI(spi,cs)
print("Go Ahead - Touch the Screen - Make My Day!")
while True:
    if(not st.bufferEmpty):
        print(st.readData())
