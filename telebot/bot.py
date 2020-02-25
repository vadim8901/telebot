import telebot
from telebot import types
import urllib.request

TOKEN = '922248965:AAFF0YCps5TxnG8A6IRn9WkywTizg4R6slY'
bot = telebot.TeleBot(TOKEN)
#                python C:\telebot\bot.py

@bot.message_handler(commands=['start', 'go'])
def start(message):
	sti = open('C:/telebot/static/welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)
	bot.send_message(message.chat.id, 'Привет, {0.first_name}!\n Я <b>{1.first_name}</b>🤖, создан для упрощения твоего обучения, тут будут подсказки, дз, и со временем добавится чатик, где вы сможете задавать вопросы и скидывать код своего дз!:)\nВоспользуйся коммандой /help, чтобы узнать о всех существующих коммандах бота'.format(message.from_user, bot.get_me()), parse_mode='html')

@bot.message_handler(commands=['info'])
def info(message):
	markup = types.InlineKeyboardMarkup()
	button0 = types.InlineKeyboardButton(text='ДЗ', callback_data='num0')
	button1 = types.InlineKeyboardButton(text='Создание проекта в Visual Studio', callback_data='num1')
	button2 = types.InlineKeyboardButton(text='Типы данных С++', callback_data='num2')
	button3 = types.InlineKeyboardButton(text='Конструкция ветвления', callback_data='num3')
	button4 = types.InlineKeyboardButton(text='Конструкция switch — case', callback_data='num4')
	markup.add(button0, button1, button2,button3, button4)
	bot.send_message(message.chat.id, 'Выберите что вам нужно:', reply_markup = markup)

@bot.message_handler(commands=['help', 'helper'])
def help(message):
	bot.send_message(message.chat.id, 'Комманды которые пока доступны:\n1) /go & /start - начало работы бота.\n2) /info - информация.')

@bot.message_handler(content_types=['text'])
def Notext(message):
	text = message.text.lower()
	if text == 'привет':
		bot.send_message(message.chat.id, 'Привет, рад видеть тебя!)')
	else:
		bot.send_message(message.chat.id, 'Не знаю что ответить :(\nПопробуй /help')

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
	chat_id = c.message.chat.id
	img = open('C:/telebot/static/oneex.png', 'rb')
	img1 = open('C:/telebot/static/two.png', 'rb')
	img2 = open('C:/telebot/static/three.png', 'rb')
	img3 = open('C:/telebot/static/four.png', 'rb')
	img4 = open('C:/telebot/static/five.png', 'rb')
	img5 = open('C:/telebot/static/six.png', 'rb')
	img6 = open('C:/telebot/static/seven.png', 'rb')
	if c.data == 'num1':
		bot.send_message(chat_id, '<b>Создание пустого проекта в среде Visual Studio:</b>\nЗапускаем среду программирования.\nПеред нами открывается начальная страница.', parse_mode='html')
		bot.send_photo(chat_id, photo=img)
		bot.send_message(chat_id, 'Теперь нам нужно создать пустой проект.\nвыбираем пункт Создание проекта.\nЛибо, можно использовать "горячие клавиши" Ctrl+Shift+N.')
		bot.send_photo(chat_id, photo=img1)
		bot.send_message(chat_id, 'Затем выбираем тип проекта, после чего называем его и указываем путь:')
		bot.send_photo(chat_id, photo=img2)
		bot.send_message(chat_id, '<b>Готово!</b>', parse_mode='html')
		bot.send_photo(chat_id, photo=img3)
	elif c.data == 'num0':
		bot.send_message(chat_id, 'Заполнить двумерный массив случайными числами от 10 до 100.\nПосчитать сумму элементов отдельно в каждой строке и определить номер строки, в которой эта сумма максимальна.')
	elif c.data == 'num2':
		bot.send_photo(chat_id, photo=img4)
	elif c.data == 'num3':
		bot.send_message(chat_id, '<b>Оператор if</b>\nОператор <b>if</b> служит для того, чтобы выполнить какую-либо операцию в том случае, когда условие является верным.\nУсловная конструкция в С++ всегда записывается в круглых скобках после оператора if.Внутри фигурных скобок указывается тело условия.\nЕсли условие выполнится, то начнется выполнение всех команд, которые находятся между фигурными скобками.', parse_mode='html')
		bot.send_photo(chat_id, photo=img5)
		bot.send_message(chat_id,'Каждому оператору if соответствует только один оператор else. Совокупность этих операторов — else if означает, что если не выполнилось предыдущее условие, то проверить данное. Если ни одно из условий не верно, то выполняется тело оператора else.')
	elif c.data == 'num4':
		bot.send_message(chat_id, 'Очень часто в процессе написания программы требуется писать длинные if-else конструкции, например, когда мы получаем какой-либо ключ от пользователя;\nесли вы пишете игру, то придется проверять на какую кнопку нажал игрок (вправо, влево, пробел и т.д.)\n<b>Конструкция switch-case — это удобная замена длинной if-else конструкции</b>, которая сравнивает переменную с несколькими константными значениями, например int или char.).', parse_mode='html')
		bot.send_photo(chat_id, photo=img6)

bot.polling()
