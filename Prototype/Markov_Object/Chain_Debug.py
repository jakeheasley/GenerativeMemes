from Markov_Object.Markov_Chain import Chain

# testing file for Markov generator


filepath = "testing.txt"
chars = 140
tries = 200
ratio = .5

test_chain = Chain(chars=chars, tries=tries, ratio=ratio, filepath=filepath)
print(test_chain.get_chars())
print(test_chain.get_ratio())
print(test_chain.get_tries())
print(test_chain.get_filepath())

print(test_chain.make_sent(1))
