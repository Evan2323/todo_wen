from app import bot, dp
from aiogram.types import Message
from config import admin_id, todo, HELP
import time


async def send_to_admin(dp):
  await bot.send_message(chat_id = admin_id, text = "Бот запущен!")

@dp.messege_hendler(command = ["start"])
async def start(massage:Messege):
  await messege.answer("Работает")

  @dp.messege_hendler(command = ["add"])
async def add(massage:Messege):
  await messege.answer("Работает")

  @dp.messege_hendler(command = ["show"])
async def show(massage:Messege):
  await messege.answer("Работает")

  @dp.messege_hendler(command = ["done"])
async def done(massage:Messege):
  await messege.answer("Работает")

@dp.messege_hendler(command = ["help"])
async def help(massage:Messege):
  await messege.answer(HELP)

  @dp.messege_hendler(command = ["start"])
async def text(massage:Messege):
  await messege.answer(text = messege.text)