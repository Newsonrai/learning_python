import random
random_number=random.randint(1,10)
life=10

for n in range(life):
    Guessed_Random_Number=int(input("Guess the random number between 1 to 10 :--"))

    if random_number==Guessed_Random_Number:
        print("Congratulations! You guessed the number!")
        break
    else:
        print("Sorry wrong guess,Try again.")