def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # O(N)
    dInverse = {}
    for k,v in d.items():
        if v in dInverse:
            dInverse[v].append(k)
        else:        
            dInverse[v] = [k] #critical part k: [v]

    return dInverse

if __name__ == "__main__":
    d =  {1:10, 4:40, 3:30}
    dInverse = dict_invert(d) 
    print(dInverse)      