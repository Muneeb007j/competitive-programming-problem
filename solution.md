## Problem Overview

You are given:

* An integer **N**: number of elements in an array
* An integer **B**: budget
* An array **A** of size **N**

The task is to:

1. Use a **prime-count budget** to determine the maximum factorial value that can be used.
2. Replace the **smallest element**of the array with that factorial value.
3. Output the resulting sum.

---

## Key Observations

* Only factorials up to **20!** are considered because factorial values grow very fast.
* The **cost** of choosing `k!` is defined as the **number of prime numbers ≤ k**.
* We must choose the **maximum `k`** such that the prime count does not exceed the budget **B**.

---

## Step-by-Step Approach

### 1. Input Reading

```python
N, B = map(int, input().split())
A = list(map(int, input().split()))
```

---

### 2. Prime Sieve (Up to 20)

We use the **Sieve of Eratosthenes** to mark prime numbers up to `MAX_K = 20`.

```python
for i in range(2, int(MAX_K ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, MAX_K + 1, i):
            prime[j] = False
```

This allows fast prime lookup.

---

### 3. Prime Cost Prefix Array

`count[k]` stores how many primes exist from `1` to `k`.

```python
count[k] = count[k - 1] + (1 if prime[k] else 0)
```

This makes budget checking efficient.

---

### 4. Factorial Precomputation

Factorials are precomputed up to `20!`:

```python
factorial[k] = factorial[k - 1] * k
```

---

### 5. Maximum Valid Factorial

We select the **largest `k`** such that:

```
count[k] ≤ B
```

This ensures the prime cost does not exceed the budget.

---

### 6. Final Calculation

* Remove the **smallest element** from the array
* Add the selected factorial

```python
total_sum - smallest + factorial[k_max]
```

---

## Final Output

The computed value is printed as the final answer.

---

## Time and Space Complexity

### Time Complexity

* Sieve: **O(MAX_K log log MAX_K)** (very small)
* Factorial + prefix computations: **O(MAX_K)**
* Overall: **O(N)** due to array operations

### Space Complexity

* Arrays for primes, factorials, and counts: **O(MAX_K)**

---

## Summary

* Efficient use of prefix sums and sieve
* Greedy choice of maximum factorial under budget
* Clean and optimal for given constraints

✔ Suitable for competitive programming
✔ Safe due to factorial limit (20)

---

**End of solution.md**
