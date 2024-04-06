def sub(a, b):
    print(a-b)
print(sub(5, 6))

def count_perfect_divisors(arr):
    MOD = 10**7
    n = len(arr)
    total_sum = 0
    
    # Calculate the number of non-empty subsequences (2^n - 1)
    num_subsequences = (1 << n) - 1
    
    # Iterate through all possible subsequences
    for i in range(1, num_subsequences + 1):
        product = 1
        for j in range(n):
            if i & (1 << j):
                product *= arr[j]
        # Count distinct prime factors of the product
        prime_factors_count = count_prime_factors(product)
        total_sum += prime_factors_count
    
    return total_sum % MOD

def count_prime_factors(num):
    factors = set()
    for i in range(2, int(num**0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return len(factors)

# Example usage:
A1 = [2, 15]
result1 = count_perfect_divisors(A1)
print(result1)  # Output: 11

A2 = [2, 4, 8, 16, 32]
result2 = count_perfect_divisors(A2)
print(result2)  # Output: 31
