'''1.4 Palindrome Permutation

Given a string, check if it is a permutation of a palindrome. 
'''

def isPalindrome(string):
    """ Checks if string is palindrome

    Args:
        string : string
    Returns:
        boolean; True if is palindrome, else False
    """
    # Remove Spaces
    string = string.replace(' ','')

    # Declare dictionary
    temp = {}

    # Load dictionary
    for i in string:
        if i in temp:
            temp[i] += 1
        else: 
            temp[i] = 1

    count = 0

    # Make sure at most only 1 not divisible by 2
    for values in temp.values():
        if values % 2 != 0:
            count +=1

    # Check
    if count > 1:
        return False

    return True

if __name__ == '__main__':
    print(isPalindrome('tact coa'))
    print(isPalindrome('atco cta'))
    print(isPalindrome('hi'))
