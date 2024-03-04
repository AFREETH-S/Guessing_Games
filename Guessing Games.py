import time
import random

def ytig():
    print("====================================================================")
    print("\n")
    print("       You Think I Guess        ")
    time.sleep(2)
    print("\n\n Between 1 to 100 I think a number and you can guess  ")
    print("\n\n Start guessing ")
    rand = random.randint(1, 100)
    guess = -1
    clue_given = False
    
    while rand != int(guess):
        guess = input("\n What is your guess: ")
        
        if guess == "clue" and not clue_given:
            clue_given = True
            if rand % 2 == 0:
                print("It's an even number")
            else:
                print("It's an odd number")
        elif int(guess) == rand:
            break
        elif int(guess) in range(rand - 5, rand + 6):
            print("So close, try again")
        elif int(guess) in range(rand - 10, rand + 11):
            print("Close, keep guessing")
        elif int(guess) in range(rand - 2, rand + 3):
            print("Very close, almost there")

        else:
            print("Nope, keep guessing")
    print("You got it! That's the number I thought")
    print("====================================================================")    
    choice()
    
def ityg():
    print("====================================================================")
    print("\n")
    print("       I Think You Guess        ")
    time.sleep(2)
    print("\n\n Think the number between 1 to 100")
    time.sleep(2)
    
    flag=1
    mi=0
    ma=101
    d=0
    mid=int((mi+ma)/2)
    
    while(flag):
        print("\n Is your number greater than {}: y/n ".format(mid))
        res=input()
        
        if(not res):
            flag=0
            d=1
            break
        elif(res.lower() == "y" and mi+2 != ma):
            if(mi+2 == ma or mid == mi):
                mid=mi+1
                flag=0
            else:
                mi=mid
                mid=int((mi+ma)/2)
        else:
            ma=mid
            mid=int((mi+ma)/2)
            
    if(d):
        print("please try again")
    else:
        print("Your number is {} ".format(mid))
    print("====================================================================")
    choice()

def main():
    print("====================================================================")
    print("Welcome everyone this is the Guessing Game, Here we have 'You Think I Guess ' and \
    'I think You Guess '")
    time.sleep(2)
    print("\n press 1 for You Think I Guess ")
    time.sleep(1)
    print("\n press 2 for I think You Guess ")  
    time.sleep(1)
    print("\n press 3 for exit")
    time.sleep(1)
    choice()

def choice():
    cho=-1
    
    while(cho!=3):
        cho=int(input("\n Say your Choice: "))
        if(cho==1):
            ytig()
        elif(cho==2):
            ityg()
        else:
            print("Please Enter a Valid selection ")
    if(cho == 3):
        print("Bye bYE")
        time.sleep(2)
        exit()
    

main()

