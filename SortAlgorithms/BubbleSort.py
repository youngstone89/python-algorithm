#Unoprimized bubble sort algorithms, simply swapping adjacent elements if they are in wrong order.
def bubbleSort(arr):
    # Assign the length of passed-in array to the variable n.
    n = len(arr);

    # Traverse through all array elements
    for i in range(n):

        # Last i Elemetns are already in place
        for j in range(0,n-(i+1)):
            print('i,j,j+1>>',i,j,j+1);
            if arr[j]> arr[j+1] :
                arr[j], arr[j+1] = arr [j+1], arr[j]

            print(arr);




arr = [64, 34, 25, 12, 22, 11, 90]

#Length = 7
#First i = 0
#First j = 0, Range(0,6)
#j=0, j+1 = 1
#j=1, j+1 = 2
#j=2, j+1 = 3
#j=3, j+1 = 4
#j=4, j+1 = 5
#j=5, j+1 = 6

bubbleSort(arr);

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])


#Optimized bubble sort
def optimalBublbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True


        if swapped == False:
            break

arr = [64, 34, 25, 12, 22, 11, 90]

optimalBublbleSort(arr)

print ("Sorted array :")
for i in range(len(arr)):
    print ("%d" %arr[i], end=" ")



sortedArr = [1,2,3,4,5,6,7]

optimalBublbleSort(sortedArr)
