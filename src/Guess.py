from random import randint

guess = randint(0, 100)

x = 0

print("Guess The number from 0 to 100")
while True:
    x += 1
    player = int(input("Guess Number : "))
    if(player == guess):
        print("You win, Your Guess this Number in ", x, "time")
        break
    elif(player > guess):
        print("Your guess is bigger then guess ")
    elif(player < guess):
        print("Your guess is smaller then guess ")
    else:
        print("error")