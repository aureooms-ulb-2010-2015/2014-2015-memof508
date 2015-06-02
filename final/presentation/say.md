
# Title page

The subject I am going to present is called
	*Lower Bounds and Algorithms in the Linear Decision Tree Model*.





# Introduction


## 1st paragraph

In summary, we are interested in the number of ``yes/no'' questions needed to
solve problems.

For example,

If we can prove that at least a certain number of questions are
required in order to solve a problem, we call this result a lower bound.

If we
come up with an algorithm solving a problem using at most a certain number of
questions, we call this result an upper bound.


## Outline

This presentation is organized as follows

### Decision Tree Model

We first define the model we are going to work with

The model is the *decision tree model*.

### ITLB

Then we explain a generic lower bound that can be derived in this model

This lower bound is called *information-theoretic lower bound*.

### SUPI

Then we give an example of a generic sorting problem in this model,
and compute its information-theoretic lower bound.

This generic sorting problem is *Sorting under Partial Information*.

### kLDT

To illustrate why we qualify our decision tree model with the adjective *linear*,
we give a second example of a problem in this model.

This problem is *k-linear degeneracy testing*.

### Application of Meiser's Algorithm

In the last part of the presentation, I will explain how to apply a point
location algorithm to the k-linear degeneracy testing problem.

This algorithm is *Meiser's algorithm*.




# Decision Tree Model

## Definition

In our model,

to solve a problem we are allowed to ask questions to an oracle that are answered
``yes'' or ``no''.

Hence, each answer gives us at most
one additional bit of information.

Each question asked to the oracle costs us a single unit.

Every other operation can be carried out for free.

## Text

Like I said in the introduction,

we are interested in lower bounds and upper bounds.

The goal of each of our analyses is to show that at least a certain
number of questions are required to be asked to solve a given problem, or
to provide an algorithm solving this problem using at most a certain number of
questions.

Note that

since instances of a problem can have variable sizes

A lower bound or an upper bound is in general expressed as a function of the input size.

