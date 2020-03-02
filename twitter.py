# Import
from twython import Twython
import Julia2D as jl
import logging
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

# Var
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

jl.main()

image = open("Exports/export-"+str(jl.today)+".png", 'rb')
response = twitter.upload_media(media=image)
media_id = [response['media_id']]
twitter.update_status(status=jl.main(), media_ids=media_id)
