import numpy as np


def calculate_sum(n):
    result = n * (n + 1) // 2
    return result


if __name__ == '__main__':

    print("Enter positive integer number:")
    while True:
        try:
            N = int(input("\nN: "))
            if N > 10 ** 25:
                print("N must be <= 10^25")
                continue
            if N < 0:
                print("N cannot be negative")
                continue
            if N == 0:
                print("N cannot ne zero")
                continue
            result = calculate_sum(N)
            print(f"Result: {result}")
        except ValueError:
            print("Enter only integer number")
