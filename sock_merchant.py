from __future__ import print_function

def main():
    number_of_socks = int(input().strip())
    colors_of_socks = sorted(map(int, input().strip().split(' ')))

    pairs = 0
    colors_of_socks.append('-1')

    i = 0

    while i < number_of_socks:
        if colors_of_socks[i] == colors_of_socks[i+1]:
            pairs += 1
            i+= 2
        else:
            i += 1

    print(pairs)

if __name__ == '__main__':
    main()

#Sample Test Case number_of_socks = 9, colors_of_socks = [10 20 20 10 10 30 50 10 20]