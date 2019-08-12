def print_formatted(number):
    # your code goes here
    w = len("{0:b}".format(number))
    num = number + 1
    for i in range(1,num):
        print ("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)