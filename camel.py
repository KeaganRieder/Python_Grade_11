#Camel
from random import randint

done = False
miles = 0
thirst = 0
camel_tiredness = 0
natives_distance = -20
drinks_in_canteen = 3
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")


while done is False:
    oasis = randint(1,20)
    distance_away = miles - natives_distance
    miles_away = miles - 15
    
    print("\nA. Drink from your canteen.\n"
          'B. Ahead moderate speed.\n'
          'C. Ahead full speed.\n'
          'D. Stop for the night.\n'
          'E. Status check.\n'
          'Q. Quit.\n')
    
    user_choice = input('what is your choice \n > ')

    if user_choice.upper() == 'Q':
        done = True
        
    elif user_choice.upper() == 'A':
        if drinks_in_canteen > 0:
            thirst = 0
            drinks_in_canteen -= 1
            
        else:
            print('sorry but there are no more dirnks left')
        
    elif user_choice.upper() == 'B':
       player_move = randint(5,12)
       print('you have tarveled ',player_move,' miles')
       camel_tiredness += 1
       thirst += 1
       natives_distance += randint(7,14)
       miles += player_move
        
    elif user_choice.upper() == 'C':
       player_move = randint(10,20)
       print('you have tarveled ',player_move,' miles')
       camel_tiredness += randint(1,3)
       thirst += 1
       natives_distance += randint(7,14)
       miles += player_move
    
    elif user_choice.upper() == 'D':    
        print('your camel is happy')
        camel_tiredness = 0
        natives_distance += randint(7,14) 
    
    elif user_choice.upper() == 'E':
        print('miles traveled: ',str(miles),
              '\nDrinks in canteen: ',str(drinks_in_canteen),
              '\nThe natives are ', str(distance_away),'  miles behind you.\n')

    #telling the palyer if they have lost or won, and if they need to do certain things like sleep or drink
    if thirst >= 4 and thirst <6:
        print('you are thirsty')
        
    elif thirst == 6:
        print('you have die of thirst')
        done = True
        
    elif camel_tiredness >= 5 and camel_tiredness <8:
        print('your camel is tired')
        
    elif camel_tiredness >= 8:
        print ('your camel has died')
        done = True
        
    elif natives_distance == miles:
        print('the natives have caught up')
        done = True
        
    elif distance_away == miles_away:
        print ('the natives are close')
        
    elif miles >= 200:
        print('you win')
        done = True
        
    elif oasis == 1:
        print('you have found an oasis')
        thirst = 0
        camel_tiredness = 0
        drinks_in_canteen = 3 
    
