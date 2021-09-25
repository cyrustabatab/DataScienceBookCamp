import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np







def generate_deck():
    
    ranks = list(range(2,12)) + [10] * 3




    return ranks * 4




def plot_histogram(data):


    plt.hist(data,edgecolor='black',bins=np.arange(2,12))
    plt.xticks(np.arange(2,12))
    plt.show()


if __name__ == "__main__":



    deck = generate_deck()

    plot_histogram(deck)



