import sys

if len(sys.argv) != 2:
    print("Usage: wordcount <file>", file=sys.stderr)
    exit(-1)
txt = open(sys.argv[1])

split_sentences = txt.read().split('.')
word_length = [len(sentence.split(' ')) for sentence in split_sentences]
avg_word_count_per_sentence = sum(word_length)/len(word_length)
print avg_word_count_per_sentence

