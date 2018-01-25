# receive.py => A riff off of Tony DiCola's SimpleTest.py.  See send.py
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
#
# # Wait to receive packets.  Note that this library can't receive data at a fast
# # rate, in fact it can only receive and process one 60 byte packet at a time.
# # This means you should only use this for low bandwidth scenarios, like sending
# # and receiving a single message at a time.
print('Waiting for packets...')
while True:
    packet = rfm69.receive()
    # Optionally change the receive timeout from its default of 0.5 seconds:
    #packet = rfm69.receive(timeout_s=5.0)
    # If no packet was received during the timeout then None is returned.
    if packet is None:
        print('Received nothing! Listening again...')
    else:
        # Received a packet!
        # Print out the raw bytes of the packet:
        print('Received (raw bytes): {0}'.format(packet))
        # And decode to ASCII text and print it too.  Note that you always
        # receive raw bytes and need to convert to a text format like ASCII
        # if you intend to do string processing on your data.  Make sure the
        # sending side is sending ASCII data before you try to decode!
        packet_text = str(packet, 'ascii')
