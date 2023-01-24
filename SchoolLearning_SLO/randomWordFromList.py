import random
import os
# You put words here and it will randomly display each word
# If you type 'stop', then the program will be stopped
words = [
    'idempotentnost','absorpcija','komutativnost','asociativnost','distributivnost'
]

word = 'start'

while (word != 'stop'):
    word = input()
    os.system('cls')
    print(words[random.randint(1,5) - 1])

