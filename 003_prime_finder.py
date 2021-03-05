# Let's find all prime numbers between 2 and n
# prime number ►
# n.	A positive integer that is greater than 1
# and is not divisible without a remainder by any positive integer other than itself and 1.

n = 600
number_range = set(range(2, n + 1))
# {2, 3, 4, 5,...,n}
# print(f"Original number range: \n{number_range}")

primes_list = []

while number_range:
    # The pop() method removes an arbitrary element from the set and returns the element removed.
    # is based on a HashMap
    # removes the first element, which is the smaller hashcode
    # In the case of set of ints, it's the smallest int. <====
    # this means we'll start by initializing prime with the value of 2
    prime = number_range.pop()

    primes_list.append(prime)

    # will create multiples based on the prime we found
    # will use step -- we want to increment in steps of our prime number
    # range([start], stop[, step])
    multiples = set(range(prime * 2, n + 1, prime))
    # print(multiples)

    # The difference_update() method removes the items that exist in both sets.
    # removes the unwanted items from the **original set**.
    number_range.difference_update(multiples)
    # print(number_range)

# print(primes_list)
prime_count = len(primes_list)
largest_prime = max(primes_list)
print(f"There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}.")
