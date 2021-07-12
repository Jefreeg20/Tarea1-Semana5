import telebot

bot = telebot.TeleBot("1886425559:AAFLFZyCxuCwusI9Gzvek1SUiuNv8UnoIzE")

@bot.message_handler(commands=["start" ])
def start (mensaje):
    bot.reply_to(mensaje, "Bienvenido")
    print ("inicio")

@bot.message_handler(commands=["hla1" ])
def hla1 (mensaje):
    bot.reply_to(mensaje, "Hola, un gusto saludarte, ¿cómo estás?")
    print ("hola")

@bot.message_handler(commands=["comoestas2"]) 
def comoestas2 (mensaje):
    bot.reply_to(mensaje, "Estoy muy bien, ¿y tu?")
    print("como estas")
@bot.message_handler(commands=["dedonderes3"]) 
def dedonderes3 (mensaje):
    bot.reply_to(mensaje, "ESTOY UBICADO DENTRO EN LA MENTE HUMANA")
    print("de donde eres")

@bot.message_handler(commands=["cualestuedad4"]) 
def cualestuedad4 (mensaje):
    bot.reply_to(mensaje, "NO TENGO EDAD CADA DIA COMIENZO DE NUEVO")
    print("tu edad perrin")

@bot.message_handler(commands=["cualestusexo5"]) 
def cualestusexo5 (mensaje):
    bot.reply_to(mensaje, "M")
    print("edad")


bot.polling()