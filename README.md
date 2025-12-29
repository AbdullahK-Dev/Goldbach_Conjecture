## Overview

This project investigates the Goldbach Conjecture which states every even number > 2 can be written as the sum of 2 prime numbers. Currently the program takes an even input and generates Goldbach pairs for every even number up until the input storing each pair with the even number.

## Learning Objectives

- Improve my understanding of Git and GitHub.
- Gain experience with working with large numerical ranges.
- Practise debugging and fixing errors.

## Technical Implementation

To find Goldbach pairs the program must first generate an array with all primes until the limit which is the even number that the user inputs. Using the prime number array the algorithm finds the difference between the first prime in the array and the current even number. If the difference is prime then we have found our Goldbach pair, else we continue to iterate through the prime numbers array. Once a Goldbach pair has been found the program moves to the next even number and repeats this process until all pairs until the limit have been found.

<br />

Efficiency is key because the program must be able to handle large ranges, due to this the following features have been implemented: 
- Sieve of Eratosthenes to efficiently generate prime numbers through reducing the number of iterations required to check a large range.
- Stored results to avoid unnecessary prime checks.
- NumPy arrays because of their memory efficiency which decreases run time when generating prime numbers.

## Code Quality and Maintainability
The following features are included to increase readability:
- Comments where the logic is complex.
- Descriptive variable names.
- Subroutines to break down large blocks of code therefore reducing nesting.

## Future Improvements

- Plotting graphs using libraries such as seaborn to make data easier to understand.
- Porting the program to C++ because it is more efficient than python therefore allowing for even larger ranges.
