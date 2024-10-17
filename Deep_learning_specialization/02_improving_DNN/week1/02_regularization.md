# Regularization of ANN

If you suspect your neural network is over fitting your data, that is, you have a `high variance problem`, one of the first things you should try is probably `regularization`. The other way to address high variance is to get more training data that's also quite reliable. But you can't always get more training data, or it could be expensive to get more data. 

## L2 Regularization


Lambda here is called the regularization parameter.

## L1 Regularization
If you use L1 regularization, then w will end up being sparse. And what that means is that the w vector will have a lot of zeros in it.

## Dropout Regularization

 what we're going to do is go through each of the layers of the network and set some probability of eliminating a node in neural network. 

 ### Inverted Dropout
 
Why does it work? So as a regulizer, let's give some better intuition. In the previous video, I gave this intuition that drop out randomly knocks out units in your network. So it's as if on every iteration you're working with a smaller neural network. And so using a smaller neural network seems like it should have a regularizing effect.

## Other Regularization

1. Data Augmentation
    * If you are over fitting getting more training data can help, but getting more training data can be expensive and sometimes you just can't get more data. But what you can do is augment your training set by taking image like this. And for example, flipping it horizontally and adding that also with your training set. So now instead of just this one example in your training set, you can add this to your training example. 

2. Early Stopping

