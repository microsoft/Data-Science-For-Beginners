# A Brief Introduction to Statistics and Probability

Statistics and Probability Theory are two highly related areas of Mathematics that are highly relevant to Data Science. It is possible to operate with data without deep knowledge of mathematics, but it is still better to know at least some basic concepts. Here we will present a short introduction that will help you get started.

## Pre-Lecture Quiz

[Pre-lecture quiz]()

## Probability and Random Variables

**Probability** is a number between 0 and 1 that expresses how probable an **event** is. It is defined as a number of positive outcomes (that lead to the event), divided by total number of outcomes, given that all outcomes are equally probable. For example, when we roll a dice, the probability that we get an even number is 3/6 = 0.5.

When we talk about events, we use **random variables**. For example, the random variable that represents a number obtained when rolling a dice would take values from 1 to 6. Set of numbers from 1 to 6 is called **sample space**. We can talk about probability of a random variable taking a certain value, for example P(X=3)=1/6.

The random variable in previous example is called **discrete**, because it has a countable sample space, i.e. there are separate values that can be enumerated. There are cases when sample space is a range of real numbers, or the whole set of real numbers. Such variables are called **continuous**. An good example is the time when the bus arrives.

## Probability Distribution

In the case of discrete random variables, it is easy to describe the probability of each event by a function P(X). For each value *s* from sample space *S* it will give a number from 0 to 1, such that the sum of all values of P(X=s) for all events would be 1.

The most well-known discrete distribution is **uniform distribution**, in which there is a sample space of N elements, with equal probability of 1/N for each of them. 

It is more difficult to describe the probability distribution of a continuous variable. Consider the case of bus arrival time. In fact, for each exact arrival time $t$, the probability of a bus arriving at exactly that time is 0!

> Now you know that events with 0 probability happen, and very often! At least each time when the bus arrives!

We can only talk about the probability of a variable falling in a given interval of values, eg. P(t<sub>1</sub>&le;X&lt;t<sub>2</sub>). In this case, probability distribution is described by a **probability density function** p(x), such that

<img src="http://www.sciweavers.org/tex2img.php?eq=P%28t_1%5Cle%20X%3Ct_2%29%3D%5Cint_%7Bt_1%7D%5E%7Bt_2%7Dp%28x%29dx&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="P(t_1\le X<t_2)=\int_{t_1}^{t_2}p(x)dx" width="228" height="51" >
  
An continuous analog of uniform distribution is called **continuous uniform**, which is defined on a finite interval. A probability that the value X falls into an interval of length l is proportional to l, and rises up to 1.

Another important distribution is **normal distribution**, which we will talk about in more detail below.

## Mean, Variance and Standard Deviation

Suppose we draw n samples of a random variable X: {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>}. We can define **mean** (or ** arithmetic average**) value of the sequence in the traditional way as (x<sub>1</sub>+x<sub>2</sub>+x<sub>n</sub>)/n. As we grow the size of the sample (i.e. take the limit with n&rarr;&infin;), we will obtain the mean (also called **expectation**) of the distribution.

> It can be demonstrated that for any discrete distribution with values x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub> and corresponding probabilities p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub>, the expectation would equal to E(X)=x<sub>1</sub>p<sub>1</sub>+x<sub>2</sub>p<sub>2</sub>+...+x<sub>N</sub>p<sub>N</sub>.

## Normal Distribution

## 🚀 Challenge


## Post-Lecture Quiz

[Post-lecture quiz]()

## Review & Self Study


## Assignment

[Assignment Title](assignment.md)
