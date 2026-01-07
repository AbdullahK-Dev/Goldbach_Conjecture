import math
import numpy as np



#p stands for prime and gb stands for goldbach

p_bool_array = np.array([False, False, True]) #index position represents the number, value represents whether its prime
p_bool_length = len(p_bool_array)
p_nums = np.where(p_bool_array == True)[0] #array with all prime numbers(index True represents prime), [0] because we are only using the 1st dimension
gb_pairs = []



def make_multiples_false(multiple, data_structure, start = 0, end_position = None):
    
    if start < multiple:
        start_position = 2 * multiple # "2*" to avoid iterating over prime number
    else:
        start_position = start - (start % multiple) + multiple# "start - (start % multiple)" finds the highest multiple that is less than start --> "+ multiple" to avoid iterating over prime number

    if end_position == None:
        end_position = len(data_structure)

    for possible_multiple in range(start_position , end_position, multiple): #num + 1 ensures it does not include the num in the iteration
        data_structure[possible_multiple] = False



def find_primes_until(num): #primes found are stored in p_nums
    global p_bool_array
    global p_bool_length
    global p_nums

    difference = num - p_bool_length
    if difference < 0: #returns incase primes have already been found
        return
    
    true_arr = np.ones(difference, dtype=bool) #array that holds extra true values
    p_bool_array = np.concatenate((p_bool_array, true_arr))
    p_bool_length = len(p_bool_array)

    last_confirmed_prime = p_bool_length - np.argmin(p_bool_array[::-1]) # finds the last false value's index --> must do "length -" because array is inversed by [::-1] 
    limit = int(math.sqrt(p_bool_length)) + 1 # most efficent method as small primes would have marked all multiples

    for potential_prime in range(last_confirmed_prime, limit):# searches for primes then makes their multiples False
        if is_prime(potential_prime) == True:
            make_multiples_false(potential_prime, p_bool_array, p_bool_length-difference, p_bool_length)

    p_nums = np.where(p_bool_array == True)[0] #array with all prime numbers(index True represents prime), [0] because we are only using the 1st dimension



def is_prime(num): #returns true or false depending if prime
    if num >= p_bool_length:
        find_primes_until(num)

    return p_bool_array[num]



FIRST_EVEN = 4
def find_gb_pairs_until(last_even):

    find_primes_until(last_even) #to avoid calling the array multiple times
    
    for even_num in range(FIRST_EVEN, last_even+2, 2): #+2 because it is exclusive of last_even
        
        pair_found = False
        counter = 0

        while pair_found == False:

            certain_p = p_nums[counter]
            possible_p = even_num - certain_p
            
            if is_prime(possible_p) == True:
                pair_found = True
                gb_pairs.append([even_num, certain_p, possible_p])
            
            counter += 1



def print_gb_pairs():
    print("\nHere are the Goldbach Pairs")
    for element in gb_pairs:
        format = f"{element[1]}".center(12) + "+" + f"{element[2]}".center(12) + "=" + f"{element[0]}".center(12)
        print(format)



def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False



print("\nThis project investigates the Goldbach Conjecture which states every even number > 2 can be written as the sum of 2 prime numbers. Currently the program takes an even input and generates Goldbach pairs for every even number up until the input storing each pair with the even number in an array then outputing the pairs and even numbers.")

last_even = int(input("\nUp to what even number would you like to search until : "))

while is_even(last_even) != True or last_even <= 2:
    print("\nPlease enter an even number that is greater than 2")
    last_even = int(input("Up to what even number would you like to search until : "))

find_gb_pairs_until(last_even)
print_gb_pairs()