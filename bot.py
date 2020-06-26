import telebot
import time as tm
from telebot import types
from modul.config import BOT_TOKEN
from modul.egs import egs
from modul.currency import currency
from modul.jagatplay import jagatplay
from modul.steam import steam
from modul.winpoin import winpoin

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)

@bot.message_handler(commands=['start'])
def command_start(message):
	start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
	start_markup.row('/start', '/help', '/hide','/top_steam')
	start_markup.row('/jagatplay', '/usd', '/free_game','/winpoin')
	bot.send_message(message.chat.id, "🤖 Bot telah aktif!\n⚙ Enter /help Untuk melihat fungsi bot")
	bot.send_message(message.from_user.id, "⌨️ The Keyboard is added!\n⌨️ /hide To remove keyboard ", reply_markup=start_markup)

@bot.message_handler(commands=['hide'])
def command_hide(message):
	hide_markup = telebot.types.ReplyKeyboardRemove()
	bot.send_message(message.chat.id, "⌨💤...", reply_markup=hide_markup)

@bot.message_handler(commands=['help'])
def command_help(message):
	bot.send_message(message.chat.id, "🤖 /start 	 		- Tampilkan Keyboard\n"
									  "🎮 /free_game 		- Game Gratis EGS\n"
                                      "📰 /jagatplay 	 	- Update Artikel Jagat Play\n"
									  "📰 /winpoin 	 		- Update Artikel WinPoin\n"
									  "💻 /top_steam 		- Top Seller Steam\n"
									  "💰  /usd	 			 - Konversi USD > IDR")

@bot.message_handler(commands=['jagatplay'])
def command_news(message):
	bot.send_message(message.chat.id, "🆕 Update Artikel Jagat Play\n")
	bot.send_message(message.chat.id, jagatplay(), parse_mode='HTML')

@bot.message_handler(commands=['free_game'])
def command_news(message):
	bot.send_message(message.chat.id, "🆕 Game Gratis EGS:\n")
	bot.send_message(message.chat.id, egs(), parse_mode='HTML')

@bot.message_handler(commands=['usd'])
def command_news(message):
	bot.send_message(message.chat.id, "💰 Konversi\n")
	bot.send_message(message.chat.id, currency(), parse_mode='HTML')

@bot.message_handler(commands=['top_steam'])
def command_news(message):
	bot.send_message(message.chat.id, "🆕 Steam top seller now\n")
	bot.send_message(message.chat.id, steam(), parse_mode='HTML')

@bot.message_handler(commands=['winpoin'])
def command_news(message):
	bot.send_message(message.chat.id, "🆕 Update Artikel WinPoin\n")
	bot.send_message(message.chat.id, winpoin(), parse_mode='HTML')


print('Bot Aktif')
while True:
    try:
        bot.infinity_polling(True)
    except Exception:
        tm.sleep(1)