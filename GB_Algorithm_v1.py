import math
import NumPy

p_nums = [False,False,True]
gb_pairs = []
p_nums_length = len(p_nums)



def make_multiples_false(num):
    global p_nums

    start = num+1 # +1 ensures it does not include the num in the iteration
    for possible_multiple in range(start,p_nums_length):

        if possible_multiple % num == 0:
            p_nums[possible_multiple] = False




FIRST_PRIME = 2
def find_primes_until(num):
    global p_nums_length
    global p_nums

    difference = num - p_nums_length

    if difference < 0:
        return

    for counter in range(difference+1):#adds more True values until the list reaches the "limit" index number
        p_nums.append(True)
    p_nums_length = len(p_nums)

    limit = int(math.sqrt(p_nums_length)) + 1 # most efficent method as small primes would have marked all multiples
    for current_num in range(FIRST_PRIME, limit):# searches for primes then makes their multiples False
        prime =p_nums[current_num]

        if  prime == True:
            make_multiples_false(current_num)



def is_prime(num):
    if num >= p_nums_length:
        find_primes_until(num)

    return p_nums[num]