# Python script to analyse words in a text

# Insert text here
text = """
CROWD:  A witch!  A witch!  A witch!  A witch!  We've found a witch!  A witch!
    A witch!  A witch!  A witch!  We've got a witch!  A witch!  A witch!  Burn
    her!  Burn her!  Burn her!  We've found a witch!  We've found a witch!  A
    witch!  A witch!  A witch!
VILLAGER #1:  We have found a witch.  May we burn her?
CROWD:  Burn her!  Burn!  Burn her!  Burn her!
BEDEVERE:  How do you know she is a witch?
VILLAGER #2:  She looks like one.
CROWD:  Right!  Yeah!  Yeah!
BEDEVERE:  Bring her forward.
WITCH:  I'm not a witch.  I'm not a witch.
BEDEVERE:  Uh, but you are dressed as one.
WITCH:  They dressed me up like this.
CROWD:  Augh, we didn't!  We didn't...
WITCH:  And this isn't my nose.  It's a false one.
BEDEVERE:  Well?
VILLAGER #1:  Well, we did do the nose.
BEDEVERE:  The nose?
VILLAGER #1:  And the hat, but she is a witch!
VILLAGER #2:  Yeah!
CROWD:  We burn her!  Right!  Yeaaah!  Yeaah!
BEDEVERE:  Did you dress her up like this?
VILLAGER #1:  No!
VILLAGER #2 and 3: No.  No.
VILLAGER #2:  No.
VILLAGER #1:  No.
VILLAGERS #2 and #3:  No.
VILLAGER #1:  Yes.
VILLAGER #2:  Yes.
VILLAGER #1:  Yes.  Yeah, a bit.
VILLAGER #3:  A bit.
VILLAGERS #1 and #2:  A bit.
VILLAGER #3:  A bit.
VILLAGER #1:  She has got a wart.
RANDOM:  [cough]
BEDEVERE:  What makes you think she is a witch?
VILLAGER #3:  Well, she turned me into a newt.
BEDEVERE:  A newt?
VILLAGER #3:  I got better.
VILLAGER #2:  Burn her anyway!
VILLAGER #1:  Burn!
CROWD:  Burn her!  Burn!  Burn her!...
BEDEVERE:  Quiet!  Quiet!  Quiet!  Quiet!  There are ways of telling whether
    she is a witch.
VILLAGER #1:  Are there?
VILLAGER #2:  Ah?
VILLAGER #1:  What are they?
CROWD:  Tell us!  Tell us!...
BEDEVERE:  Tell me, what do you do with witches?
VILLAGER #2:  Burn!
VILLAGER #1:  Burn!
CROWD:  Burn!  Burn them up!  Burn!...
BEDEVERE:  And what do you burn apart from witches?
VILLAGER #1:  More witches!
VILLAGER #3:  Shh!
VILLAGER #2:  Wood!
BEDEVERE:  So, why do witches burn?
"""

# Extract words
words = [word.strip(",.;!?-–'") for word in text.split()]
print("Words:", len(words))

# Calculate word lengths
word_lengths = [len(word) for word in words]
print("Avg. word length: {:.1f} chars".format(
      sum(word_lengths) / len(word_lengths)))
longest = word_lengths.index(max(word_lengths))
longest_word = words[longest]
print("Longest word: {:s} ({:d})".format(longest_word, len(longest_word)))

# Make a tally of word counts
word_tally = {}
for word in words:
    word_tally[word] = word_tally.get(word, 0) + 1
print("Top-10 words longer than 3 letters:")
long_word_tally = {word: n for word, n in word_tally.items() if len(word) > 3}
print(sorted(long_word_tally.items(), key=lambda x: x[1], reverse=True)[:10])
