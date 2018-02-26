''' Write a method to replace all spaces in a string with '%20'. 

'''

def urlify(string,int):
    """ Replaces all spaces with '%20'

    Args:
        string : string
        int : integer indicating true length of the string
    Returns:
        returns string with all spaces replaced with '%20'
    """
    newString = ''

    for i in range(0,int):
        if string[i] == ' ':
            newString += '%20'
        else:
            newString += string[i]

    return newString


if __name__ == '__main__':
    print(urlify('Mr John Smith    ',13))
