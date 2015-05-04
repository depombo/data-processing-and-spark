from __future__ import print_function

import sys

from pyspark import SparkContext


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile(sys.argv[1], 1)

    ####### Please define a series of Transformations on the Base RDD to get the average word count per sentence. ######
    ####### Use the basic wordcount example for inspiration. #########
    ####### FILL IN YOUR WORK BELOW ########


    print("%i" % avg_word_count_per_sentence)
    sc.stop()

