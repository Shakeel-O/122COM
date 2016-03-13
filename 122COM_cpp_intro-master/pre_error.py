import sys

def main():
    bugs = 1

    for i in range(10):
        print( bugs, "little bugs in the code" )
        print( bugs, "little bugs" )
        print( "Take one down, patch it around" )
    
        bugs *= 2;

        print( bugs, "little bugs in the code..." )
        print()

    return 0

if __name__ == '__main__':
    sys.exit(main())