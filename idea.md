##  Core idea:

Idea is to combine **number theory**(prime number and factorials) with a greedy stratigy under a fixed budget constraint.
Eash factorial value **k!** has an associated cost, define as the number of prime numbers less than or equal to k. Give a limited budget **B**, we aim to select the **largst possible factorial** whose prime cost does not exceed the budget.
This selected factorial replaces the **smallest element** in the array to maximize the final sum.

## Key Points
1. Uees Sieve of Eratosthense efficiently
2. Applies prefix sums for fast budget evaluation
3. Greedy selection ensure optimal result
4. Factorials are capped to avoid ovevrflow

## Algorithm Stratedy
1. Precompute primes up to 20 using a siee
2. Build a prefix array of prime counts
3. Precompute factorials up to 20
4. Greedily choose maximum valid factorial under budget
5. Replace the smallest array value with this factorial 