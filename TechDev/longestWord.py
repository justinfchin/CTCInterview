'''
Problem:
    - given string S and set of words D, find the longest word W in D that is a subsequence of S
    - W is a subsequence of S if some number of characters (possibly 0) can be deleted from S to form W without reording the remaining characters
    - D can be in any format, list, hashtable, prefix tree, etc. 
'''

def lw(S,D):
    """
    Args:
        S : string
        D : set of words in any format (list, hashtable, prefix tree, etc.)
    Returns:
        W : string
            the longest word in D that is a subsequence of S

    Examples:
        S = 'abppplee'
        D = {'able', 'ale', 'apple', 'bale', 'kangaroo'}
        W = 'apple'
    """
    # Idea: two indexes, and check that each char in each word in D is in S in the correct order. 
        # if it is in S, len and check if larger than old stored len

    wlen = -1
    W = ''

    for word in D:
        j = 0 # D word index
        for i in range(0,len(S)):
            # Done checking word
            if j == len(word)-1:
                # Make this new W if len is larger than old
                if len(W) < len(word):
                    W = word
                break
            # Check each letter in the word
            if S[i] == word[j]:
                j += 1
                
    return W

if __name__ == '__main__':
    S = 'abppplee'
    D = {'able','ale','apple','bale','kangaroo'}
    print(lw(S,D))
