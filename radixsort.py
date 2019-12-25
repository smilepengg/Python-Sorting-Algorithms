#radix sort

def sortr(L):
        sorted_list=list(L)
        modulo=10;
        divide=1;
        max_num=-999999999999
        for i in range(0,len(L),1):
                if L[i]>max_num:
                        max_num=L[i]
        while True:
                #creating a hash table for each possible digits, ie 0,1,2,3,4,5,6,7,8,9
                rad=0
                hash_table=[[],[],[],[],[],[],[],[],[],[]]
                for element in sorted_list:
                        #calculating the hash index (where you would put the element based on the "last" digit)
                        hash_idx=element%modulo
                        hash_idx=hash_idx//divide
                        hash_table[hash_idx]=hash_table[hash_idx]+[element]
                #inserting in sorted_list
                for i in range (0,10,1):
                        for j in hash_table[i]:
                                sorted_list[rad]=j
                                rad=rad+1
                #breaking the loop if all the elements of the list are in the 0th index of the hash table bc it means that it has reached the highest "position" for the digits
                if modulo>max_num:
                        break
                #incrementing modulo and divide to evalute the next "position" of indexing
                modulo=modulo*10
                divide=divide*10
        return sorted_list
