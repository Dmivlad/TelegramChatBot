import unittest
from unittest.mock import patch, AsyncMock
from aiogram import types

from bot import config
from bot.core.main import start_command_handler, admin_info_command_handler, any_message_handler


class TestBot(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        """
        Setup for bot async test functions.
        Creates a test message for bot.
        :return:
        """
        self.message_mock = types.Message(
            message_id=1,
            date=1597802801,
            chat=types.Chat(
                id=12345,
                type='PRIVATE',
            ),
            from_user=types.User(
                id=12345,
                first_name='John',
                username='johndoe',
                is_bot=False
            )
        )

    @patch('aiogram.types.Message.answer', new_callable=AsyncMock)
    async def test_start_command_handler(self, answer_mock):
        """
        Test for handling command "/start"
        :param answer_mock: Mock which replaces actual types.Message.answer function in aiogram.
        :return:
        """
        await start_command_handler(self.message_mock)

        answer_mock.assert_called_once_with(text="Hello John :)!\nHow is your day?")

    @patch('aiogram.types.Message.answer', new_callable=AsyncMock)
    async def test_admin_info_command_handler(self, answer_mock):
        """
        Test for handling command "/admin_info"
        :param answer_mock: Mock which replaces actual types.Message.answer function in aiogram.
        :return:
        """
        await admin_info_command_handler(self.message_mock)

        answer_mock.assert_called_once_with(text=f"The creator of the bot is {config.YOUR_NAME}.\n"
                                                 "Thank you for using it! Hope you like it!\n"
                                                 f"If you want to contact with me, "
                                                 f"write me in {config.YOUR_MESSENGER} -> {config.MESSENGER_LINK}")

    @patch('aiogram.types.Message.answer', new_callable=AsyncMock)
    async def test_any_message_handler(self, answer_mock):
        """
        Test for handling any user's text.
        :param answer_mock: Mock which replaces actual types.Message.answer function in aiogram.
        :return:
        """
        await any_message_handler(self.message_mock)

        answer_mock.assert_called_once_with(text="Sorry, can't handle that type of message now!\n"
                                                 "Use the offered commands Bot can work with :)")


if __name__ == '__main__':
    unittest.main()
