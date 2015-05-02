txt = open("lorem_ipsum.txt")
split_sentences = txt.read().split('.')
word_length = [len(sentence.split(' ')) for sentence in split_sentences]
print sum(word_length)/len(word_length)
	
