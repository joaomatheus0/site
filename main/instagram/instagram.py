from instabot import Bot

class Login():
    
    def validation_login(username, password):
        bot = Bot()
        try:
            bot.login(username = username, password = password)
            bot.logout()
            return True
        except:
            return False

    def send_image(username, password):
        bot = Bot()
        bot.login(username = username, password = password)