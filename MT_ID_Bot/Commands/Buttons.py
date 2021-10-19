from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("📢 BOT UPDATES", url=f"t.me/DB_BOTZ"),
       InlineKeyboardButton("Open SOURCE  💫", url=f"https://telegra.ph/file/c59c590677fe936ae5e89.jpg")
       ],[
       InlineKeyboardButton("⬇️ More Information ⬇️", callback_data="help")
       ]]
       )

HELP_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("Telegram Id ", callback_data="id"),
       InlineKeyboardButton("Telegram info", callback_data="info")
       ],[
       InlineKeyboardButton("🏠 home", callback_data="start"),
       InlineKeyboardButton("⬇️ Close", callback_data="close"),
       InlineKeyboardButton("🤠 About", callback_data="about")
       ]]
       )

ABOUT_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🔙 Back", callback_data="help"),
       InlineKeyboardButton("🏠 Home", callback_data="start"),
       InlineKeyboardButton("⬇️ Close", callback_data="close")
       ]]
       )
