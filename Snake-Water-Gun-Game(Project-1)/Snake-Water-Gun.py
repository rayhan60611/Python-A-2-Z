import random

# compValue = random.randint(1, 3)

x=0
def PlayerinputFuncton():
    playerValue=input(f'''Players Turn:
            1.Press "S" For Snake 
            2.Press "W" For Water
            3.Press "G" for Gun
            >>>>>>>>>>>>> ''')
    compValue = random.randint(1, 3)
    return playerValue , compValue

playerValue,compValue = PlayerinputFuncton()
# compValue = random.randint(1, 3)
# set Snake =1 , Water= 2 & gun = 3             
if playerValue == "s" or playerValue == "S":
    playerValue = 1
elif playerValue == "w" or playerValue == "W":
    playerValue = 2
elif playerValue == "g" or playerValue == "G":
    playerValue = 3
else:
    print("Please Give A valid input Between S, W, G")
    PlayerinputFuncton()

def game(c,p):
    if c == p: 
        if c==1:
            print(f'''              
                    Player Choose: Snake@
                    Computer Choose: Snake@
                    Result Is a Tie !!!''')
        elif c==2:
            print(f'''  
                    Player Choose: Water!
                    Computer Choose: Water!
                    Result Is a Tie !!!''')
        else:
            print(f'''  
                    Player Choose: Gun->
                    Computer Choose: Gun->
                    Result Is a Tie !!!''')

    elif c == 1 and p == 2:
        print(f'''  
                    Player Choose: Water!
                    Computer Choose: Snake@
                    Computer Win !!!''')
    elif c == 1 and p == 3:
        print(f'''  
                    Player Choose: Gun->
                    Computer Choose: Snake@
                    Player Win !!!''')
    elif c == 2 and p == 1:
        print(f'''  
                    Player Choose: Snake@
                    Computer Choose: Water!
                    Player Win !!!''')
    elif c == 2 and p == 3:
        print(f'''  
                    Player Choose: Gun->
                    Computer Choose: Water!
                    Computer Win !!!''')
    elif c == 3 and p == 1:
        print(f'''     
                    Player Choose: Snake@
                    Computer Choose: Gun->
                    Computer Win !!!''')
    elif c == 3 and p == 2:
        print(f'''  
                    Player Choose: Water!
                    Computer Choose: Gun->
                    Player Win !!!''')
    else:
        print("Please Give A valid input Between S, W, G")
        PlayerinputFuncton()


game(compValue,playerValue)