# Insertion sort
# Best Case : equals input N
# Worst Case: equals 1+2+..+N-1 O(N^2)

ar1 = [2,5,1,4,8,3,6,4]

ar2 = [6,4,2,1,7,8]

ar3 = [1,2,3,4,5,6]

ar4 = [9,7,4,3,2,1]

def sort(ar):
    for i in range(1, len(ar)): #take first unsorted element
        element = ar[i]
        pos = i
        while pos>=1 and ar[pos-1] > element: #push right till 0 or correct pos reached
            ar[pos-1], ar[pos] = element, ar[pos-1] #swap
            pos -= 1
            print(ar)

sort(ar4)
