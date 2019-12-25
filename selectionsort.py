#selection sort: sort list in ascending order

def selection_sort(u):
        #initialization of minimum value-always start at the 0th position
        current_min=u[0]
        current_item=u[0]
        min_pos=0
        cnt=0
        swap=True
        #stay in while loop if swapping was done previously (indication that sorting is not done!)
        while swap==True:
                for i in range (cnt,len(u),1):
                        current_item=u[i]
                        #check if the value at the current position in the list is smaller than the current smallest value that thas been encountered so far
                        if (current_item<current_min):
                        		#taking note of the new minimum value
                                current_min=current_item
                                min_pos=i
                #switching the current minimum value encoutered so far in the list
                temp=u[cnt]
                u[min_pos]=temp
                u[cnt]=current_min
                cnt=cnt+1
                if cnt==len(u):
                        swap=False
                else:
                        current_min=u[cnt]
                        current_item=u[cnt]
        return True
