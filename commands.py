from pyrogram import Client, filters


    @Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker(
        sticker="CAACAgIAAx0CVBD5pAACN5VjAqGYgoyg-OXjf0lNy0lgmhH37wACIAADlp-MDqz9QTP0qm_5HgQ",
        caption="""""",
    reply_markup=InlineKeyboardMarkup(
                [
                    InlineKeyboardButton(
                        "Endorsement", url="https://sociabuzz.com/iniokekkk/tribe"
                       ),
                  ]
             )
    )
