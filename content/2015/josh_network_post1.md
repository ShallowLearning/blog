Title: What's a Neural Network? : Part 1
Date: 2015-06-13
Category: Neural Networks
Tags: Algorithms
Author: Joshua Loyal
about_author: Data scientist, physicist, wannabe guitar player, and an avid climber.
Email: jloyal25@gmail.com

Introduction
------------
In the past few years, deep neural networks have dominated the field of pattern recognition. Academically, they have had important empirical successes in applications such as computer vision, natural language processing, and speech recognition. Neural networks are actively being used and developed by industry giants such as Google, Facebook,and Microsoft. CERN used deep learning to discover the Higgs Boson in 2014. They even found a place in the arsenal of experimenting data scientists during a recent Kaggle competition: The Otto Group Product Classification Challenge.

Deep neural networks clearly have the spot light, and that popularity -- along with clever marketing -- is inspiring the imagination of even non-data scientists. Google's Inceptionism (a very fun application that everyone should try out) creates beautiful, albeit a bit creepy, works of art by essential running these networks backwards. The reason researchers at Google did this was not just to create surreal photos, but to try and answer a very important question: what are neural networks actually learning?

Although I am by no means equipped to answer that question, I have spent time training and developing neural network algorithms in both academia and industry. In the remainder of this post, I am going to work through some of the basic building blocks of how neural networks learn to recognize patterns in data. In doing so, I hope to give you a better intuition of the mechanics of neural networks, so that you can go on to understand some of the exciting breakthroughs occurring in the field.

The Language of Neural Networks: Graphs
---------------------------------------
Before we delve into the mathematics, let's briefly go over why we even call the algorithm a network. If you've done any previous reading on neural networks, it probably doesn't take long for the author to throw-up an intimidating picture like the following:

{% img center-image {filename}/images/colored_nn.svg.png  200 200 Neural Network %}

A Simple Network: Logistic Regression
---------------------------------------

One of the beautiful things about neural networks...

$$ J(\mathbf{t}) = - \frac{1}{N} \sum_i t_i \log{y_i}  $$
```python
import numpy as np

def squared_loss(x, y):
    return np.mean( (y - x)**2 )
```
