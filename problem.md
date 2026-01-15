**Prime Factorial Array**

**Problem statement:**
You are given an array of integers A of length N and a budget B.
You may perform the following operation any number of times ( including zero ):
1. Choose an index i (1 <= i <= N) and an integer k >= A[i].
2. Replace A[i] with k! ( the factorial of k).
 
The cost of using k! is equal to the number of distinct prime numbers <= k.
The total cost of all operations must not exceed B.

**Your task is to mazimize the sum of the final array after performing zero or more operations under the budget constraint.**


**Input:**
 The first line contains two integers N and B ------ the array size and the budget
 (1 <=  N <= 2*10^5  ,  0 <= B <= 10^6).
The second line contains N integers A[1], A[2]……A[N] (1 <= A[i] <= 10^6).


**Output:**
Print a single integer the maximum sum of the array after performing the operatoins.