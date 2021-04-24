def insertion(li):
    for i in range(1,len(li)):
        j=i-1
        nxt=li[i]
        while li[j]>nxt and j>=0:
            li[j+1]=li[j]
            j=j-1
        li[j+1]=nxt

li=[12,5,4,626,64,6,9,62,46,1,461,16,49]
insertion(li)
print(li)