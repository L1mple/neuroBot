import os
import subprocess

from aiogram import Dispatcher
from aiogram.types import Message, ParseMode


async def echo(message: Message):
    """Echo example for test."""
    # Download the voice message file
    voice_file = await message.voice.download()

    # Convert the voice message to WAV format using FFmpeg
    wav_file = os.path.splitext(voice_file.name)[0] + ".wav"
    subprocess.run(["ffmpeg", "-y", "-i", voice_file.name, wav_file])

    # Reply with a success message
    await message.reply("Success", parse_mode=ParseMode.HTML)

    # Clean up the temporary files
    os.remove(voice_file)
    os.remove(wav_file)


def register_all_handlers(dp: Dispatcher) -> None:
    """Add all handlers to bot."""
    # todo: register all handlers
    dp.register_message_handler(echo, content_types=["voice"])
