import random


class Bot:
    def greeting_response(self, user_input):
        user_input = user_input.lower()

        #User greetings
        USER_GREETINGS = ('hi', 'hello', 'wassup', 'whatsup', 'wossop', 'good morning', 'good afternoon', 'good evening')

        #bot greeeting
        BOT_GREETING = ['Hi', 'Hello there!', 'Hi there!', 'Nice to meet you']

        for word in user_input.split():
            if word in USER_GREETINGS:
                return random.choice(BOT_GREETING)


