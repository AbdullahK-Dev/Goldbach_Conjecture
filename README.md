## Overview

This project investigates Goldbach's Conjecture, which states that every even integer greater than 2 can be expressed as the sum of two prime numbers. The program accepts an even integer as an upper limit and finds one Goldbach pair for each even integer greater than 2 up to that limit.

## Technical Implementation

### Prime Generation

The program uses the Sieve of Eratosthenes to identify all prime numbers up to the user-specified limit. A Boolean array is used to track potential prime numbers, where each index represents an integer and its Boolean value indicates whether it is a prime number.

The array is initially set up with index postions 0 and 1 marked as False because they are not prime, and index position 2 marked as True because it is the first prime number. Based on the upper limit given by the user an additional array with all values set intially as True is concatinated, these values are tempoaray, representing they are potentially a prime number.

The algorithm then iterates through the array, marking the multiples of the first True value as False then repeats the process with the next until it gets to the end of the array, hence removing all multiples of the prime numbers. Therefore the index positions that remain True have no multiples except 1 and themselves which means they are prime numbers.

### Goldbach Pair Generation

For each even integer, the program iterates through the generated prime numbers and calculates the difference between the even integer and the first prime number. The is_prime() subroutine checks whether this difference is prime by accessing its corresponding index position in the Boolean array, if the difference is prime then it means a Goldbach pair has been found, else the algorithm moves on to the next prime number repeating the process. This process continues until a pair has been generated for every even integer within the specified range.

## Code Quality and Maintainability
The following features are included to increase readability:
- Comments where the logic is complex.
- Descriptive variable names.
- Subroutines to break down large blocks of code therefore reducing nesting.
