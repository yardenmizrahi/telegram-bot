import os
import telebot

API_KEY = '5358422135:AAHC3xFp6kcTiWV354lSvt6ps6qdytB7A7c'
#API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['sunday'])
def sunday(message):
    send = "computer communication 9-11: " + "https://moodle.afeka.ac.il/mod/url/view.php?id=63418‏"
    send = send + "\nmodels 14-16: https://teams.microsoft.com/l/meetup-join/19%3ap9cZ1fgxHpr5gmPO3H_y5r1Mnx4xsmUUph-mbyDBxI81%40thread.tacv2/1644395877676?context=%7b%22Tid%22%3a%2279caa7d1-da42-47a2-b507-432ca23f0704%22%2c%22Oid%22%3a%222de24a28-b8de-47ef-819e-fb5e60296da8%22%7d‏"
    bot.send_message(message.chat.id, send)

@bot.message_handler(commands=['monday'])
def monday(message):
    send = "programming language 10-13: https://us02web.zoom.us/j/81506322767?pwd=a0d6SE5NczZsMVhldVVBZ0hvcXM0QT09"
    send += "\ndesign and analyze algorithms 15-17:  https://us02web.zoom.us/j/82795556762"
    bot.send_message(message.chat.id, send)

@bot.message_handler(commands=['tuesday'])
def tuesday(message):
    send = "design and analyze algorithms 8-12:  https://us02web.zoom.us/j/83334828154"
    send += "\nstatistic's lecturer 13-15: https://us02web.zoom.us/j/86032188256?pwd=V01sUVRxRUZxRHc0RStPVlVMZmRoZz09"
    send += "\nstatistic's practice 15-17: https://us02web.zoom.us/j/83001421470‏"
    bot.send_message(message.chat.id, send)

@bot.message_handler(commands=['thursday'])
def thursday(message):
    send = "models 12-15: <https://teams.microsoft.com/meetingOptions/?organizerId=2de24a28-b8de-47ef-819e-fb5e60296da8&tenantId=79caa7d1-da42-47a2-b507-432ca23f0704&threadId=19_p9cZ1fgxHpr5gmPO3H_y5r1Mnx4xsmUUph-mbyDBxI81@thread.tacv2&messageId=1644395877676&language=he-IL>"
    send += "\nrequirements engineering 15-19: https://us02web.zoom.us/j/85146180642"
    bot.send_message(message.chat.id, send)

bot.polling()