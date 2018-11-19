import tweepy as tp
import requests
from bs4 import BeautifulSoup as bs
import urllib
import random

meme_ids = []

#Function that finds the meme by separating the specified search term from the Tweet.
def memeFinder(tweets):
    search = tweets.split("!", 1)[1].strip()
    print(search)

    url = "https://www.memedroid.com/search?query=" + search
    html = requests.get(url)
    soup = bs(html.text, "html.parser")

    images = soup.findAll("img")

#Loop that iterates through the list of image URLs in 'images' and chooses a random one between indexes 0 and 14 that will be uploaded to Twitter.
    for image in images:
            temp = (image.get("src"))
            try:
                if temp[:random.randint(0,15)] == "h":
                    print(temp)
                    image_file = open("meme.jpeg", "wb")
                    image_file.write(urllib.request.urlopen(temp).read())
                    image_file.close()
            except:
                pass

#Bot logging in.
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

#The search term the bot searches for. I kept this quite unique so there wouldn't be any clashes with other Twitter users while testing.
tweet = api.search(q="Amazing Twitter Meme Bot, respond to me!")

#Main loop that makes use of the 'memeFinder' function and replies to the user with a meme of the theme they wanted.
for twt in tweet:
    if twt.text:
        memeFinder(twt.text)
        meme = api.media_upload("meme.jpeg")
        meme_ids.append(meme.media_id)
        twt_user = twt.user.screen_name
        print(twt)
        print(twt.id)
        api.create_favorite(twt.id)
        twt = api.update_status(status="@" + twt_user + " Enjoy your meme!", in_reply_to_status_id=twt.id, media_ids=meme_ids)
