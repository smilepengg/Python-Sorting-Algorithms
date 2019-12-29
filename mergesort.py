#merge sort: ascending order

#merging function. all parameters are lists
def helper_merge_sort_1(u1,u2,u):
        cnt1=0
        cnt2=0
        #return value list
        rlist=[]
        #sorting of ascending order
        while cnt1<len(u1) and cnt2<len(u2):
                if u1[cnt1]<=u2[cnt2]:
                        rlist=rlist+[u1[cnt1]]
                        cnt1=cnt1+1
                        if cnt1==len(u1):
                                rlist=rlist+u2[cnt2:len(u2)]
                elif u2[cnt2]<u1[cnt1]:
                        rlist=rlist+[u2[cnt2]]
                        cnt2=cnt2+1
                        if cnt2==len(u2):
                                rlist=rlist+u1[cnt1:len(u1)]
        #changing the actual list with the values of the new list
        for i in range(0,len(rlist),1):
                u[i]=rlist[i]
        return True

#recursive function that does the merge sort. parameter is the list to be sorted
def helper_merge_sort_2(u):
        length=len(u)
        #base case for recursive calling
        if length==2:
                if u[1]<u[0]:
                        temp=u[0]
                        u[0]=u[1]
                        u[1]=temp
        #splitting the list in half (depends on if list length is even or odd)
        if length%2==0:
                half=length/2
                half=int(half)
        elif length%2==1:
                half=(length-1)/2
                half=int(half)
        #partition
        left=u[0:half]
        right=u[half:length]
        #recursive calling or splitting and merging
        if length>2:
                helper_merge_sort_2(left)
                helper_merge_sort_2(right)
                helper_merge_sort_1(left,right,u)
        return True

#merge sort function--returns True
def merge_sort(u):
        helper_merge_sort_2(u)
        return True

