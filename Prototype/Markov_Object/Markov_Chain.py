import markovify
import re
import spacy

nlp = spacy.load("en")


class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence


class Chain:

    def __init__(self, chars, tries, ratio, tweet_list):
        """constructor for a new markov chain
        @:param chars: integer instance variable for max characters in a sentence.
        @:param tries: integer number of attempts to acheive optimal ratio.
        @:param ratio: decimal between 0-1 indicating desired similarity to original text.
        TODO: make this work with any text, not just specifically a list of tweets?"""

        self.text = "\n".join(tweet_list)

        # Sentences are shown by new lines
        self.model = markovify.NewlineText(self.text)
        self.chars = chars
        self.tries = tries
        self.ratio = ratio

    def make_sent(self, chars=None):
        """Returns a generated sentence based on current text
        @:param chars: optional parameter when you want to set the character limit for a sentence"""

        if chars is None:
            chars=self.chars

        while True:
            sentence = self.model.make_short_sentence(max_chars=chars,
                                                      tries=self.tries,
                                                      max_overlap_ratio=self.ratio)
            # Ensures that no one is tagged in a post
            if "@" not in sentence:
                break

        return sentence

    def make_sent_seed(self, seed):
        """Returns a sentence that starts with the seeded term"""
        while True:
            sentence = self.model.make_sentence_with_start(beginning=seed, strict=False)

            if ("@" not in sentence) and (len(sentence) <= 140):
                break
        return sentence

    # Functions that update variable values
    def update_text(self, tweet_list):
        self.text = "\n".join(tweet_list)
        self.model = markovify.NewlineText(self.text)

    def update_chars(self, chars):
        self.chars = chars

    def update_tries(self, tries):
        self.tries = tries

    def update_ratio(self, ratio):
        self.ratio = ratio

    # Helper functions that get variable values
    def get_chars(self):
        return self.chars

    def get_tries(self):
        return self.tries

    def get_ratio(self):
        return self.ratio

    def get_text(self):
        return self.text
