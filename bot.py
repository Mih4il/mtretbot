import telebot
import config
import random
import numpy

e = 0

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])

def lalala(message):
    t = message.text
    arr = []
    arr.append(message.text)
    if t == "/say":
        array = ["Я крутой", "Сбежал из дурки", "Я - патриот Российской Федерации", "Ставь лайк чтобы жалко", "Что все пристали к этому Путену???",
                 "Моргенштерн - козел"]
        bot.send_message(message.chat.id, random.choice(array))
    elif "морген" in t.lower() and "дурк" in t.lower():
        bot.send_message(message.chat.id, "Спорный вопрос, но могу сказать одно")
        bot.send_message(message.chat.id, "Моргештерн - дурачок!!")
    elif "дурк" in t.lower():
        array = ["Зачем говорить про дурку?", "Дурка - как раз твое место!", "Путин - класс, и это не обсуждается", "Я крутой, а ты из дурки!",
                 "Мне тебя жалко, раз у тебя на устах лишь психиатрическая больница"]
        textOfArray = random.choice(array)
        a = random.choice([0, 1, 2, 3, 4, 5])
        if textOfArray == "Мне тебя жалко, раз у тебя на устах лишь психиатрическая больница":
            if a == 1:
                textOfArray += " номер 4"
            elif a == 2:
                textOfArray += " номер 13"
            elif a == 3:
                textOfArray += " номер 65"
            elif a == 4:
                textOfArray += " номер 1411"
            elif a == 5:
                textOfArray += " номер 534"
        bot.send_message(message.chat.id, textOfArray)

    elif "морген" in t.lower():
        bot.send_message(message.chat.id, "Моргештерн - дебил")
        bot.send_message(message.chat.id, "Он реально тупой")
        bot.send_message(message.chat.id, "дурачок")
    elif t == "/talk":
        e += 1
        if e > 3:
            r = random.choice(arr)
            while True:
                a = random.choice([0, 1])
                if a == 0: break
                r += " " + random.choice
            bot.send_message(message.chat.id, r)
        else:
            r = "Их всего ", e
            bot.send_message(message.chat.id, "Недостаточно сообщений для воспроизведения")
            bot.send_message(message.chat.id, r)
    else:
        array2 = ["Не понял вас", "Вот скажите мне, зачем вы мне это написали?", "Не понимаю вас вообще", "Что вы несете, простите?",
                 "Не понимаю вас. Что ж, я еще развиваюсь", "Не нравится мне такой ваш акцент", message.text]
        bot.send_message(message.chat.id, random.choice(array2))

bot.polling(none_stop=True)
