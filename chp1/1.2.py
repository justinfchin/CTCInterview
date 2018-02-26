# 1.2 - Check Permutation:

task = "TASK: Determine if 2 strings are permutations of one another\n"

''' NOTES

'''

def checkPermutation(str1, str2):
    ''' Check is strings are permutations of one another

    Args:
        str1, str2: strings
    Returns:
        boolean; True if they are permutations, else False
    '''
    # Create a Dictionary
    temp = {}

    # Population Dictionary with str1
    for i in str1:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1

    # Check str2 in str1
    for i in str2:
        if i in temp:
            temp[i] -= 1
        else:
            return False

    # Make sure all values are zero
    for value in temp.values():
        if value != 0:
            return False
    
    return True

if __name__ == '__main__':
    print(checkPermutation('god','dog'))
    print(checkPermutation('godd','dog'))
