# Twitter-Meme-Bot
Bot that makes use of the Tweepy library to reply to Tweets with memes.

# How It Works
The bot searches for tweets that include a specific phrase. In this case I used something unique, so that I could easily test the bot.
```

tweet = api.search(q="Amazing Twitter Meme Bot, respond to me!")

```
An example would be (as shown in the screenshot below) 'Amazing Twitter Meme Bot, respond to me! Minecraft'. The bot would then split the string into two substrings from the "!" to get what I call the 'search term', which in this case is 'Minecraft'.
```

search = tweets.split("!", 1)[1].strip()

```
Continuing from the example, the bot would then search 'Minecraft' on memedroid.com to find the latest Minecraft related memes uploaded onto the site. It will then find all the images by finding everything with the 'img' tag on the page.
```

url = "https://www.memedroid.com/search?query=" + search
    html = requests.get(url)
    soup = bs(html.text, "html.parser")

    images = soup.findAll("img")

```
A loop was then used to find a random meme on the page and save it for it to be later uploaded onto Twitter. Afterwards, the Tweet is finally sent with the meme.
```

 twt = api.update_status(status="@" + twt_user + " Enjoy your meme!", in_reply_to_status_id=twt.id, media_ids=meme_ids)

```

# Example
![alt text](https://github.com/ANevgi/Twitter-Meme-Bot/blob/master/TwitterMemeBotExample.PNG?raw=true)
