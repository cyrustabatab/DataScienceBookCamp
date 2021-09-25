import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random







def generate_deck():
    
    ranks = list(range(2,12)) + [10] * 3




    return ranks * 4



def simulate():
    np.random.seed(0)
    

    turn = []
    n = 100_000


    for i in range(n):
        deck = generate_deck()
        random.shuffle(deck)
        
        hand = [deck.pop() for _ in range(2)]
        
        if sum(hand) == 22:
            if hand[0] == 11:
                hand[0] = 1
            else:
                hand[1] = 1
         

        
        hand_sum = sum(hand)

        if hand_sum < 16:

            
            while True:
                while hand_sum < 16:
                    card = deck.pop()
                    hand.append(card)
                    hand_sum += card
                


                if hand_sum > 21:
                    try:
                        eleven_index = hand.index(11)
                    except:
                        break
                    else:
                        hand[eleven_index] = 1
                        hand_sum -= 10
                else:
                    break




        turn.append(hand_sum)


    plt.hist(turn,edgecolor='black')
    plt.show()















def plot_histogram(data):


    plt.hist(data,edgecolor='black',bins=np.arange(2,12))
    plt.xticks(np.arange(2,12))
    plt.show()


if __name__ == "__main__":

    simulate()




