import math


def is_prime(i, ret):
    sqrt = int(math.sqrt(i))
    for prime in ret:
        if i % prime == 0:
            return False
        if prime > sqrt:
            return True


def get_primes(m):
    ret = [2]
    for i in range(3, m):
        if is_prime(i, ret):
            ret.append(i)
    return ret


def get_val(param, primes):
    res = 1
    while param != 1:
        if is_prime(param, primes):
            res *= (param + 1)
            param = 1
        else:
            prime = None
            for sm_prime in primes:
                if param % sm_prime == 0:
                    prime = sm_prime
                    break
            x = 1
            while param % prime == 0:
                x *= prime
                param = param // prime
            res *= ((x * prime - 1) // (prime - 1))
    return res


def main():
    primes = get_primes(1898)

    # res = smallest nr which has the sum of divisors >= 3600000

    for i in range(1, 600000):
        if i % 5000 == 0:
            print(i)
        if get_val(6 * i, primes) >= 3600000:
            nr = 6 * i
            break

    print('Part One: ', nr)


if __name__ == "__main__":
    main()
