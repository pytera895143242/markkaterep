from aiogram import executor
from misc import dp
import handlers
import asyncio

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)