import sys
import collections

def subsets(nums):
    temp = []
    result = []
    result.append([])
    size = len(nums)
    backtrack(nums, temp, result, 0, size)
    result.remove([])
    return result
    
def backtrack(nums, temp, result, start, size):
    if start == size: return
    for i in range(start, size):
        temp.append(nums[i])
        result.append(temp[:])
        backtrack(nums, temp, result, i + 1, size)
        temp.pop()  


def apriori(D, support):
    
    C = {}
    for T in D:
        for I in T:
            if I in C:
                C[I] += 1
            else:
                C[I] = 1

    _keys1 = C.keys()

    keys1 = []
    for i in _keys1:
        keys1.append([i])


    cutKeys1 = []

    for k in keys1:
        if C[k[0]] >= support:
            cutKeys1.append(k)

    cutKeys1.sort()

    keys = cutKeys1 

    key = []
    for k in keys:
        key.append(k[0])

    dict = {}

    all_sets = subsets(key)

    for set in all_sets:
        for seq in D:
            flag = True
            for character in set:
                if character not in seq:
                    flag = False
                    break
            if flag:
                k = tuple(set)
                if k not in dict:
                    dict[k] = 1
                else:
                    dict[k] += 1

    result = {}

    for k in dict:
        if dict[k] >= support:
            newk = dict[k]
            if newk not in result:
                result[newk] = []
                result[newk].append(k)
            else:
                result[newk].append(k)

    sorted_result = {}
    for k in sorted(result)[::-1]:
        sorted_result[k] = result[k]
   
    for k in sorted_result:
        sorted_result[k] = sorted(sorted_result[k], key=len)

    result = {}
    
    for k in sorted_result:
        result[k] = []
        for val in sorted_result[k]:
            result[k].append(list(val))

    for k in result:
        result[k] = sorted(result[k])

    for key in result:
         for val in result[key]:
            print(key,'[', end='') 
            for i in range(len(val)):
                if i == len(val) - 1:
                    print(val[i], end='')
                else:
                    print(val[i], '', end='')
            print(']')
    print()

    all_data = []
    for k in result:
        all_data += result[k]

    reverse = {}

    for key in result:
        for val in result[key]:
            reverse[tuple(val)] = key

    closep = []
    maxp = []

    key = [k[0] for k in keys]
    
    for l in all_data:
        select = True
        for k in key:
            if k not in l:
                temp = l + [k]
                temp = sorted(temp)
                if tuple(temp) in reverse and \
                  reverse[tuple(temp)] >= reverse[tuple(l)]:
                    select = False
        if select == True:
            if (l, reverse[tuple(l)]) not in closep:
                closep.append((l, reverse[tuple(l)]))

    close = {}
    for c in closep:
        if c[1] not in close:
            close[c[1]] = []
        close[c[1]].append(c[0])

    for key in close:
         for val in close[key]:
            print(key,'[', end='') 
            for i in range(len(val)):
                if i == len(val) - 1:
                    print(val[i], end='')
                else:
                    print(val[i], '', end='')
            print(']')
    print()


    key = [k[0] for k in keys]

    for l in all_data:
        select = True
        for k in key:
            if k not in l:
                temp = l + [k]
                temp = sorted(temp)
                if tuple(temp) in reverse:
                    select = False
        if select == True:
            if (l, reverse[tuple(l)]) not in maxp:
                maxp.append((l, reverse[tuple(l)]))
    
    m = {}
    for c in maxp:
        if c[1] not in m:
            m[c[1]] = []
        m[c[1]].append(c[0])
    
    for key in m:
        for val in m[key]:
            print(key,'[', end='') 
            for i in range(len(val)):
                if i == len(val) - 1:
                    print(val[i], end='')
                else:
                    print(val[i], '', end='')
            print(']')


D = [['data','mining'],['frequent','pattern', 'mining'], \
     ['mining','frequent','patterns', 'from', 'the', 'transaction', 'dataset'],  \
     ['closed', 'and', 'maximal', 'pattern', 'mining']]
apriori(D, 2)

