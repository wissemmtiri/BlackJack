# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 22:08:44 2022

@author: Wissem
"""

import art 
import os
import random 

def money_to_coins(money,coins):
    coins[0] = money // 50
    money = money - coins[0]*50
    coins[1] = money // 20
    money = money - coins[1]*20
    coins[2] = money // 10
    money = money - coins[2]*10
    
def betting(coins):
    sum_tot = 0
    sum_tot = 50*coins[0] + 20*coins[1] + 10*coins[2]
    while(True):
        print(coins)
        print("PLACE A BET : ")
        bet_in_50 = int(input("50 ==> "))
        bet_in_20 = int(input("20 ==> "))
        bet_in_10 = int(input("10 ==> "))
        sum_n = bet_in_50*50 + bet_in_20*20 + bet_in_10*10
        if sum_n <= sum_tot :
            break
        
    coins[0] -= bet_in_50
    coins[1] -= bet_in_20
    coins[2] -= bet_in_10
    return(bet_in_50,bet_in_20,bet_in_10)    

def win(coins,bet_50,bet_20,bet_10):
    coins[0] += 2*bet_50
    coins[1] += 2*bet_20
    coins[2] += 2*bet_10

def draw(coins,bet_50,bet_20,bet_10):
    coins[0] += bet_50
    coins[1] += bet_20
    coins[2] += bet_10

def test_fin(coins):
    return(coins[0]==0)&(coins[1]==0)&(coins[2]==0)

def play(money) :
    coins = [0,0,0]
    money_to_coins(money,coins)
    print("You have ",coins[0]," peices of 50")
    print("         ",coins[1]," peices of 20")
    print("         ",coins[2]," peices of 10")
    end_of_game = False
    while(not end_of_game):
        bet_50,bet_20,bet_10  = betting(coins)
        input("S T A R T")
        card_1 = random.randint(0, 11)
        while(True):
            card_2 = random.randint(0, 11)
            if card_1 != card_2 :
                break
        
        player_sum = 0
        if card_1 >= 9:
            player_sum += 10
        else: 
            player_sum += card_1+1
        if card_2 >= 9:
            player_sum += 10
        else: 
            player_sum += card_2+1
        
        dealer_card_1 = random.randint(0, 11)
        dealer_card_2 = random.randint(0, 11)
        
        dealer_sum = 0
        if dealer_card_1 >= 9:
            dealer_sum += 10
        else: 
            dealer_sum += dealer_card_1+1
        if dealer_card_2 >= 9:
            dealer_sum += 10
        else: 
            dealer_sum += dealer_card_2+1
        
        print("Your Cards : ")
        print(art.CARDS[card_1],art.CARDS[card_2])
        print("Dealer's Cards : ")
        print(art.CARDS[dealer_card_1],art.BLANKCARD)
        print("[1] : HIT")
        print("[2] : STAND")
        while(True):
            choice = input("==>")
            if choice in ["1","2"]:
                break
        if choice == "1":
            card_3 = random.randint(0, 11)
            print("Your Cards : ")
            print(art.CARDS[card_1],art.CARDS[card_2],art.CARDS[card_3])
            print("Dealer's Cards : ")
            print(art.CARDS[dealer_card_1],art.CARDS[dealer_card_2])
            if card_3 >= 9:
                player_sum += 10
            else: 
                player_sum += card_3+1 
        else : 
            print("Your Cards : ")
            print(art.CARDS[card_1],art.CARDS[card_2])
            print("Dealer's Cards : ")
            print(art.CARDS[dealer_card_1],art.CARDS[dealer_card_2])
        if(player_sum > 21):
            print("You Lost !")
            print("You have ",coins[0]," peices of 50")
            print("         ",coins[1]," peices of 20")
            print("         ",coins[2]," peices of 10")
        else :
            
            if player_sum > dealer_sum : 
                print("YOU WON !")
                win(coins,bet_50,bet_20,bet_10)
                print("You have ",coins[0]," peices of 50")
                print("         ",coins[1]," peices of 20")
                print("         ",coins[2]," peices of 10")
            elif player_sum < dealer_sum :
                print("YOU LOST !")
                print("You have ",coins[0]," peices of 50")
                print("         ",coins[1]," peices of 20")
                print("         ",coins[2]," peices of 10")
            else : 
                print("DRAW !")
                draw(coins, bet_50, bet_20, bet_10)
                print("You have ",coins[0]," peices of 50")
                print("         ",coins[1]," peices of 20")
                print("         ",coins[2]," peices of 10")
        if (test_fin(coins)):
            print("Money Gone")
            end_of_game = True
            break
        while(True):
            keep_on_playing = input("CONTINUE ? [Y]|[N] : ")
            if(keep_on_playing == "N"):
                end_of_game = True
                break
            elif(keep_on_playing != "Y"):
                print("INVALID INPUT")
            else:
                break
    sum = coins[0]*50 + coins[1]*20 + coins[2]*10
    print("YOU ENDED UP WITH $",sum)
    input()
    os.system('cls')
    Menu()

def helpp():
    print(''' 
          blackjack, or twenty-one, Card game whose object is to be dealt cards
          having a higher count than those of the dealer, up to but not exceeding 21.
          Aces count as 1, and face cards as 10. Bets are placed before the deal
          
                                                                        ©MTIRI WISSEM
          ''')
    input()
    os.system('cls')
    Menu()

def Menu():
    print(art.logo)
    print("\n                         [1] : P L A Y")
    print("                         [2] : H E L P")
    print("                         [3] : E X I T")
    
    nb = 0
    while(True):
        choice = input("==> ")
        if choice == "1" :
            while(True):
                money = int(input("HOW MUCH MONEY ARE YOU WILLING TO PLAY WITH : $"))
                if(money>50):
                    break
            play(money)
            break
        elif choice == "2":
            helpp()
            break
        elif choice == "3":
            exit(1)
        else : 
            nb += 1
            print("INPUT ALLOWED : '1' , '2' , '3'")
            if nb == 3 :
                os.system('cls')
                print("LIMIT REACHED ! Quitting..")
                exit(1)
                input()
    
Menu()
