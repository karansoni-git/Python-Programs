import random

def score():        
    number = random.randint(1,100)
    print(f"Score : {number}")

    with open("score.txt","r") as f:
        score = int(f.read())

    if(number > score):
        with open("score.txt","w") as f:
            f.write(str(number))
        print("High score will be updated to your next game...")
    print(f"High Score : {score}")  

score()