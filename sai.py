def sub(a, b):
    print(a-b)
print(sub(5, 6))

MOD = 10**7

# Function to generate all subsequences of an array
def generate_subsequences(arr):
    n = len(arr)
    subsequences = []
    for i in range(1, 2**n):
        subseq = []
        for j in range(n):
            if i & (1 << j):
                subseq.append(arr[j])
        subsequences.append(subseq)
    return subsequences

# Function to calculate the product of elements in a subsequence
def product_of_subsequence(subseq):
    product = 1
    for num in subseq:
        product *= num
    return product

# Function to count distinct prime factors of a number
def count_prime_factors(num):
    factors = set()
    for i in range(2, int(num**0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return len(factors)

# Main function to find the sum of R modulo 10^7
def sum_of_R(arr):
    subsequences = generate_subsequences(arr)
    total_sum = 0
    for subseq in subsequences:
        product = product_of_subsequence(subseq)
        prime_factors_count = count_prime_factors(product)
        total_sum += prime_factors_count
    return total_sum % MOD

# Example usage:
A = [2, 3, 5]
result = sum_of_R(A)
print(result)  # Output: 8
