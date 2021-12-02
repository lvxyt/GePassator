# import's
import random
import string
from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()
print(Fore.BLACK)
print(Back.CYAN + "GePassator by Kini-Noro")
# Скрипт генератор паролей GePassator + параметры запуска
print(Fore.RESET)
name = int( input(Back.RESET + 'Set the length:'))
print()
print(Back.GREEN + 'Generation methods:')
print()
print('1. A random alphabetic string with a lowercase combination.')
print('2. Using secrets.choice.(Letters and numbers)')
print()
choicemod = str( input(Back.RED + 'Choose a generation method:')) # Generation methods
print(Fore.CYAN)
# A random alphabetic string with a lowercase combination.
if choicemod == "1":
    def generate_random_string(length):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        print(Back.RESET + "Random string of length", name, "is:", rand_string)
    generate_random_string(name)
# Using secrets.choice.(Letters and numbers)
elif choicemod == "2":
    def generate_alphanum_random_string(length):
        letters_and_digits = string.ascii_letters + string.digits
        rand_string = ''.join(random.sample(letters_and_digits, length))
        print(Back.RESET + "Cryptic Random string of length", name, "is:", rand_string)
    generate_alphanum_random_string(name)
# Else variant
else:
    print('!You chose the wrong option!')
print()
input()
