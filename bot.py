from pyrogram import filters, Client
from pyrogram.types import Message
from requests import get
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

logo = Client("logo Bot", bot_token = BOT_TOKEN, api_id = API_ID, api_hash = API_HASH)

#Caption for Logo
caption01 = """
✍️ Logo Generated Successfully✅
◇───────────────◇
🔥 **Created By** : **[DK LOGO GENERATOR BOT 😈](https://t.me/DK_Logo_Gen_Bot)**
🌷 **Requestor** : ** {} **
⚡️ **Powered By **  : **[👨‍💻 DK Bots 😈 ](https://t.me/DK_Bots)**
◇───────────────◇️  
A Bot Developed By (DK Bots 🇱🇰 corporation ©)[https://t.me/DK_Bots].
**All Right Reserved**⚠️️
    """

#Caption for HQ Logo
caption02 = """
✍️ HQ Logo Generated Successfully✅
◇───────────────◇
🔥 **Created By** : **[DK LOGO GENERATOR BOT 😈](https://t.me/DK_Logo_Gen_Bot)**
🌷 **Requestor** : ** {} **
⚡️ **Powered By **  : **[👨‍💻 DK Bots 😈 ](https://t.me/DK_Bots)**
◇───────────────◇️  
🤞A Bot Developed By 👨‍💻(DK Bots 🇱🇰 corporation ©)[https://t.me/DK_Bots].
**All Right Reserved**⚠️️
    """
#◇───────────────────────────────────────◇ 

#◇───────────────────────────────────────◇ 

#Start MSG
@logo.on_message(filters.command(["start", f"start@DK_Logo_Gen_Bot"]))
async def start(client,message):
    await message.reply(f"""👋 Hey there {message.from_user.mention} !
🙋‍♂️ This is (DK LOGO GENERATOR BOT)[https://t.me/DK_Logo_Gen_Bot]
**I specialize for logo design  Services with Amazing Logo Creator Platform.**

**My Tasks :-**

    🌺 Generating logo
    🚀 Generating 4k logo
    🎯 24 horse active
    
    
🔥 Bot Commands 🔥
      
    `/logo DK Bots`
    `/logohq DK Bots`
    
🌿 Developer : @Hasith_Kaushalya

**Powered by**:
    ◈ Single Developers Logo Creator API
    ◈ (DK Bots)[http://t.me/DK_Bots]
    ◈ Pyrogram
🤞A Bot Developed By 👨‍💻(DK Bots 🇱🇰 corporation ©)[https://t.me/DK_Bots].
©2022**All Right Reserved**⚠️️""",
                       reply_markup=InlineKeyboardMarkup(
                           [
                                [
                                    InlineKeyboardButton(text="➕Add me to your group➕", url=f"http://t.me/DK_Logo_Gen_Bot?startgroup=botstart")
                                ]
                                [
                                    InlineKeyboardButton(text="🗣Join Updates🗣", url=f"http://t.me/DK_Bots"),
                                    InlineKeyboardButton(text="👀Support👀", url=f"http://t.me/Hasith_Kaushalya_bot")
                                ]
                                [
                                    InlineKeyboardButton(text="👨‍💻Developer🤞", url=f"http://t.me/Hasith_Kaushalya")
                                ]
                           ]    
                       ),
                      )
#◇───────────────────────────────────────◇ 

#Help MSG
@logo.on_message(filters.command(["help", f"help@DK_Logo_Gen_Bot"]))
async def help(client,message):
    await message.reply(f"""**Help Menu** : 
◈ `/logo <you name>`    - To make a normal logo from your name.
◈ `/logohq <your name>` - To make a High Quality Logo from your name.

**Powered By ~ @DK_Bots**
©2022**All Right Reserved**⚠️️""",
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="🗣Join Updates🗣", url=f"http://t.me/DK_Bots")
            ]
        ]
    ),
    )

#◇───────────────────────────────────────◇ 

#Logo creator
@logo.on_message(filters.command(["logo", f"logo@DK_Logo_Gen_Bot"]))
async def on_off_antiarab(_, message: Message):
    m = await message.reply_text("♻Creating your Logo♻......\n\n[░░░░░░░░░░] 00%")
    await m.edit("♻Creating your Logo♻......\n\n[▇▇░░░░░░░░] 20%")
    await m.edit("♻Creating your Logo♻......\n\n[▇▇▇▇░░░░░░] 40%")
    await m.edit("♻Creating your Logo♻......\n\n[▇▇▇▇▇░░░░░] 50%")
    await m.edit("♻Creating your Logo♻......\n\n[▇▇▇▇▇▇▇░░░] 70%")
    await m.edit("♻Creating your Logo♻......\n\n[▇▇▇▇▇▇▇▇░░] 80%")
    await m.edit("♻Creating your Logo♻......\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
    text = message.text.split(None, 1)[1]
    photo = get((f"https://single-developers.up.railway.app/logo?name={text}").replace(' ','%20')).history[1].url
    await m.edit("📤Uploading.....")
    await m.delete()
    await logo.send_photo(message.chat.id, photo=photo, caption =caption01.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•••Telegraph Link•••", url=f"{photo}"
                    )
                ]
            ]
          ),
    )

#◇────────────────────────────────────◇ 

#HQ Logo creator
@logo.on_message(filters.command(["logohq", f"logohq@DK_Logo_Gen_Bot"]))
async def on_off_antiarab(_, message: Message):
    m = await message.reply_text("♻Creating your HQ Logo♻......\n\n[░░░░░░░░░░] 00%")
    await m.edit("♻Creating your HQ Logo♻......\n\n[▇▇░░░░░░░░] 20%")
    await m.edit("♻Creating your HQ Logo♻......\n\n[▇▇▇▇░░░░░░] 40%")
    await m.edit("♻Creating your HQ Logo♻......\n\n[▇▇▇▇▇░░░░░] 50%")
    await m.edit("♻Creating your HQ Logo♻......\n\n[▇▇▇▇▇▇▇░░░] 70%")
    await m.edit("♻Creating your HQ Logo♻......\n\n[▇▇▇▇▇▇▇▇░░] 80%")
    await m.edit("♻Creating your HQ Logo♻......\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
    text = message.text.split(None, 1)[1]
    photo = get((f"https://single-developers.up.railway.app/logohq?name={text}").replace(' ','%20')).history[1].url
    await m.edit("📤Uploading.....")
    await m.delete()
    await logo.send_photo(message.chat.id, photo=photo, caption =caption02.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•••Telegraph Link•••", url=f"{photo}"
                    )
                ]
            ]
          ),
    )


logo.run()

app.start()
LOGGER.info(f"""DK Bots 🇱🇰 corporation ©
▒█▀▀▄ ▒█░▄▀ ░░ ▒█▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ 
▒█░▒█ ▒█▀▄░ ▀▀ ▒█▀▀▄ █░░█ ░░█░░ ▀▀█ 
▒█▄▄▀ ▒█░▒█ ░░ ▒█▄▄█ ▀▀▀▀ ░░▀░░ ▀▀▀""")
idle()
