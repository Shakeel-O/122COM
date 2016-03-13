import sys

def main():
    a = 0
    b = 1

    for i in range(40):
        print('%d %d' % (i,b))

        c = a + b
        a = b
        b = c

if __name__ == '__main__':
    sys.exit(main())