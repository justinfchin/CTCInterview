'''1.5 ONE AWAY

Three types of edits on a string, insert, remove, replace.

Given two strings, check if they are one or 0 edits away.
'''

def oneaway(str1, str2):
    """ Determine if two strings are at most one edit away

    Args:
        str1, str2 : strings
    Returns:
        boolean; True if they are, else False
    """

    # Declare dictionary
    temp = {}

    # Populate dictionary
    for i in str1:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1

    numDiff = 0

    # Declare numDifference
    for i in str2:
        if i in temp:
            temp[i] -= 1
        else:
            numDiff += 1

    for values in temp.values():
        numDiff += values

    return numDiff <= 2
if __name__ == '__main__':
    print(oneaway('pale','ple'))
    print(oneaway('pales','pale'))
    print(oneaway('pale','bale'))
    print(oneaway('pale','bae'))

