import random
comp_num = random.randint(1,101)
chance = 10
while(chance):
    user_num = int(input("Enter number between 1 and 100: "))
    if user_num== comp_num:
        print("Hurrah!, you guessed it correct.")
        break;
    elif(user_num>comp_num):
        print("Oops! you guessed higher number please choose smaller number.")
        chance= chance-1
        print("Now, your remaining chances are: ",chance)

    else:
        print("Oops! you guessed lower number please choose higher number.")
        chance = chance - 1
        print("Now, your remaining chances are: ", chance)

else:
    print("Game over!")

