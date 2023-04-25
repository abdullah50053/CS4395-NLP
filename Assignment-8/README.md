# Assignment 8

## Overview

This assignment is about gaining experience with sklearn (Naive Bayes, Logistic Regression, Neural Networks) using text data as well as text classification. 

## Analysis
Overall, the Logistic Regression model worked the best, followed by the Neural Network and then the Naive Bayes algorithms. The accuracy scores overall were very low and not indicative of a very strong correlation, likely because there is little correlation between the EEG headset data and the state of a person's eyes being open or shut. All the accuracy scores were within 15% of a random guess, with the LR anf NN algorithms doing better and slightly better than a random guess and NB doing slightly worse. One possible explanation for the low accuracy is that the data used to train and test the models was limited to a 117-second sample that was manually labeled. Increasing the amount of data fed into the Neural Network model could be beneficial in the long run, as Neural Networks tend to perform better with larger datasets. Overall, the results suggest that further research is needed to better understand the relationship between EEG headset data and the state of a person's eyes being open or shut.