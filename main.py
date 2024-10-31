import random

lives_human = 50
lives_bot = 50

for attack in range (5):
    print(f"{attack+1} attack")
    action = input("Choose your action: a) attack  b) healing c) VAMPIRE")
    if action == "a":
        kill_bot = random.randint (5,15)
        lives_bot = lives_bot-kill_bot
        print("you attacked bot, his lives are: ", lives_bot)

    elif action == "b":
        lives_human = lives_human+random.randint (5,10)
        print("you successfully healed, your total is: ", lives_human)
    elif action == "c":
        lives_human = lives_human+random.randint(7, 18)
        lives_bot = lives_bot-random.randint(7,18)
        print(f"YOU BIT HIM, his lives are: , {lives_bot}")
        print(f"you healed yourself, your total is: {lives_human}")
    if lives_bot <= 0:
        print("Game over, you won! ")
        break
    #bots move
    kill_human = random.randint (10,30)
    lives_human = lives_human - kill_human
    print("enemy has attacked you! Your total is: ", lives_human)
    if lives_human <= 0:
        print("Game over! you lost to the freaking computer, you are dumb")
        break
if lives_human > 0 and lives_bot > 0:
    if lives_human > lives_bot:
        print("Game over, you won!")
    else:
        print("Game over! you lost to the freaking computer, you are dumb")