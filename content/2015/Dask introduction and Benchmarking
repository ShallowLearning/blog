Title: Dask Introduction and Benchmarking (Scaling data from in memory to on disk)
Date: 2015-12-17
Category: misc   
Tags: Machine Learning, Streaming   
Author: Kevin Wang
about_author: Data scientist at PowerAdvocate and Consultant, sleepy climber
Email: kcwang@ymail.com
Summary: Introduction to Dask.  Brief Background use cases and scenario's alongw with Benchmarked Examples.  Keep reading if you care about those things.  Otherwise feel free to comment about what you would like to read

In this post we'll start by introducing a framework with which to do work on and manipulate medium to large datasets.  The datasets that people work on for machine learning vary in size from small to medium and large.  

Small datasets - All computing can easily be done on a single node or instance in terms of memory (RAM).  Your laptop or a single computer can likely handle all work related to this size of dataset. Can go up to gigabytes in terms of storage space though typically it will be in the megabytes range.

Medium datasets - Your dataset is now larger than your RAM on a single node or instance, but not larger than the disk space of your computer.  Can go up to 100s or 1000s of gigabytes in terms of storage space though that would require a large multicore workstation.

Large datasets - Your dataset now needs to be on either a database or a cluster in order to process efficiently depending on your workflow.  Can go up to petabyes in terms of storage space.

Almost all easily accessible examples of machine learning are in the small range including nearly all competition sets on Kaggle, DrivenData, and similar sites.  Then there are some of those which fall into the medium range such as the Malwarebytes competition on Kaggle or some large scale image recognition image competitions such as the Microsoft Common Objects in Context dataset.  Finally, there are the industry applications for large datasets such as Facebook's facial recognition and Google's autonomous car projects.  Typically, one can gain a large amount of insight out of a small or medium sized dataset before scaling to applications, which require large datasets.  For small datasets, in-memory computing tools such as the pandas in Python or dplyr in R are highly useful in the exploratory data analysis portion and preprocessing portion of your data analysis pipeline.  However, as your dataset size shifts from small to medium/ large memory constraints can bottleneck your pipeline and restrict your algorithm choices for analysis.  Dask can help with ease this constraint through parallelization and out of core computing.

According to the documentation, 'on a single machine dask increases the scale of comfortable data from fits-in-memory to fits-on-disk by intelligently streaming data from disk and by leveraging all the cores of a modern CPU'.  It does this through creating task graphs, which can look as simple as the one below and can operate on collections similar to arrays, bags, and dataframes.  

The goal for a framework such as dask is to be able to operate on datasets at near equivalent speeds to in memory computing tools, while not occupying a large amount of RAM.  Here we compare the performance of a the commonly used DataFrame (a 2 dimensional labeled data structure of potentially mixed types) through using dask vs. using pandas.

As you can see there is are many functions you can do in pandas, which you cannot in dask.  This is essentially because dask relies on parallel computation on your data, which has been broken down into many blocks for any operation and those functions are not easily parallelizable.  However, for the large part dask shows good performance that even beats pandas in certain operations where it's parallel nature can provide an advantage.  This also lets you run many different tasks at once, replacing your previous RAM limit with your CPU power.  Finally, for those of you who have made it through the whole post, below is an example of how sklearn can integrate with dask to operate on medium sized data, while still having memory to spare for other tasks.  Let me know in the comments what you think!
