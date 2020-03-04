"""Python Julia set generator for the twitter account FractalDiary.

by : Chittaro Hugo
"""
# Import
from twython import Twython
import Julia2DNumba as jl
import logging
import color as cl
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Logging config
logging.basicConfig(filename='log',
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logging.info('Started twitter.py')

# Var
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Colormap
anchor = {'#000764': 0,
          '#206bcb': 0.16,
          '#edffff': 0.42,
          '#ffaa00': 0.6425,
          '#000200': 0.8575,
          '#000765': 1}
customcmap = cl.colorMapCustomDist(**anchor)

# jl.main(cmap=customcmap)

message = jl.julia_set(width=12000, height=12000, cmap=customcmap)

try:
    image = open("Exports/export-"+str(jl.today)+".png", 'rb')
    response = twitter.upload_media(media=image)
    media_id = [response['media_id']]
    twitter.update_status(status=message, media_ids=media_id)
except:
    logging.error('Can\'t post on twitter')
