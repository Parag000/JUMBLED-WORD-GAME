def smallest(numList):#TO FIND SMALLEST NUMBER
    n=len(numList)
    smallest_number=numList[0]#TAKING DUMMY VALUE
    i=1
    while (i<n):
        if numList[i]>smallest_number:
            smallest_number=numList[i]
            i+=1
    return smallest_number

def my_sort(list):#TO SORT IT IN DESCENDING ORDER
    k=len(list)
    sort_list=[]
    x=1
    while (x<=k):
        print(*list) # in-built function
        sm = smallest(list) # user function
        sort_list.append(sm)
        list.remove(sm)
        x+=1
    print(*sort_list)

my_sort([1,2,3,4,5,6])
