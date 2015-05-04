from __future__ import print_function

import sys

from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile(sys.argv[1], 1)
    split_words = lines.flatMap(lambda x: x.split(' ')) # Base RDD
    counts = split_words.map(lambda x: (x, 1)).reduceByKey(lambda a,b: a+b) # Transformed RDD
    output = counts.collect() # Action triggers materialization of RDD through its lineage
    for (word, count) in output:
        print("%s: %i" % (word, count))

    sc.stop()

