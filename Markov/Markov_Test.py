import markovify
import sys


def gen_markov(text, name):

    model = markovify.NewlineText(text)

    sentences = []
    for i in range(50):
        sentences.append(model.make_short_sentence(max_chars=140, tries=100, max_overlap_ratio=.6))
        print sentences[i]

    with open(str(name) + '_markov.txt', 'w+') as f:
        for sentence in sentences:
            f.write(sentence + "\n")


if __name__ == '__main__':
    handles, tweets = sys.argv
    gen_markov(tweets, handles)
