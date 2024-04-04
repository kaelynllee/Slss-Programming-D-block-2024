# Emoji Replacer
# Author: Kaelyn
# 26 February 2024


def translate(usr_input):
    return usr_input.replace("1", "1️⃣").replace("bubble tea", "🧋")


def main():
    usr_input = input()
    print(translate(usr_input))


print(translate("Get to 1 !"))
print(translate("I like bubble tea."))
print(translate("I ove 1 bubble tea."))
main()
