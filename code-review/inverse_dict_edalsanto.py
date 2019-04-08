def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    https://github.com/EDalSanto/MIT-6.00.1x/blob/master/Final%20Exam/Inverse_Dict.py
    '''
    #create empty inverse dictionary
    # O(N) + O(N) , plus sorting is not working
    inverse = {}
    for elm in d.keys():
        if d[elm] in inverse:
            inverse[d[elm]].append(elm)
        else:
            inverse[d[elm]] = [elm]
    for val in inverse.values():
        val.sort()
    return inverse

if __name__ == "__main__":
    d =  {1:10, 4:40, 3:40}
    dInverse = dict_invert(d) 
    print(dInverse)
