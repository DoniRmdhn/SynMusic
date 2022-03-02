import os, pytube, requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from youtube_search import YoutubeSearch
from pytube import YouTube
from Yukki import app

CAPTION_TEXT = """
࿂ **Title:** `{}`
࿂ **Requester** : {}
࿂ **Downloaded Via** : `{}`
࿂ **Downloaded By :** @szrosebot
"""

CAPTION_BTN = InlineKeyboardMarkup(
            [[InlineKeyboardButton("News  Channel", url="https://t.me/szteambots")]])

async def downloadsong(m, message, vid_id):
   try: 
    m = await m.edit(text = f"📥 **Upload Started**\n@szteambots",
    reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("📥 Downloading...", callback_data="progress")]]))
    link =  YouTube(f"https://youtu.be/{vid_id}")
    thumbloc = link.title + "thumb"
    thumb = requests.get(link.thumbnail_url, allow_redirects=True)
    open(thumbloc , 'wb').write(thumb.content)
    songlink = link.streams.filter(only_audio=True).first()
    down = songlink.download()
    first, last = os.path.splitext(down)
    song = first + '.mp3'
    os.rename(down, song)
    m = await m.edit(text = """
📤 **Upload Started**
@szteambots
  """,
    reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("📤 Uploading...", callback_data="progress")]]))
    await message.reply_audio(song,
    caption = CAPTION_TEXT.format(link.title, message.from_user.mention if message.from_user else "Anonymous Admin", "Youtube"),
    thumb = thumbloc,
    reply_markup = CAPTION_BTN)
    await m.delete()
    if os.path.exists(song):
        os.remove(song)
    if os.path.exists(thumbloc):
        os.remove(thumbloc)
   except Exception as e:
       await m.edit(f"__Error occured. ⚠️ \nAnd also you can get a help from @slbotzone.__\n\n{str(e)}")

async def downlodvideo(m, message, vid_id):
   try: 
    m = await m.edit(text = "📥 Downloading...",
    reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("📥 Downloading...", callback_data="progress")]]))
    link =  YouTube(f"https://youtu.be/{vid_id}")
    videolink = link.streams.get_highest_resolution()
    video = videolink.download()
    m = await m.edit(text = "📤 Uploading...",
    reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("📤 Uploading...", callback_data="progress")]]))
    await message.reply_video(video, 
    caption=CAPTION_TEXT.format(link.title, message.from_user.mention if message.from_user else "Anonymous Admin", "Youtube"),
    reply_markup=CAPTION_BTN)
    await m.delete()
    if os.path.exists(video):
            os.remove(video)
   except Exception as e:
       await m.edit(f"__Error occured. ⚠️ \nAnd also you can get a help from @slbotzone.__\n\n{str(e)}")

@app.on_message(filters.command("song"))
async def songdown(_, message):
   try: 
    if len(message.command) < 2:
            return await message.reply_text("Give a song name ⚠️")
    m = await message.reply_text("🔎 Searching ...")
    name = message.text.split(None, 1)[1]
    vid_id = (YoutubeSearch(name, max_results=1).to_dict())[0]["id"]
    await downloadsong(m, message, vid_id)
   except Exception as e:
       await m.edit(f"""
**Nothing Found** {message.from_user.mention}   
Please check, you using correct format or your spellings are correct and try again!
Use help Menu : /help 
       """)

@app.on_message(filters.command("video"))
async def videodown(_, message):
   try: 
    if len(message.command) < 2:
            return await message.reply_text("Give a song name ⚠️")
    m = await message.reply_text("🔎 Searching ...")
    name = message.text.split(None, 1)[1]
    vid_id = (YoutubeSearch(name, max_results=1).to_dict())[0]["id"]
    await downlodvideo(m, message, vid_id)
   except Exception:
       await m.edit(f"""
**Nothing Found** {message.from_user.mention}    
Please check, you using correct format or your spellings are correct and try again!
Use help Menu : /help 
       """)
