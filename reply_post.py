import praw
import re
import random

goldie_quotes = \
[
"He's got him in some kind of strange choke I've never seen before.",
"Because SOAKoudjou is so highly touted... you almost want to sit back and" \
"watch and SOAK it in.",
"If his last name were Johnson, the nickname Dean of Mean would make no sense.",
"...So you want to be an ultimate fighter?",
"HERE WE GO..",
"AND IT IS ALL OVER!",
"JUST LIKE THAT!",
"His precision is uh... really precise.",
"Tito taking a book out of Chuck's chapter right there.",
"...leg kick to the midsection.",
"Diaz smells the opening..",
"Michael Jordan-esque... in his grappling skills is Travis Lutter"
]

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit('mma')


def createComment(term1, term2):
    while True:
        try:
            for comment in subreddit.stream.comments():
                #so it doesn't infinitely respond to itself.
                if comment.author.name == "GhostofMikeGoldberg":
                    pass
                else:
                    if re.search(term1, comment.body, re.IGNORECASE) or \
                       re.search(term2, comment.body, re.IGNORECASE):
                        print comment.body
                        goldie_reply = "You have been visited by the Ghost of Mike " \
                                    "Goldberg's past...  \n" \
                                    + "&nbsp;  \n" + "*" + random.choice(goldie_quotes) + "*" \
                                    + "&nbsp;  \n" "**I am a spooky bot that haunts r/mma**"
                        
                        comment.reply(goldie_reply)
                        print goldie_reply
        except:
            pass

createComment('mike goldberg', 'goldie')




