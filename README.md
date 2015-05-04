### Introduction to Big Data Processing - Workshop
#### Latin@ Coder Summit 2015

The slides to the presentation can be found here: https://prezi.com/htjybybpltsz/introduction-to-big-data-processing/

##### Setup

- Download latest, compiled Spark version here: http://www.apache.org/dyn/closer.cgi/spark/spark-1.3.1/spark-1.3.1-bin-cdh4.tgz
- Unzip and navigate to the folder in your command line with:

	```
	cd ~/Downloads_or_wherever_it saved to/spark-1.3.1-bin-cdh4
	```

- All you need to do now is start Spark with the following command:

	```
	./sbin/start-master.sh
	``` 
- Run the following command and make sure you get access to an interactive python shell:

	```
	./bin/pyspark --master local[2]
	```

Apache Spark is now succesfully installed. If you get any erros, make sure you have python and java installed properly. 

Run your spark job by running the spark-submit bash script under /spark-1.3.1-bin-cdh4/bin/ and then providing a python file with any necessary arguments, in this case, the name of a text file (../lorem_ipsum.txt).

``` 
./spark-1.3.1-bin-cdh4/bin/spark-submit ../path_to/word_count.py ../path_to/lorem_ipsum.txt
```

##### Exercises

You will find two problems to solve. There are several ways to solve either of them.

(1) 
```
avg_word_count_per_sentence_non_spark.py
```
Lets start simple. Create a python script that:
- Takes in text file name
- Parse the file contents as a string 
- Compute and return the average word count for all the sentences in the document/string.

The first two requirements are already done for you.  

(2)
```
avg_word_count_per_sentence.py
```
Now you are solving the same problem but using a Spark Job. The code as-is loads the text file for you into an RDD. It's up to you to Transform that Base RDD and then get the desired value through an Action.

Remember to look at the word_count.py exercise and Spark API (https://spark.apache.org/docs/latest/programming-guide.html#transformations and https://spark.apache.org/docs/latest/programming-guide.html#actions) for inspiration.

##### Solutions

All correct answers should return: 8. Navigate to the solutions folder to find a possible implementation to each of the exercises. Now that you are done, notice the overhead of solving the same problem with a Spark Job vs pure python. The latter is crealy more convenient. It's important to understand that using big data processing solutions such as Apache Spark is useful mostly when you are dealing with a sizable amont of data, not a 931 byte dataset such as ```lorem_ipsum.txt```.

If you run into any issues, or have any comments, don't hesitate to email me at lfdepombo at gmail dot com.
