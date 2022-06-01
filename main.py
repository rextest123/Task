import pickle
import time

# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.dispatcher.filters import Command
# from selenium.webdriver.common.by import By
from aiogram import Dispatcher, executor, Bot, types
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

bot = Bot(token="5379391361:AAHnBd7aWw0afk8MJFArzQokqyX1unJG0i4")
dp = Dispatcher(bot)


@dp.message_handler(text="/search")
async def search(message: types.Message):
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    driver = webdriver.Chrome('chromedriver.exe')

    driver.get('http://127.0.0.1:8000/admin')
    time.sleep(3)
    # pickle.dump(driver.get_cookies(), open("cookies", "wb"))
    # print("ok!")

    for cookie in pickle.load(open("cookies", "rb")):
        driver.add_cookie(cookie)

    driver.get("http://127.0.0.1:8000/adminmain/task/")
    divs = driver.find_element(By.CLASS_NAME, "results")

    await message.answer(str(divs.text))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)