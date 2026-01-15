import math
from typing import List

def sieve_of_eratosthenes(n: int) -> List[bool]:
    """Returns a boolean array where prime[i] is True if i is prime"""
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    
    return prime

def count_primes_up_to(n: int, prime_array: List[bool]) -> int:
    """Count number of primes <= n using precomputed prime array"""
    return sum(1 for i in range(2, n + 1) if prime_array[i])

def solve():
    # Read input
    n, b = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Precompute primes up to a reasonable limit
    # Since factorials grow very fast, we don't need very large k values
    MAX_K = 20  # 20! is already huge (2.4e18), more than enough
    
    prime = sieve_of_eratosthenes(MAX_K)
    
    # Precompute factorials and costs
    factorials = [1]  # 0!
    for i in range(1, MAX_K + 1):
        factorials.append(factorials[-1] * i)
    
    # For each possible k, compute its cost (number of primes <= k)
    costs = []
    for k in range(MAX_K + 1):
        costs.append(count_primes_up_to(k, prime))
    
    # For each element in array, find the best possible upgrade
    upgrades = []
    
    for val in a:
        current_val = val
        base_contribution = current_val
        
        # Try all possible k >= val
        best_gain = 0
        best_k = val
        best_cost = 0
        
        for k in range(val, MAX_K + 1):
            new_val = factorials[k]
            cost = costs[k]
            gain = new_val - current_val
            
            if gain > best_gain:
                best_gain = gain
                best_k = k
                best_cost = cost
        
        # Only consider upgrades that actually improve the value
        if best_gain > 0:
            upgrades.append((best_gain, best_cost, best_k, current_val))
    
    # Sort upgrades by gain-to-cost ratio (greedy approach)
    # If cost is 0, it's free - prioritize those
    upgrades.sort(key=lambda x: float('inf') if x[1] == 0 else x[0] / x[1], reverse=True)
    
    # Apply upgrades within budget
    total_sum = sum(a)
    remaining_budget = b
    
    for gain, cost, k, original_val in upgrades:
        if cost <= remaining_budget:
            total_sum += gain
            remaining_budget -= cost
    
    print(total_sum)

solve()