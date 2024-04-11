# Unit 2 activity
# Author: Kaelyn 
# 9 April 2024

def say_hello_params(name):
    print(f"Hello {name}!")

say_hello_params('Bobita')

def translate(usr_input):
    return usr_input.replace("You slay", "🫵😍🫵")

def main():
    usr_input = input()
    print(translate(usr_input))

print(translate("You slay"))
main()

user_answer = input ("Can you hang after school?")

while user_answer not in ["yes", "no", "yeah", "nah", "yus","naur"]:
    user_answer = input ("Do you want to go out to eat?")

if user_answer in ["yes", "yeah","yus"]:
    print("WOOO let's go get some food!")

if user_answer in  ["no", "nah","not with you", "naur"]:
    print ("You never have time.")