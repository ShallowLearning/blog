Title: What's a Neural Network? : Part 1
Date: 2015-06-13
Category: Neural Networks
Tags: Algorithms
Author: Joshua Loyal
about_author: Data scientist, physicist, wannabe guitar player, and an avid climber.
Email: jloyal25@gmail.com

Neural networks are what got me interested in the field of machine learning, so what better place than to make my first blog post. I am going to focus on the use of neural networks for classification although the extension to regression is rather straight forward.

A Simple Network: Logistic Regression
---------------------------------------

One of the beautiful things about neural networks...

$$ J(\mathbf{t}) = - \frac{1}{N} \sum_i t_i \log{y_i}  $$
```python
import numpy as np

def squared_loss(x, y):
    return np.mean( (y - x)**2 )
```
