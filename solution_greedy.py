import sys 


input = sys.stdin.readline

def solution():
        # userinputs  
    N ,B = map(int, input().split())
    A = list(map(int, input().split()))

    # maximun number of k( faastorials)
    MAX_K =20

    # Sieve methord(To count prime)
    prime = [True] * (MAX_K + 1)
    prime[0] = prime[1] = False  # 0 and 1 are not prime

    for i in range(2 , int(MAX_K ** 0.5) + 1):
        if prime[i]:
            for j in range( i * i, MAX_K + 1, i):
                prime[j] = False


    # Finding cost ( prime count(π(k)))

    count = [0] * (MAX_K + 1)
    for k in range(1, MAX_K+1):
        count[k] = count[k - 1] + (1 if prime[k] else 0)

    # Factorial
    factorial = [1] * (MAX_K + 1)
    for k in range(1, MAX_K + 1):
        factorial[k] = factorial[k - 1] * k


    # 0/1 knapsack 
    dp = [0] * (B+1)
    for k in range(1, MAX_K + 1):
        cost = count[k]
        value = factorial[k]
        for b in range(B, cost -1, -1):
            dp[b] = max(dp[b], value)

    best_factorial = max(dp)
    total_sum = sum(A)
    smallest = min(A)

    result = total_sum - smallest + best_factorial
    print(result)

if __name__ == "__main__":
    solution()



# complexity O(N + B)    