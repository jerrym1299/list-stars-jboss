import requests
import telebot
import time

url = 'https://api.github.com/orgs/JBossOutreach/repos'

json_data = requests.get(url).json()

numoflists = len(json_data)
stars = 0

#finding the overall number of stars
for i in range(numoflists):
    stars += json_data[i]['stargazers_count']

#Each of the repositories number of stars
blogstars = json_data[0]['stargazers_count']
archivestars = json_data[1]['stargazers_count']
leadmgmtandroidstars = json_data[2]['stargazers_count']
leadmgmtserverstars = json_data[3]['stargazers_count']
contactgroupsandroidstars = json_data[4]['stargazers_count']
contactgroupsserverstars = json_data[5]['stargazers_count']
homestars = json_data[6]['stargazers_count']
ideastars = json_data[7]['stargazers_count']
certificategeneratorserverstars = json_data[8]['stargazers_count']
visitingcardstars = json_data[9]['stargazers_count']
certificategeneratorfrontstars = json_data[10]['stargazers_count']
leadmgmtfrontstars = json_data[11]['stargazers_count']
codeinmentorsplygrdstars = json_data[12]['stargazers_count']
gciwebsitestars = json_data[13]['stargazers_count']
mentorshandbookstars = json_data[14]['stargazers_count']
visitingcardandroidstars = json_data[15]['stargazers_count']
visitingcardbackendstars = json_data[16]['stargazers_count']
jbosslogostars = json_data[17]['stargazers_count']

bot_token = '566958721:AAEVVrN8R5f0DfDW_pdxsekdpqo3C1Vs4ao'
bigmessage = ("Blog stars: " + str(blogstars) + "\n" + "Archive stars: " + str(archivestars) + "\n"  + "Lead management android stars: " +  str(leadmgmtandroidstars) + "\n" + "Lead management server stars: " + str(leadmgmtserverstars) + "\n" + "Contact group android stars: " + str(contactgroupsandroidstars) + "\n" + "Contact group server stars: " + str(contactgroupsserverstars) + "\n"  + "Home stars: " + str(homestars) + "\n" + "Idea news: " + str(ideastars) + "\n"
+ "Certificate generator server stars: " + str(certificategeneratorserverstars) + "\n" + "Visting card stars: " + str(visitingcardstars) + "\n" + "Certificate generator front stars: " + str(certificategeneratorfrontstars) + "\n"
+ "Lead management front stars: " + str(leadmgmtfrontstars) + "\n" + "Code in mentors playground stars: " + str(codeinmentorsplygrdstars) + "\n" + "Gci website stars: " + str(gciwebsitestars) + "\n"
+ "Mentors hand book stars: " + str(mentorshandbookstars) + "\n" + "Visiting card android stars: " + str(visitingcardandroidstars) + "\n" + "Visiting card back end stars: " + str(visitingcardbackendstars) + "\n"
+ "Jboss logo stars: " + str(jbosslogostars))
bot = telebot.TeleBot(token = bot_token)

@bot.message_handler(commands=['addallstars'])
def send_stars(message):
    bot.reply_to(message,stars)

@bot.message_handler(commands=['listallstars'])
def send_stars(message):
    bot.reply_to(message, bigmessage)
    print("done")
@bot.message_handler(commands=['blog'])
def send_stars(message):
    bot.reply_to(message, blogstars )
@bot.message_handler(commands=['Archive'])
def send_stars(message):
    bot.reply_to(message, archivestars)
@bot.message_handler(commands=['leadmgmtandroidstars'])
def send_stars(message):
    bot.reply_to(message, leadmgmtandroidstars)
@bot.message_handler(commands=['leadmgmtserverstars'])
def send_stars(message):
    bot.reply_to(message, leadmgmtserverstars)
@bot.message_handler(commands=['contactgroupsandroidstars'])
def send_stars(message):
    bot.reply_to(message, contactgroupsandroidstars )
@bot.message_handler(commands=['contactgroupsserverstars'])
def send_stars(message):
    bot.reply_to(message, contactgroupsserverstars)
@bot.message_handler(commands=['homestars'])
def send_stars(message):
    bot.reply_to(message, homestars )
@bot.message_handler(commands=['ideastars'])
def send_stars(message):
    bot.reply_to(message, ideastars )
@bot.message_handler(commands=['certificategeneratorserverstars'])
def send_stars(message):
    bot.reply_to(message, certificategeneratorserverstars )
@bot.message_handler(commands=['visitingcardstars'])
def send_stars(message):
    bot.reply_to(message, visitingcardstars)
@bot.message_handler(commands=['certificategeneratorfrontstars'])
def send_stars(message):
    bot.reply_to(message, certificategeneratorfrontstars)
@bot.message_handler(commands=['leadmgmtfrontstars'])
def send_stars(message):
    bot.reply_to(message, leadmgmtfrontstars)
@bot.message_handler(commands=['codeinmentorsplygrdstars'])
def send_stars(message):
    bot.reply_to(message, codeinmentorsplygrdstars)
@bot.message_handler(commands=['gciwebsitestars'])
def send_stars(message):
    bot.reply_to(message, gciwebsitestars)
@bot.message_handler(commands=['mentorshandbookstars'])
def send_stars(message):
    bot.reply_to(message, mentorshandbookstars)
@bot.message_handler(commands=['visitingcardandroidstars'])
def send_stars(message):
    bot.reply_to(message, visitingcardandroidstars)
@bot.message_handler(commands=['visitingcardbackendstars'])
def send_stars(message):
    bot.reply_to(message, visitingcardbackendstars)
@bot.message_handler(commands=['jbosslogostars'])
def send_stars(message):
    bot.reply_to(message, jbosslogostars)
@bot.message_handler(commands=['help'])
def send_stars(message):
    bot.reply_to(message, "/help" + "\n" + "/listallstars" + "\n" + "/addallstars" + "\n" + "/blogstars" + "\n" + "/Archive" + "\n" + "/leadmgmtandroidstars" + "\n" + "/leadmgmtserverstars" + "\n" + "/contactgroupsandroidstars" + "\n" + "/contactgroupsserverstars" + "\n" "/homestars" + "\n" + "/ideastars" + "\n" "/certificategeneratorserverstars" + "\n" + "/visitingcardstars" + "\n" + "/certificategeneratorfrontstars" + "\n" + "/leadmgmtfrontstars" + "\n" + "/codeinmentorsplygrdstars" + "\n" + "/gciwebsitestars" + "\n" + "/mentorshandbookstars" + "\n" + "/visitingcardandroidstars" + "\n" + "/visitingcardbackendstars" + "\n" + "/jbosslogostars")
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
