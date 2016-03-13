import sys

def main():
    userinputs = []

    while len(userinputs) < 5:
        try:
            ui = int(input('Enter integer:'))
            userinputs.append(ui)
        except ValueError:
            print('Not an integer')
        
    for i in range(len(userinputs)-1, -1, -1):
        print( 'number', i+1, 'is', userinputs[i] )

if __name__ == '__main__':
    sys.exit(main())