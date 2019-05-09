import string


def find_rare_word(input_text, tweet):
    word_dict = {}
    table = str.maketrans({key: None for key in string.punctuation})
    for x in input_text:
        temp_list = x.split(' ')

        for word in temp_list:
            temp = word.translate(table)

            word_dict[temp] = word_dict.get(temp,0)+1
    
    tweet_list = tweet.split(' ')
    min_word = ''
    min_int = 100
    for x in tweet_list:
        x = x.translate(table)
        temp = word_dict.get(x,1000)
        if temp < min_int:
            min_int = temp
            min_word = x

    return(min_word)



a = ["this is,./ a test","this","test","webs area cool./,/.;;;;;"]
b  ="hello,ea.,/: this area; asdasd"


print(find_rare_word(a,b))
