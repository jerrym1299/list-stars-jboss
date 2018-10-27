import requests
import telebot
import time

url = 'https://api.github.com/orgs/JBossOutreach/repos'

json_data = requests.get(url).json()

numoflists = len(json_data)
stars = 0

for i in range(numoflists):
    stars += json_data[i]['stargazers_count']


bot_token = '566958721:AAEVVrN8R5f0DfDW_pdxsekdpqo3C1Vs4ao'

bot = telebot.TeleBot(token = bot_token)

@bot.message_handler(commands=['liststars'])

def send_stars(message):
    bot.reply_to(message,stars)

bot.polling()
print(stars)
