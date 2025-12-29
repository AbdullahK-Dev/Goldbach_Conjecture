## Overview

This project investigates the Goldbach Conjecture which states every even number > 2 can be written as the sum of 2 prime numbers. Currently the program takes an even input and generates goldbach pairs for every even number up until the input storing each pair with the even number.

## Learning Objectives

- Improve my understanding of Git and Github.
- Gain expereince with working with large numerical ranges.
- Practise debugging and fixing errors.

## Technical Implementation

The program must be able to handle large ranges of even numbers making effecint algorithm design key. 
Overall to find Goldbach Pairs the program first generates all the prime numbers until the limit which is the even number that the user inputs. Using the array with all the prime numbers the program finds the difference between the first prime in the array and the current even number. If the difference is prime then we have found our GoldBach Pair, else we continue to iterate through the prime numbers array. Once a Goldbach Pair has been found the program moves to the next even number and repeats this process until all pairs have been found.

- a
- a

## Code Quality and Maintainability

- a
- a

## Future Improvements

- a
- a



I am attempting to make an algorithm that tests Goldbach's Conjecture, for example "8 = 5 + 3").

The goal of this project is to help me improve core skills of programing, specifically readability and effencincy when writing code.
Also its a fun puzzle :D

To improve effeciency I have implemeneted:
  Sieve of Erathonos algorithm - this helps with large ranges of prime numbers.
  Use of arrays from Numpy library - Arrays are faster then lists and I am only using Integers so it is the most logical choice.

To improve Redability I have implemented:
  Subroutines - to reduce the amount of nesting required and assist in maintainablilty.
  Descriptive variable names - although they may be abit lengthy at times I believe it is better to prioritse making them understable because this algorithm can get complicated.
  Comments where neccesary.

I may not get to completing all of these further steps however here is a rough outline of places i could improve/expand on in this project.
Further steps:
  Port the code to C++ to reduce run time.
  Explore more prime number generating algorithms such as Sieve of Atkin and Sieve of Sundaram.
  Implement graphs using libraries such as seaborn to: compare effecincy of different prime number generator algorithms ;explore patterns between prime numbers such as the differences between them.
