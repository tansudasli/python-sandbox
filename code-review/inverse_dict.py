def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''

    #O(N) + O(N) + O(N) = 3 O(N) bad !!
    keys=[]
    values=[]
    
    result={}
    for i in d:
        keys.append([i])
    for i in d:
        values.append(d[i])
       
    i = -1
    for v in values:
        i+=1
        result[v] = result.get(v,[]) + keys[i]
    return result        

if __name__ == "__main__":
    d =  {1:10, 4:40, 3:40}
    dInverse = dict_invert(d) 
    print(dInverse)    