# Riff of Tony DiCola's SimpleTest.py which is included with the RFM69 library.
# Because SimpleTest sent only once, the RFM69 Feather set up to receive would
# miss the packet.  I decided to break simpletest into two .py files - one to send
# a packet, the other to receive a packet.
import board
import busio
import digitalio

import adafruit_rfm69

# Define radio parameters.
RADIO_FREQ_MHZ = 915.0  # Frequency of the radio in Mhz. Must match your
                          # module! Can be a value like 915.0, 433.0, etc.
# Define pins connected to the chip.
CS = digitalio.DigitalInOut(board.RFM69_CS)
RESET = digitalio.DigitalInOut(board.RFM69_RST)

# Initialize SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialze RFM radio
rfm69 = adafruit_rfm69.RFM69(spi, CS, RESET, RADIO_FREQ_MHZ)

while True:
# # Send a packet.  Note you can only send a packet up to 60 bytes in length.
# # This is a limitation of the radio packet size, so if you need to send larger
# # amounts of data you will need to break it into smaller send calls.  Each send
# # call will wait for the previous one to finish before continuing.
    rfm69.send('Hello world!\r\n')
    print('Sent hello world message!')
