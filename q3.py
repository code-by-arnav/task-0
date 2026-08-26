def is_prime(n):
    if n < 2:
        return False

    # The else block attached to a for loop runs only when the loop completes
    # fully without encountering a 'break'. If a break happens, else is skipped.
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        return True

    return False


print(is_prime(7))
print(is_prime(12))

N = int(input("Enter N: "))
print("Primes from 2 to", N, ":")
for num in range(2, N + 1):
    if is_prime(num):
        print(num, end=" ")