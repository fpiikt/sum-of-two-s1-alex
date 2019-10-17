"""
Автор: Емельянов А.А. группа №42552
Ссылка на сайт-портфолио: https://github.com/fpiikt/sum-of-two-s1-alex
Дополнительные комментарии по решению
Решение реализовано внутри метода sum
"""
def sum(d1, s1): #search indices of elements (d1) forming the sum(s1). Each combination used only once. Assert - not so good decision, but... 
    lst = []
    i = 0
    i1 = 0
    for i in range (len(d1)):
        for i1 in range (i, len(d1)):
            if d1[i] + d1[i1] == s1:
                ind = (i+1, i1+1)
                lst.append(ind)
        i1=+1
    i=+1
    return lst   

assert sum([1,2,3,4,5,6,7,8,9], 6) == [(1, 5), (2, 4), (3, 3)], 1 
assert sum([1,2,3], 4) == [(1, 3), (2, 2)], 1 
assert sum([100,1001,99,400], 500) == [(1, 4)], 1
assert sum([0.5,1,7,9,8.3], 17.3) == [(4, 5)], 1
assert sum([0.5,1,7,9,8.3], 17.2) == [(4, 5)], 0
assert sum([100,1001,99,400], 500) == [(1, 2)], 0
assert sum([1,2,3], 3) == [(1, 3), (1, 2)], 0 

