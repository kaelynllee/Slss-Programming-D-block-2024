# Emoji Replacer
# Author: Kaelyn
# 26 February 2024

def translate(usr_input):
    return usr_input.replace("100", "1️💯").replace("noodles", "🍜")


def main():
  
    usr_input = input()

    print(translate(usr_input))



print(translate("Get to 💯!"))
print(translate("I like 🍜."))
print(translate("I have 100 noodles."))
main()
