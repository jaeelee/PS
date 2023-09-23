def gcd(a:int, b:int):
    return int(gcd(b, a % b) if b else a)


def lcm(a:int, b:int):
    return int(a * b / gcd(a, b))


if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        N = int(input())
        X = [ int(i) for i in input().split(' ') if int(i) != 1]
        