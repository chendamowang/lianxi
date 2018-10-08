"""
heap-sort
"""
def heap_sort(lst):
    """
    contrust a max-heap based on given array ranging from the last non-leaf node to root node
    in python:non-leaf node number reduce from half of the last index of the array minus 1 to 0
    """
    for i in range((len(lst))/2,-1,-1):
        heap_adjust(lst,i,len(lst))

    for j in range(len(lst)-1, 0, -1):
        """
        swap the top of the heap and the last of unordered part ,if we iterate
        k times ,then we get a array whose the last k elements is the top k
        """
        # print lst[0]
        lst[j], lst[0]=lst[0], lst[j]
        heap_adjust(lst, 0, j)

def heap_adjust(lst,s,m):
    """
    re-contruct a max-heap from s to m based on array
    """
    i = 2*s+1 #the left node of the s
    temp=lst[s]
    while i < m:
        if (i+1 < m) and (lst[i] < lst[i+1]):
            i = i+1
        if temp >= lst[i]:
            break
        #else:
        lst[s] = lst[i]
        s = i
        i=i*2+1
        # print lst
    lst[s]=temp

if __name__=="__main__":
    a=[50,10,90,30,70,40,80,60,20]

    heap_sort(a)

    print a
