# TwitterClassification
Using machine learning to classify tweets subjects


## Obtaining data

The tweets used here were obtained using the Twitter's APIs and a library called tweepy which ones give us access to opened data.
In adition to the tweets, it was used a collection of embedding vectors calculated using the Glove algorithm.
These vectors were built in order to represent the semantical distance of english words using texts in the learning process.
It was used a Twitter context to extract the vectors containing 2B tweets and 1.2M words.

The links for the APIs and the Glove data are:
https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/introduction
https://docs.tweepy.org/en/stable/streamingclient.html
https://nlp.stanford.edu/projects/glove/


## The models

The main goal of this project is to classify the tweet subject.
Twitter API already do this, however for some subjects the classification given by twitter is confusing or they are labeled with some generic subject, like "city" or "person".
Thus, our proposal is to improve the classification on this blured subjects and to give the classification confidence as well in the Twitter's entity classification.

To do this, we designed two differen model structures: Standard model and two-phases model.
The first one is focused on improving the model itself and the second one is focused on creating an artificial database to train a model.
Both seeking a better accuracy.

### Standard model
The standard model were built comparing some of the well-known algorithms for text classification with a tunning process to search for hyperparameters that gives the maximum local results.

### Two-phases model
The two-phases model were built comparing different artificial databases choosing the one that best helps a well-known algorithm. This artificial database is used to pre-train the model at the apriori-phase and then the model will be trained using the labeled databased at the aposteriori-phase.

### Hybrid model (possibility)

At the end, if both models give a good result we have the possibility of merging both models to try a better result.
Adding the artificial database to pre-train the first model.

## Training models

The models will be trained using a labeled database which we didn't decided yet...


## Testing models

The models will be evaluated using part of the labaled databased used to train, compared to Twitter's labels, and tested using humans as an oracle.
This oracle will be represented by a web application that will gatther answers from its users.
The idea is to show a tweet text and its label in order to get the opinion of the user in some scenarios:

1- Correct/Wrong options for the user saying if the tweet belongs to that label
2- Label options for the user choose as the most related option

## Data Visualization

The results will be shared in the same web application that was used to get the oracle labels.
A second web application will be developed for showing statistics about a Twitter timeline or Twitter account using the labels obtained from the best model according to very same users!
It may show the most frequent subject, a recent trending subject or even show all tweets but one subject.. all sort of cool stuffs.

Don't loose the oportunity to be our Oracle!

## Authors

Tiago Faria
Márcio Antônio
