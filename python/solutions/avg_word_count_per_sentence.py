from __future__ import print_function

import sys

from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile(sys.argv[1], 1)
    split_sentences = lines.flatMap(lambda x: x.split('.')) # Base RDD
    words_per_sentence = split_sentences.map(lambda x: len(x.split(' ')) ) 
    avg_word_count_per_sentence = words_per_sentence.reduce(lambda a,b: a+b) / split_sentences.count()
    print("%i" % avg_word_count_per_sentence)

    sc.stop()

