# Master-thesis
The codes comprise of both ipynb and py files. They can be run by creating a python virtual environment
and downloading the required dependencies from requirements.txt

#Order of files
First preprocessing is done using the regex in parser.py. Output from this is passed to the oh_isolation.ipynb file to carryout the further preprocessing where the words are converted to the lower case, special characters are removed and unwanted numerical data is also removed such as len: and time: along with the removal of stopword(for example: is, in, the, but etc) buy adding custom list to prevent information loss. The sentences which has less than 5 words are removed and each sentence is padded to the word length of 50 to keep the consistent length of each sentence.The one hot encoding is applied to turn the each unique word into the features and the presence of each word in a sentence is detected and assigned binary value. The data is shuffled randomly and split into 2 traning sets and one test set.

The X_train1_oh.csv, X_train2_oh.csv and X_test_oh.csv is passed to autoencod.ipynb file. The dataset are scaled to 0-1 using min max scaler and the X_train1_scaled.csv is passed to the first autoencoder and trained which result in reducing the feature dimension. After which the predict() is used on X_train2_scaled.csv and X_test_scaled.csv to reduce the feature dimensions.

The X_train2_scaled is passed to isolation forest to training and the positive and negative logs are predicted for the X_test_scaled.csv. 

Part of this positive logs are passed to second autoencoder and trained. Later the used for predicting features which generates o1. The rest of positive logs and negative logs are also passed for feature prediction which generates o2.

The mean and standard deviation of o1 for each row is computed. Later a threshold(std * c) is found where std is standard deviationa and c is constant(calculated based on the predicted percentage of negative logs in test data by the Isolation forest. The mean for o2 is calculated as well for each sample and if the mean is less than the threshold then it is considered as Anamoly.
