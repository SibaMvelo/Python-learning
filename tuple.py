def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    aTup = tuple(input('Enter a tuple: '))
    return aTup[::2]


print(oddTuples((1, 2, 3, 4, 5, 6, 7, 8)))
