def q1(lst):
    #sort the list first
    lst.sort()
    print(lst)
    prev=None
    #ensuring the list is in accending value
    for elem in lst:
        if elem>= 0: #dont bother checking negative integer
            if prev ==None: #initialize the prev value
                prev=elem
            elif prev+1!=elem: #ensuring is concurrent numbers
                return prev+1
            prev=elem
def q2(n):
    sequence=[0,0, 3, 3, 6, 9, 15, 24, 39, 63, 102, 165]
    if n > len(sequence)-1: #if the n value is not in the initial generated number
        #the sequence of the number is first number + second number
        first=sequence[-1]
        second=sequence[-2]
        ans=0 #the total of first + second
        for num in range (len(sequence),n+1): # generate the sequence till n
            ans=first+second
            second=first
            first=ans
        return ans
    else: #if n value already generated return value in that index
        return sequence[n]

def q3(lst):
    retlst=[]
    for item in lst:
        item=item.upper()
        if item not in retlst:
            retlst.append(item)
    retlst.sort()
    print(retlst)
    return retlst




if __name__ == '__main__':
    lst=[2, 3, -7,6, 8, 1, -10, 15, -35]
    print(q1(lst))
    print(q2(7))
    lst=["Panasonic", "pensonic", "panasonic" , "Haier", "electrolux " , "Electrolux"]
    q3(lst)