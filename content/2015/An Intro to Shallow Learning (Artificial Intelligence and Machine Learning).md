Title: This is Not the Terminator You are Looking For
Date: 2015-07-15
Category: misc   
Tags: Machine Learning, Statistics, Deep Learning   
Author: Kevin Wang
about_author: Data scientist at PowerAdvocate and Consultant, sleepy climber
Email: kcwang@ymail.com
Summary: Introduction to the Shallow Learning blog.  Brief Background to Machine Learning and A.I. while allaying concerns over the danger of a superintelligent computer killing us all.  Keep reading if you care about those things.  Otherwise feel free to comment about what you want to 

Welcome to Shallow Learning.  I plan to write a number of posts on the theme of machine learning and statistics to help people gain a more intuitive understanding of various phenomena around us.  I'm going to start with a topic that has recently gained a lot of traction in the media; the perception of the pressing danger of machine artificial intelligence (AI) concerning humanity. Going forward Josh and I will touch on many of the abstractions present and implied by the debate. 

<center>
{% img mid {filename}/images/sky_net.jpg 400 200  "Judgement Day is coming"  %}
</center>

Typically when people not directly working on AI or machine learning think about a the dangerous AI they think about a conscious malevolent superintelligence like Skynet (actually shockingly dumb, which is another problem altogether).  A long list of notables including Elon Musk, Ray Kurzweil, Bill Gates, and Stephen Hawking have expressed great concern about this topic<sup>[1][1][2][2]</sup>.  Polls are being taken of when Judgement Day will happen with scary results<sup>[3][3]</sup>. So why is this blog called Shallow Learning and not simply written by a computer? Simply put, while there have been amazing advances in AI research lately, the open problems in mimicking 1 billion years of evolution are incredibly hard if not intractable to solve. To begin to explain the current constraints of AI and why I am not worried about this result while working in the field, I need to introduce a few terms and limit my focus to the advances in Machine learning or statistical approaches to A.I.

Statistical approaches to A.I. can be divided up into three different categories; supervised learning, unsupervised learning, and reinforcement learning.  Below are my definitions of those categories.

<center>
{% img mid {filename}/images/facebook_face_tagger.jpg 400 200 Pretty sure this is your face  %}
</center>

Supervised learning - Given data that has been labeled in some manner the algorithm analyzes and infers the a function that can then infer the labels for unlabeled data. Psychologists also call this concept learning.

<center>
{% img mid {filename}/images/cat_deep_learning.jpg 400 200 16 percent sure this is something  %}
</center>

Unsupervised learning - Given unlabeled data the algorithm analyzes and draws inferences from said data

<center>
{% img mid {filename}/images/deepblue.jpg 400 200 This action is the best one  %}
</center>

Reinforcement learning - Given data an agent goes through trial and error drawing inferences through interactions or rewards and punishments

Shallow Learning will have posts that cover these far more in depth, but for now we're going to focus on the hype and limitation of deep learning: a supervised learning technique that has matched or exceeded human performance in many subtasks that measure human intelligence.

The definition of deep learning I prefer is an algorithm that can automatically learn concepts or feature representations through experience or a large number of examples. Media uses it as the ultimate buzz/scare-word as well as industry.  It is the only viable approach to building AI systems that can operate in complicated real world environments<sup>[4][4]</sup>.  Without getting too much into the details (a later post will cover this), the base algorithm for deep learning is currently the neural network, which can be described as layers of logistic regression functions.  Though extremely successful, this approach has many problems including perspective invariance, memory, limited inference in comparison to humans, and flexible hierarchical learning just to name a few.

These problems are nontrivial and necessary in representing human intelligence correctly.  A machine that cannot recognize a your friend except through her face is not a very good approximation of intelligence.  Finding efficient and viable ways for neural networks to retain stateful information as you do everytime you build a mental narrative or process the semantic relationships between words (like now) is another process necessary for mimic'ing human ability that is being researched.  Yet another higher order inference that is hard for machines to even frame is inferring social situations from cartoons that might not even fully look like humans (Josh Tenenbaum likes to call this rich learning<sup>[6][6]</sup>).  The choice as to whether to model information in a hierarchial structure that is unconstrained by human choice.  Lastly, other large concerns are limitations in reasoning, representation of knowledge and sentience in the current methodologies of machine learning make the roadmap toward AGI a nontrivial endeavor even when ignoring other practical concerns of processing time and integration.

The statistical algorithms we use for deep learning have a limitation in inference where they are susceptible to being very confident about data that is outside of what it can predict<sup>[7][7]</sup>.  This means even if researchers get all other parts of the process correct, you still have a system that cannot identify the gaps in its own reasoning, which is an undesirable form of intelligence. Lastly, limitations on representation of knowledge and sentience are tied together.  Creating a notion of self and identity for a machine that is nontrivial is something that research and philosophy currently has no means of answering.  Marvin Minsky may be correct in that an intelligence is comprised up of many non-intelligent parts with layers of processes that regulate one another, yet currently AI is not comprised of enough working unintelligent parts to even verify the hypothesis.  Integrating the algorithms that eventually prove best for each specific task will be a huge endeavor.  There is much work to be done where intelligence is concerned given that there are more deficiencies in machine learning that we have not encountered yet.

There are things I've missed and not given proper attention to.  These words are currently all I have on the topic, but the topic is large enough that I'm sure I've omitted many things.  Let me know in the comments what you think.   

1. [One of many articles about famous intlligent people think A.I. is dangerous](https://www.washingtonpost.com/blogs/the-switch/wp/2015/03/24/apple-co-founder-on-artificial-intelligence-the-future-is-scary-and-very-bad-for-people/ "Washington Post woohoo")
2. [There's a term for when people believe experts in a field that is not their own and it's residual expertise](http://simplystatistics.org/2015/05/18/residual-expertise/)
3. [Survey of when AGI when happen, when ASI will happen, when people will solve AIDS... (ok the last isn't true)](http://www.nickbostrom.com/papers/survey.pdf)
4. [Yoshua Bengio's (one of the three fathers of the deep learning movement) comment in his upcoming textbook](http://www.iro.umontreal.ca/~bengioy/dlbook/front_matter.pdf)
5. [Geoffrey Hinton's paper regarding his solution for perspective in vision](http://www.cs.toronto.edu/~fritz/absps/transauto6.pdf)
6. [Tenenbaum's classic lecture on 'rich inference' in pdf form](http://web.mit.edu/cocosci/Papers/tkgg-science11-reprint.pdf)
7. [Ian Goodfellow's Adverserial Examples paper, which formalizes this weakness](http://arxiv.org/pdf/1412.6572.pdf)

[1]: https://www.washingtonpost.com/blogs/the-switch/wp/2015/03/24/apple-co-founder-on-artificial-intelligence-the-future-is-scary-and-very-bad-for-people/ 
[2]: http://simplystatistics.org/2015/05/18/residual-expertise/ 
[3]: http://www.nickbostrom.com/papers/survey.pdf 
[4]: http://www.iro.umontreal.ca/~bengioy/dlbook/front_matter.pdf
[5]: http://www.cs.toronto.edu/~fritz/absps/transauto6.pdf
[6]: http://web.mit.edu/cocosci/Papers/tkgg-science11-reprint.pdf
[7]: http://arxiv.org/pdf/1412.6572.pdf
