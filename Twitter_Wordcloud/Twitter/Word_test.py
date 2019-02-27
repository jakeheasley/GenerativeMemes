# importing all necessery modules 
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os

def create_map(twitter_handle):
    text_file_route = "/Users/Jake/PycharmProjects/Test/Twitter_Wordcloud/Twitter/" + twitter_handle + "_tweets.txt"
    csv_file_route = "/Users/Jake/PycharmProjects/Test/Twitter_Wordcloud/Twitter/" + twitter_handle + "_tweets.csv"
    f = open(text_file_route, "r")
    lines = f.readlines()

    comment_words = ' '
    stopwords = set(STOPWORDS)

    # iterate through the csv file
    for val in lines:

        # typecaste each val to string
        #val = val.encode('utf-8', 'ignore').decode('utf-8')

        # split the value
        tokens = val.split()

        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        #top_ten(tokens)

        for words in tokens:
            comment_words = comment_words + words + ' '

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(comment_words)

    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()



    delete = raw_input("\n\nWould you like to delete text and csv files? (y/n) ")
    if delete == "y":
        os.remove(text_file_route)
        os.remove(csv_file_route)



if __name__ == '__main__':
    create_map()