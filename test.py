import teleBot

def handle_message(message):
    if message.text == "/start":
        return "Halo, apa yang bisa saya bantu?"
    elif message.text == "/info":
        return "Ini adalah chatbot sederhana yang dibuat dengan Python."
    else:
        return "Maaf, saya tidak mengerti."

def run_chatbot():
    bot = telebot.TeleBot(TOKEN)
    while True:
        message = bot.get_message()
        response = handle_message(message)
        bot.send_message(message.chat.id, response)

if __name__ == "__main__":
    run_chatbot()
