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
    # start by initializing prime with the minimum value
    # in the case of number_range, as defined, it will always be 2 on the first loop iteration
    prime = min(sorted(number_range))

    number_range.remove(prime)
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
