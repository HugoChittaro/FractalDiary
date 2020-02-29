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

message = """Julia set | {}\n
Resolution : {} x {} ;
Iteration : {} ;
Colormap : {} ;
c = {} + {}i"""

jl.main()

image = open("Exports/export-"+str(jl.today)+".png", 'rb')
response = twitter.upload_media(media=image)
media_id = [response['media_id']]
twitter.update_status(status=message.format(str(jl.today),
                                            str(jl.h),
                                            str(jl.w),
                                            str(jl.max_iter),
                                            str(jl.cmap),
                                            str(jl.x),
                                            str(jl.y)), media_ids=media_id)
