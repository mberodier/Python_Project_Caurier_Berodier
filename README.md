# Python_Project_Caurier_Berodier
Grégoire Caurier &amp; Mattéo Berodier repository for python project




We were asked to deal with the QSAR biodegradable dataset in order to build an accurate model which would be able to tell if a chemical is biodegradable or not.
Here is our work on it, you'll find our notebook, powerpoint and our database in .csv in this repository.



First of all, we worked on the data visualization and process to have a better view on it and to be able to test this database with the greatest accuracy possible. So we firstly looked at the number of columns, parameters and started to do a global visualization. After that, we noticed that some of the variables were always null and some of them wern't correlated with the biodegradable aspect of the chemicals we've got. And with a more specific analysis of theses, through some charts, we were able to assure that we could ignore them in our final model without modifying the accuracy of it.


Besides, we decided to format all our remaining values in order to use every data, specialy the null ones. We also transformed the ReadyBiodegradable/NotReadyBiodegradable values from string to binary for the same reason. Then our dataset was ready to be tested.



After, we started to create our model by splitting our database in two parts (training and test) and we tested it with a bunch of algorithms such as K Neighbors Classifier, Logistic regression, RandomForest. Then we compared the score of each algorithm and we sorted them decreasingly to think about it. And we decided for the next part to keep the 4 best algorithm

Later, we started to search for hyperparameter with cross_val and GridSearch functions to increase the scores of our algorithms. This was our way to make our model more accurate, and it worked. 
We finally had a maximum accuracy score of 0,92 with the multi-layer perceptron.



To conclude, we created an API with Flask to enable any user to know if a chemical is biodegradable or not with the input of all the variables. 



