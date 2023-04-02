from aiogram import Dispatcher
from aiogram.types import Message


async def echo(msg: Message):
    """Echo example for test."""
    # todo: remove echo example:3
    await msg.answer(msg.text)


def register_all_handlers(dp: Dispatcher) -> None:
    """Add all handlers to bot."""
    # todo: register all handlers
    dp.register_message_handler(echo, content_types=["text"])
