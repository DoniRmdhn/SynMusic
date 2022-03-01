import asyncio

from pyrogram import Client, filters
from Yukki import app, OWNER_ID
from Yukki import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5, SUDOERS)


@app.on_message(filters.command("joinall") & filters.user(SUDOERS))
async def join(client, message):
  await ASS_CLI_1.join_chat("-1001608959025")
  await ASS_CLI_2.join_chat("-1001608959025")
  await ASS_CLI_3.join_chat("-1001608959025")
  await ASS_CLI_4.join_chat("-1001608959025")
  await ASS_CLI_5.join_chat("-1001608959025")

@ASS_CLI_1.on_message(filters.command("userbotleaveall") & filters.user(SUDOERS))
async def bye(client, message):
        left = 0
        failed = 0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in ASS_CLI_1.iter_dialogs():
            try:
                await ASS_CLI_1.leave_chat(dialog.chat.id)
                left = left + 1
                await lol.edit(
                    f"Assistant leaving... Left: {left} chats. Failed: {failed} chats."
                )
            except:
                failed = failed + 1
                await lol.edit(
                    f"Assistant leaving... Left: {left} chats. Failed: {failed} chats."
                )
            await asyncio.sleep(0.7)
        await client.send_message(
            message.chat.id, f"Left {left} chats. Failed {failed} chats."
        )

@ASS_CLI_2.on_message(filters.command("userbotleaveall") & filters.user(SUDOERS))
async def bye(client, message):
        left = 0
        failed = 0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in ASS_CLI_2.iter_dialogs():
            try:
                await ASS_CLI_2.leave_chat(dialog.chat.id)
                left = left + 1
                await lol.edit(
                    f"Assistant leaving... Left: {left} chats. Failed: {failed} chats."
                )
            except:
                failed = failed + 1
                await lol.edit(
                    f"Assistant leaving... Left: {left} chats. Failed: {failed} chats."
                )
            await asyncio.sleep(0.7)
        await client.send_message(
            message.chat.id, f"Left {left} chats. Failed {failed} chats."
        )
        
@ASS_CLI_3.on_message(filters.command("userbotleaveall") & filters.user(SUDOERS))
async def bye(client, message):
        left = 0
        failed = 0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in ASS_CLI_3.iter_dialogs():
            try:
                await ASS_CLI_3.leave_chat(dialog.chat.id)
                left = left + 1
                await lol.edit(
                    f"Assistant leaving... Left: {left} chats. Failed: {failed} chats."
                )
            except:
                failed = failed + 1
                await lol.edit(
                    f"Assistant leaving... Left: {left} chats. Failed: {failed} chats."
                )
            await asyncio.sleep(0.7)
        await client.send_message(
            message.chat.id, f"Left {left} chats. Failed {failed} chats."
        )  
        
@ASS_CLI_4.on_message(filters.command("userbotleaveall") & filters.user(SUDOERS))
async def bye(client, message):
        left = 0
        failed = 0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in ASS_CLI_4.iter_dialogs():
            try:
                await ASS_CLI_4.leave_chat(dialog.chat.id)
                left = left + 1
                await lol.edit(
                    f"Assistant leaving... Left: {left} chats. Failed: {failed} chats."
                )
            except:
                failed = failed + 1
                await lol.edit(
                    f"Assistant leaving... Left: {left} chats. Failed: {failed} chats."
                )
            await asyncio.sleep(0.7)
        await client.send_message(
            message.chat.id, f"Left {left} chats. Failed {failed} chats."
        )  
        
@ASS_CLI_5.on_message(filters.command("userbotleaveall") & filters.user(SUDOERS))
async def bye(client, message):
        left = 0
        failed = 0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in ASS_CLI_5.iter_dialogs():
            try:
                await ASS_CLI_5.leave_chat(dialog.chat.id)
                left = left + 1
                await lol.edit(
                    f"Assistant leaving... Left: {left} chats. Failed: {failed} chats."
                )
            except:
                failed = failed + 1
                await lol.edit(
                    f"Assistant leaving... Left: {left} chats. Failed: {failed} chats."
                )
            await asyncio.sleep(0.7)
        await client.send_message(
            message.chat.id, f"Left {left} chats. Failed {failed} chats."
        )          