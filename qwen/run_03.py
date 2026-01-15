import math

def sieve(n):
    """Return a list of primes <= n using the Sieve of Eratosthenes."""
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

def count_primes_up_to(primes, k):
    """Count number of primes <= k using precomputed primes list."""
    # Binary search to find count of primes <= k
    left, right = 0, len(primes)
    while left < right:
        mid = (left + right) // 2
        if primes[mid] <= k:
            left = mid + 1
        else:
            right = mid
    return left

def solve():
    # Read input
    N, B = map(int, input().split())
    A = list(map(int, input().split()))
    
    # We need to precompute possible operations
    # Factorials grow very fast, so we only need to check up to a certain k
    # Let's say k up to 20-25, as 20! is already huge
    MAX_K = 25
    
    # Precompute primes up to MAX_K
    primes = sieve(MAX_K)
    
    # For each possible k, compute cost and factorial value
    k_options = []
    for k in range(1, MAX_K + 1):
        cost = count_primes_up_to(primes, k)
        fact_val = 1
        for i in range(1, k + 1):
            fact_val *= i
        k_options.append((k, cost, fact_val))
    
    # For each element in the array, find the best possible replacement
    # We'll create a list of all possible beneficial operations (cost, gain)
    operations = []
    
    for val in A:
        best_gain_per_cost = -1
        
        # Find the best k for this value
        best_operation = None
        for k, cost, fact_val in k_options:
            if k >= val:  # Valid operation
                gain = fact_val - val
                if gain > 0:  # Beneficial operation
                    gain_per_cost = gain / cost if cost > 0 else float('inf')
                    if gain_per_cost > best_gain_per_cost:
                        best_gain_per_cost = gain_per_cost
                        best_operation = (cost, gain)
        
        # If we found a beneficial operation, add it
        if best_operation:
            operations.append(best_operation)
    
    # Sort operations by gain/cost ratio in descending order
    operations.sort(key=lambda x: x[0])  # Sort by cost (we'll use DP or greedy)
    
    # Use dynamic programming for knapsack-like problem
    if not operations:
        print(sum(A))
        return
        
    # Since B can be up to 10^6, we need an efficient approach
    # But operations might be limited, so let's try greedy by efficiency
    operations.sort(key=lambda x: x[1]/x[0] if x[0] > 0 else float('inf'), reverse=True)
    
    total_gain = 0
    remaining_budget = B
    
    for cost, gain in operations:
        if cost <= remaining_budget:
            total_gain += gain
            remaining_budget -= cost
    
    result = sum(A) + total_gain
    print(result)

solve()