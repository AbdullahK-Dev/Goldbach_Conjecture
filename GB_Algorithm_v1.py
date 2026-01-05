import math
import numpy as np



#p stands for prime and gb stands for goldbach

p_bool_array = np.array([False, False, True]) #index position represents the number, value represents whether its prime
p_bool_length = len(p_bool_array)
p_nums = np.where(p_bool_array == True)[0] #array with all prime numbers(index True represents prime), [0] because we are only using the 1st dimension
gb_pairs = []



def make_multiples_false(num): #this acts on p_bool_array only
    global p_bool_array

    for possible_multiple in range(num + 1, p_bool_length): #num + 1 ensures it does not include the num in the iteration
        if possible_multiple % num == 0:
            p_bool_array[possible_multiple] = False



FIRST_PRIME = 2
def find_primes_until(num): #primes found are stored in p_nums
    global p_bool_length
    global p_bool_array
    global p_nums

    difference = num - p_bool_length

    if difference < 0: #returns incase primes have already been found
        return
    
    true_arr = np.ones(difference, dtype=bool) #array that holds extra true values
    p_bool_array = np.concatenate((p_bool_array, true_arr))

    p_bool_length = len(p_bool_array)



    limit = int(math.sqrt(p_bool_length)) + 1 # most efficent method as small primes would have marked all multiples
    for current_num in range(FIRST_PRIME, limit):# searches for primes then makes their multiples False
        
        prime = p_bool_array[current_num]
        if  prime == True:
            make_multiples_false(current_num)

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
    for element in gb_pairs:
        #format = f"{element[1]} + {element[2]} = {element[0]}".center(30)
        format = f"{element[1]}".center(12) + "+" + f"{element[2]}".center(12) + "=" + f"{element[0]}".center(12)
        print(format)



last_even = int(input("Up to what even number would you like to search until : "))

find_gb_pairs_until(last_even)
print_gb_pairs()