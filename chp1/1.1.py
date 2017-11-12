'''
Is Unique:
    Algorithm to determine if string has all unique characters.

Notes:
    Do this without using additional data structures.
        Otherwise we would just use sets.
'''

def isUnique(string):
    '''
    Precondition:
        string: string
    Postcondition:
        returns boolean
            true, if all unique 
            false, otherwise
    '''
    for i in range(0,len(string)):
        for j in range(i+1, len(string)):
            if (string[i] == string[j]):
                return False
        
    return True


def printTest(testInput):
    '''
    Precondition:
        testInput: string
    Postcondition:
        Prints out information. 
    '''
    print('Testing...', testInput, ':',isUnique(testInput))


def main():
    printTest('Hello')
    printTest('Bye')


if __name__ == '__main__':
    main()
