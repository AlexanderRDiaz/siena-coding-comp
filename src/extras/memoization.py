def fibonacci(n):
    memo = [-1 for _ in range(n)]
    return _fibonacci_(n, memo)


def _fibonacci_(n, memo):
    if n <= 1:
        return 1

    if memo[n] != -1:
        return memo[n]

    memo[n] = _fibonacci_(n - 1, memo) + _fibonacci_(n - 1, memo)

    return memo[n]
