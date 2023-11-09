#!/usr/bin/env python3
import asyncio
import logging
import sys

from aiogram.filters import Command
from aiogram import Bot, types
from aiogram import Dispatcher

try:  # Checking if the user has put his own bot TOKEN in config.py
    from bot import config
except ImportError:
    exit("Please, before using the bot, delete .txt in config.py.txt and put your bot TOKEN in.")

dispatcher = Dispatcher()  # Class object to handle events


@dispatcher.message(Command("start"))
async def start_command_handler(message: types.Message) -> None:
    """
    Function for handling "/start" command.
    :param message: types.Message
    :return: None
    """
    await message.answer(text=f"Hello {message.from_user.first_name} :)!\nHow is your day?")


@dispatcher.message(Command("admin_info"))
async def admin_info_command_handler(message: types.Message) -> None:
    """
    Function for handling "/admin_info" command.
    Showing info about the creator of the bot and the link to his messenger's account.
    :param message: types.Message
    :return: None
    """
    await message.answer(text=f"The creator of the bot is {config.YOUR_NAME}.\n"
                              "Thank you for using it! Hope you like it!\n"
                              f"If you want to contact with me, write me in {config.YOUR_MESSENGER} -> "
                              f"{config.MESSENGER_LINK}")


@dispatcher.message()
async def any_message_handler(message: types.Message) -> None:
    """
    Function for handling any message if there is no right command to handle.
    :param message: types.Message
    :return: None
    """
    await message.answer(text="Sorry, can't handle that type of message now!\n"
                              "Use the offered commands Bot can work with :)")


async def main() -> None:
    logging.basicConfig(level=logging.INFO,
                        stream=sys.stdout,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    bot = Bot(config.TOKEN)
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
