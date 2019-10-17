import random
num = random.randint(1,10)
print ("Guess a number between 1 and 10")
guess= input()
guess=int(guess)


if guess==num:
     print("Correct!")
elif guess!=num:
     print("Make another guess.")
     guess= input()
     if guess==num:
          print("Correct!")
     elif guess!=num:
         print("Make one final guess.")
         guess= input()
         if guess==num:
             print("Yeah! You're correct!")
         elif guess!=num:
             print("Oh no! Game Over!")



