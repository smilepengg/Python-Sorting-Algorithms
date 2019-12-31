#heap sort: ascending order

#max heapify-->max heap is needed to sort in ascending order. parameter (u) is a list.
def heapify(u):
        cnt=0
        #defining the limit variable. the limit variable is the number of levels in the heap/tree structure
        if len(u)%2==0:
                limit=len(u)/2
        elif len(u)%2==1:
                limit=(len(u)+1)/2
        #beginning of sorting/heapifying
        while cnt<(limit):
                for i in range(len(u)-1,0,-2):
                        #defining parent and sibling value in the heap structure of list values (depends on odd or even number of values in list u)
                        if i%2==0:
                                parent=(i-2)/2
                                parent=int(parent)
                                sibling=i-1
                        elif i%2==1:
                                parent=(i-1)/2
                                parent=int(parent)
                                if i==len(u)-1:
                                        sibling=i
                                else:
                                        #bc you cant have nonetype as a indice so need to compare with itself
                                        sibling=i+1
                        #if parent node is smaller than one of it's children, then swapping of value needs to be done
                        if (u[parent]<u[i]) or (u[parent]<u[sibling]):
                                if u[i]>u[sibling]:
                                        temp=u[parent]
                                        u[parent]=u[i]
                                        u[i]=temp
                                else:
                                        temp=u[parent]
                                        u[parent]=u[sibling]
                                        u[sibling]=temp
                cnt=cnt+1
        return True

#function that will restore the max heap structure (ex: needed when an item is removed from the heap, etc)
def reheapify(u,end):
        #copying over original list
        store=list(u)
        #"removing" first value of the heap and then moving the last value of the heap to the top of the heap
        temp=store[0]
        store[0]=store[end]
        store=store[0:end]
        #restoring the heap structure since it was just modified with the previous swapping
        heapify(store)
        for i in range(0,len(store),1):
                u[i]=store[i]
        return True

#heap sort function
def heap_sort(u):
        store=list(u)
        #creating a max heap
        heapify(store)
        accum=[]
        #keep removing the biggest value from the max heap (will be the 0th value of the heap) and putting it into another list
        for i in range(0,len(u),1):
                accum=[store[0]]+accum
                #restoring max heap properties
                reheapify(store,len(store)-1)
                if len(store)==2:
                        accum=[store[0]+store[1]]+accum
                        break
        #setting items of original list to the new sorted list
        for k in range (0,len(u),1):
                u[k]=accum[k]
        return True
