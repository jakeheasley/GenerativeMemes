import TwitterScrape
import Word_test

twitter_handle = raw_input("Enter a twitter handle: ")
TwitterScrape.get_all_tweets(twitter_handle)
Word_test.create_map(twitter_handle)
