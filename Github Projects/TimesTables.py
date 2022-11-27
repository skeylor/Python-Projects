import random
from random import randint

table = []
for num in range(2,12):
    table.append(num)

print(table)
print('Are you ready to test your math skills?')
print("Type 'e' if you want to quit")
print("Type 's' to skip a question")



while True:
    i = randint(2,12)
    num = random.choice(table)
    print ("What's", num, "x", i, "?\n")
    guess = input('Enter your answer here: ')
    if guess == 'e':
        break
    if guess == 's':
        print('skipping')
        continue
    ans = num * i
    if int(guess) == ans:
        print('correct!')
    else:
        print("No, it's", ans)
print('finished')
