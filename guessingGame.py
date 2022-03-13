

count=0
while (count<5):
    guess = int(input("Guess a number (between 1 and 9)"))
    if (guess>5):
        print("Your guess is too high")
    elif (guess == 5):
        print("You won!!!")
        break
    else:
        print("Your guess is too low")
    count= count+1




  