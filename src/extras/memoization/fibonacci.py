def fibonacci(n: int, memo: list[int]) -> int:
    if n <= 1:
        return 1

    if memo[n] != -1:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 1, memo)

    return memo[n]


if __name__ == '__main__':
    n = int(input())
    memo = [-1 for _ in range(n)]
    print(fibonacci(n, memo))
