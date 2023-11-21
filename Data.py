from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey, hello {}

Welcome to {}

You can use me to manage channels with tons of features. Use below buttons to learn more !

By @The_Panda_Official
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ My Bot In Portuguese ✨", url="https://t.me/Demonick_xyz_robot")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🛸 About 🛸", callback_data="about")
        ],
        [InlineKeyboardButton("🎭 Developer 🎭", url="https://t.me/The_Panda_Official")],
        [InlineKeyboardButton("🎨 Channel 🎨", url="https://t.me/botssaved")],
    ]

    # Help Message
    HELP = """
Everything is self explanatory after you add a channel.
To add a channel use keyboard button 'Add Channels' or alternatively for ease, use `/add` command

🛸 **Available Commands** 🛸

/about - About The Bot
/help - This Message
/start - Start the Bot

Alternative Commands
/channels - List added Channels
/add - Add a channel
/report - Report a Problem
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram channel automation bot by @botssaved

Channel : [Click Here](https://t.me/botssaved)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @The_Panda_Official
    """
