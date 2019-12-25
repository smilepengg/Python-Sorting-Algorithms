#quick sort: first argument is the list, the second argument is the initial position, and the third argument is the final position of the list that is being sorted

#partition function (quick sort help)
def partition(u,ini,fin):
        #putting pivot value at the end of the list
        pIndex=fin
        pivot_val=u[fin]
        #finding first item from left that is larger than the pivot and first itme from right that is smaller than the pivot
        left_idx=ini
        right_idx=fin-1
        left_cnt=ini
        right_cnt=fin
        while right_idx>left_idx:
                #only swap the values of right and left index if it isnt the first iteration (dont want to put at the end or else it will swap even though the while statement is not true anymore)
                if left_cnt!=ini:
                        temp=u[left_idx]
                        u[left_idx]=u[right_idx]
                        u[right_idx]=temp
                #fiding left index
                for i in range (left_cnt,fin,1):
                        if (u[i]>pivot_val):
                                left_idx=i
                                left_cnt=left_cnt+1
                                break
                #finding right index
                for j in range (right_cnt-1,ini-1,-1):
                        if (u[j]<pivot_val):
                                right_idx=j
                                right_cnt=right_cnt-1
                                break
                #dont continue loop if the value at the right index is larger than the value at the left index
                if u[right_idx]>=u[left_idx]:
                        break
        #swap values of pivot and left ONLY if pivot value is less than the left index
        if u[fin]<u[left_idx]:
                temp=u[left_idx]
                u[left_idx]=u[fin]
                u[fin]=temp
                pIndex=left_idx
        return pIndex

#sorting algorithm function
def quick_sort(u,ini,fin):
        if ini<fin:
                #partitioning the list and sorting based on partition (this is recursive)
                pIndex=partition(u,ini,fin)
                quick_sort(u,ini,pIndex-1)
                quick_sort(u,pIndex+1,fin)
        return True


#u=[0,2,5,3,4,7,8]
#z=[12,1435,48,14,92,432]
#alist = [54,26,93,17,77,31,44,55,20]
#y=[12435,61542,356847,23,6,1,3,5,8,3]
#quick_sort(y,0,9)
#print(y)