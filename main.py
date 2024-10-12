import telebot
from telebot import types
import random
from PIL import Image, ImageDraw

bot = telebot.TeleBot('7938079698:AAE17WRYRm225j4aqervuq3WnYUNDe7DBDE')

messages = [
    "Hello\nBy investing 💵 in our company and giving us your money\nYou can benefit many times over\n\nMoney 💰 You double, you can trust us and invest in our company 🙏",
    
    "Hi again\nYou can send your BTC to this address:\n\nbc1q22chwe46n897jqyecjuqmuu37yfd4akrhe6k9e\n\nBecause ×2\n1 day × 2\n2 day × 4\n\nSend your amount and tomorrow check your wallet😉\n\nAll payments are auto✅",
    
    "Normal investment plans available\n\nInvest $100 and earn $1000\nInvest $200 and earn $2000\nInvest $300 and earn $3000\nInvest $400 and earn $4000\nInvest $500 and earn $5000\nInvest $600 and earn $6000\nInvest $700 and earn $7000\nInvest $800 and earn $8000\nInvest $900 and earn $9000\nInvest $1000 and earn $10000\n\n✔️✔️✔️ profits are received in 24hrs\n\nVIP plans available:\n\nInvest $1000 and earn $7500\nInvest $2000 and earn $15000\nInvest $3000 and earn $22500\nInvest $4000 and earn $30000\nInvest $5000 and earn $37500\nInvest $10000 and earn $75000\n\n✔️✔️✔️ profits are received in 12 hours.\n\n👇👇\n@rernmbot\n@bskllll\n@BNB_free_100",
    "Sja4e2chwe46n897jqyecjuqmuu37yfd4akrhe6k9e" ,
    
    "Multiply your bnb with us❤️👌\nWe have the best programs for you, just buy from us once✅\nPlease send your BNB to the following wallet:\n\nb64672chwe46n897jqyecjuqmuu37yfd4akrhe6k9e"
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.chat.id
    markup = types.InlineKeyboardMarkup()

    # Adding buttons with emojis
    invest_button = types.InlineKeyboardButton("💸 Invest Now", callback_data='invest')
    group_button = types.InlineKeyboardButton("🔗 Group Link", url='https://t.me/grgrrrg')
    share_button = types.InlineKeyboardButton("📤 Share Bot", switch_inline_query='')
    results_button = types.InlineKeyboardButton("📊 Trading Results", callback_data='results')

    # Adding buttons in a row
    markup.add(invest_button, group_button, share_button, results_button)

    # Sending the image with the message
    with open('sense.png', 'rb') as photo:
        bot.send_photo(user_id, photo, caption="""
*🚀 Grow your investment today! 💰*
*Invest $300 and earn $3000 in a day! ⏰*

🔗 Wallet Address:
*Sja4e2chwe46n897jqyecjuqmuu37yfd4akrhe6k9e*

*💬 Contact us for more info!*
*@rernmbot | @bskllll | @BNB_free_100*
""", parse_mode='Markdown', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = call.message.chat.id
    
    if call.data == 'invest':
        for msg in messages:
            bot.send_message(user_id, msg)

    elif call.data == 'results':
        # Create a dummy chart image
        width, height = 400, 300
        image = Image.new('RGB', (width, height), 'black')
        draw = ImageDraw.Draw(image)

        # Setting points for the chart
        points = []
        for day in range(1, 11):
            value = random.randint(50, 200)  # Random data
            points.append((day * 40, height - value))
            if day > 1:
                draw.line((points[day - 2], points[day - 1]), fill='blue', width=2)

            # Adding labels with profits
            draw.text((day * 40 - 10, height - value - 15), f"${value}", fill='white')

        # Adding titles
        draw.text((10, 10), "Investment Growth", fill='white')
        draw.text((width - 50, 10), "Value ($)", fill='white')
        draw.text((10, height - 20), "Days", fill='white')

        # Saving the image
        image.save('trading_results.png')

        # Sending the image
        with open('trading_results.png', 'rb') as img:
            bot.send_photo(user_id, img)

# Run the bot
if __name__ == "__main__":
    bot.polling(none_stop=True)
