import nltk
import twython

from nltk.twitter import Twitter

os.environ('TWITTER')= "/twitter-files"
#export TWITTER="/twitter-files"

tw = Twitter()
tw.tweets(keywords='love, hate', limit=10)