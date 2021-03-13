import random
random_generated=random.randint(7,100)
#guess the number
guesses=0
score=10
while guesses<8:
    guess_=int(input(f"guess {guesses}: "))
    if guess_<random_generated:
        print("guess higher")
        score-=1
    elif guess_>random_generated:
        print("guess lower")
        score-=1
    if guess_==random_generated:
        print("you are correct,the number is indeed",random_generated)
        score+=1
        break
    guesses+=1
if guess_!=random_generated:
    print(f"the number was,{random_generated}")
print("your score is", score)






