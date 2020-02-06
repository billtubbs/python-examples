# Python script to analyse words in a text

# Insert text here
with open('text.txt', 'r') as f:
    text = f.read()

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
