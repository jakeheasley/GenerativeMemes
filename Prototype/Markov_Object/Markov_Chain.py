import markovify


class Chain:

    # Initialize a new Markov chain:
    # chars = max characters in sentence
    # tries is number of attempts where Markovify tries to get optimal ratio
    # ratio = decimal of desired similarity to original sentence
    def __init__(self, chars, tries, ratio, tweet_list):

        self.text = "\n".join(tweet_list)

        # Sentences are shown by new lines
        self.model = markovify.NewlineText(self.text)
        self.chars = chars
        self.tries = tries
        self.ratio = ratio

    # Function that returns given number of sentences based on existing model
    def make_sent(self, num_sent):
        sentences = []

        while num_sent > 0:
            sentence = self.model.make_short_sentence(max_chars=self.chars,
                                                      tries=self.tries,
                                                      max_overlap_ratio=self.ratio)
            # Ensures that no one is tagged in a post
            if "@" not in sentence:
                sentences.append(sentence)
                num_sent -= 1

        return sentences

    # Functions that update variable values
    def update_text(self, filepath):
        with open(filepath, encoding = "utf-8") as f:
            text = f.read()
        self.model = markovify.NewlineText(text)

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
