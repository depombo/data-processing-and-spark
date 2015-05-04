### Introduction to Big Data Processing
#### Latin@ Coder Summit 2015

The slides to the presentation can be found here: https://prezi.com/htjybybpltsz/introduction-to-big-data-processing/

#### Workshop

- Download latest, compiled Spark version here: http://www.apache.org/dyn/closer.cgi/spark/spark-1.3.1/spark-1.3.1-bin-cdh4.tgz
- Unzip and navigate to the folder in your command line with:
	```cd ~/Downloads_or_wherever_it saved to/spark-1.3.1-bin-cdh4```

- All you need to do now is start Spark with the following command:
	```./sbin/start-master.sh```

- Run the following command and make sure you get access to an interactive python shell:
	```./bin/pyspark --master local[2]```

Apache Spark is now succesfully installed. If you get any erros, make sure you have python and java installed properly. 

Run your spark job by running the ./spark-1.3.1-bin-cdh4/bin/spark-submit bash script and then providing a python file with any necessary arguments, in this case, the name of a text file (../lorem_ipsum.txt).

	``` $ ./spark-1.3.1-bin-cdh4/bin/spark-submit ../path_to/word_count.py ../path_to/lorem_ipsum.txt```

If you run into any issues, or have any comments, don't hesitate to email me at lfdepombo at gmail dot com. 

