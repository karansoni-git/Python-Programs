import random
random_number = random.randint(1,100)
print("Guess The Number From 1 To 100")
num = 0 
guess = 0
while(num != random_number):
    num = int(input("Guess The Number : "))
    if(num > random_number):
        print(f"Guess The Number Less Than {num}")
    elif(num < random_number):
        print(f"Guess The Number More Than {num}")
    guess+=1
print(f"You have Guessed The Number {num} In {guess}")