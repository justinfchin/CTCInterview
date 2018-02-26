'''1.6 STRING COMPRESSION

Perform string compression using counts of repeated characters

'''
def compress(string):
    """ Returns string compression

    Args:
        str : string
    Returns:
        string with each count of consecutive characters if smaller than original string
    """
    # Declare variables
    temp = []
    count = 1
    # Iter
    for i in range(0,len(string)):
        print(i)
        if i+1 == len(string) or string[i] != string[i+1]:    # End of string or not equal 
            temp.append(string[i])
            temp.append(str(count))
            count = 1
        else:
            count += 1

    return ''.join(temp)

if __name__ == '__main__':
    print(compress('aabcccccaaa'))
