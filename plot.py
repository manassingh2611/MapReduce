import sys
import matplotlib.pyplot as plt
import seaborn as sns

def plot_graph():
    n = len(sys.argv)
    if n < 2: 
         print("File name not specified\n")
         return

    file = open(sys.argv[1], 'r')
    #file = open('./output/part-r-00000', 'r')
    
    doc = file.read().split('\n')
    data = []
    for x in doc:
        word = x.split('\t')
        if(len(word) < 2): continue
        data.append(word)
    
    data.sort(key=lambda x : int(x[1]))
    
    words = []
    freq = []
    for i in data:
        words.append(i[0])
        freq.append(i[1])
    
    # The roll nos. were already added in the input data, but still adding them here
    # so that they show up in the graph too!
    roll_list = [
        "CSE3152 18dcs002",
        "CSE3152 18ucs052",
        "CSE3152 18ucs120",
    ]
    roll_freq = ["1", "1", "1"]

    plt.figure(figsize=(15,15))
    plt.xticks(rotation=90)
    plt.xlabel("words")
    plt.ylabel("frequencies")
    g = sns.lineplot(roll_list + words[-50:], roll_freq + freq[-50:], color="green")
    
    #plt.show()
    g.plot()
    file.close()

if __name__ == '__main__':
    plot_graph()
