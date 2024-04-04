# Emoji Replacer
# Author: Kaelyn
# 26 February 2024


def translate(usr_input):
    return usr_input.replace("1", "1️⃣").replace("bubble tea", "🧋")


def main():
    usr_input = input()
    print(translate(usr_input))


print(translate("I'm number 1 !"))
print(translate("I love bubble tea."))
print(translate("I have 1 bubble tea."))
main()
