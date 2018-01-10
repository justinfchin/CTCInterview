# 1.1 - Is Unique:

task = 'TASK: Algorithm to determine if string has all unique characters.\n'

''' NOTES:

- Do this without using additional data structures.
    - Otherwise we would just use sets.

'''

def isUnique(string):
    '''
    Precondition:
        string: string
    Postcondition:
        Checks if string is unique.
        Returns: boolean
            false, if not string is unique 
            true, otherwise
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
        For testing the algorithm.  
    '''
    print('Testing...', testInput, ':',isUnique(testInput))


def main():
    print(task)
    printTest('Hello')
    printTest('Bye')


if __name__ == '__main__':
    main()
