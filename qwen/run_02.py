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

def solve():
    # Read input
    n, b = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Precompute primes up to a reasonable limit
    MAX_K = 20  # 20! is already huge, more than enough
    
    prime = sieve_of_eratosthenes(MAX_K)
    
    # Precompute factorials 
    factorials = [1]
    for i in range(1, MAX_K + 1):
        factorials.append(factorials[-1] * i)
    
    # Precompute cost (number of primes <= k) for each k
    prime_count = [0] * (MAX_K + 1)
    count = 0
    for i in range(2, MAX_K + 1):
        if prime[i]:
            count += 1
        prime_count[i] = count
    
    # For each element, find the maximum possible value we can achieve
    # considering the cost constraint
    improvements = []
    
    for val in a:
        max_improvement = 0
        min_cost_for_max = float('inf')
        
        # Find the best k >= val that maximizes the value
        best_value = val
        best_cost = 0
        
        for k in range(val, MAX_K + 1):
            new_value = factorials[k]
            cost = prime_count[k]
            
            if new_value > best_value:
                best_value = new_value
                best_cost = cost
        
        improvement = best_value - val
        if improvement > 0:
            improvements.append((improvement, best_cost))
    
    # Now we have a knapsack-like problem
    # But since we want to maximize sum and operations are independent,
    # we can use greedy by sorting by improvement
    
    improvements.sort(reverse=True)  # Sort by improvement amount
    
    total_improvement = 0
    remaining_budget = b
    
    for improvement, cost in improvements:
        if cost <= remaining_budget:
            total_improvement += improvement
            remaining_budget -= cost
    
    result = sum(a) + total_improvement
    print(result)

solve()