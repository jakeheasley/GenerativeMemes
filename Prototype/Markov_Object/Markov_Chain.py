import markovify


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

    def make_sent(self):
        """returns self.tries number of sentences based on self.text."""

        while True:
            sentence = self.model.make_short_sentence(max_chars=self.chars,
                                                      tries=self.tries,
                                                      max_overlap_ratio=self.ratio)
            # Ensures that no one is tagged in a post
            if "@" not in sentence:
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
