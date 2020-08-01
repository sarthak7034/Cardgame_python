from typing import List
import random


def Card_pack() -> int:
    Card_Num = random.randint(1, 100)
    return Card_Num

def roll_dices()-> int:
     return random.randint(1,6)
     

print("Enter your name : ")
name = str(input())
print("Entered Name : ",name)
status = False

print("Roll dice:")
N = roll_dices()
Card_Num= Card_pack()
print("Your tries : ",N)

No_of_tries = N
while No_of_tries!=0:
        
        print("Guess the Number: ")
        val = int(input())  

        if (val > Card_Num):
             print("Your guess was too high" )
             print('Guesses left : ',No_of_tries-1)
            
        elif (val < Card_Num):
            print("Your guess was too low") 
            print('Guesses left : ',No_of_tries-1)
        else:
            print("Congratulation you have WON !!!")
            status= True
            break
    
        No_of_tries-=1

if(No_of_tries ==0):
    print("You Lost! The number is : ",Card_Num )
if not status:
    n = "LOSS"
else:
    n = "WON"

f=open('statistics.txt', 'a')
f.write(name +" | "+ n + " | "+ str(N) )
f.close()