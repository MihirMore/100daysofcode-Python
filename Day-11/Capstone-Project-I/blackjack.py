import os
from art import logo
import random


def blackjack():
    user_play = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_play == 'y':
        _ = os.system('cls')        
        print(logo)
        user_cards = []
        computer_cards = []
        should_continue = True
        count = 0
        while should_continue:            
            def deal_card():
                cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
                card_number = random.choice(cards)
                return card_number

            def calculate_score(card_list):
                score = sum(card_list)
                if len(card_list) == 2:
                    if (11 in card_list and 10 in card_list):
                        return 0
                    else:
                        return score
                else:
                    if score > 21 and (11 in card_list):
                        card_list.remove(11)
                        card_list.append(1)
                        score = sum(card_list)
                        return score
                    elif score > 21:
                        return score
                    else:
                        return score
            if count == 0:                
                for _ in range(0, 2):                    
                    user_card = deal_card()
                    user_cards.append(user_card)

                for _ in range(0, 2):
                    dealer_card = deal_card()
                    computer_cards.append(dealer_card)
            else:
                user_card = deal_card()
                user_cards.append(user_card) 
                dealer_card = deal_card()
                computer_cards.append(dealer_card)
            count += 1
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            while (computer_score < 17):
                dealer_card = deal_card()
                computer_cards.append(dealer_card)

            print(f"Your cards: {user_cards}, Current score: {user_score}.")
            print(f"Computer's first card: {computer_cards[0]}")

            if (user_score == 0):
                print("BlackJack! You win.😃 ")
                print(f"Computer's draw: {computer_cards}")
            elif (computer_score == 0): 
                print ("BlackJack! You lose.😤")
                print(f"Computer's draw: {computer_cards}")
            if (user_score > 21 or computer_score > 21):
                should_continue = False
            else:
                continue_playing = input("Type 'y' to get another card, type 'n' to pass: ")
                if continue_playing == 'n':
                    should_continue = False

        def compare(first_score, second_score):
            if first_score > 21:
                return 3
            elif second_score > 21:  
                return 1
            elif first_score == second_score:
                return 0
            elif first_score > second_score:
                return 1
            else:
                return 2               

        print(f"Your final hand: {user_cards} final score: {user_score}")
        print(
            f"Computer's final hand: {computer_cards}, final score: {computer_score}")

        winner = compare(user_score, computer_score)
        if winner == 0:
            print("It's a draw 😐")
        elif winner == 1:
            print("You win!😃")  
        elif winner == 3:
            print("You went over. You lose.😤")          
        else:
            print("You lose.😤")
        blackjack()

blackjack()            
