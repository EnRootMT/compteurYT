import re
import time
import argparse
import requests
import json
from googleapiclient.discovery import build
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT



youtube = build('youtube', 'v3', developerKey='CLE_APIYT')
request = youtube.channels().list(part='statistics', id='ID_CHAINE' )
response: object = request.execute()


def demo(n, block_orientation, rotate, inreverse):
    # create matrix device

    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)

    # start demo
     
    i = 0
    while i == 0 :
        
        response: object = request.execute()
        abo = response['items'][0]['statistics']['subscriberCount']
        abok = str(float(float(abo)/1000))+"K"

        with canvas(device) as draw:
            text(draw, (0, 0), abok, fill="white", font=proportional(CP437_FONT))
        time.sleep(5)
        print(abok)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=1, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=0, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0, 1=90, 2=180, 3=270')
    parser.add_argument('--reverse-order', type=bool, default=False, help='Set to true if blocks are in reverse order')

    args = parser.parse_args()

    try:
        demo(args.cascaded, args.block_orientation, args.rotate, args.reverse_order)
    except KeyboardInterrupt:
        pass
