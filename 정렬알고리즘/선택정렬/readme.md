```python
#오름차순
arr=[3,7,4,9,10,223,111,23,2,39]

for i in range(0,len(arr)-1):
    min_idx=i
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            min_idx=j

    tem=arr[i]
    arr[i]=arr[min_idx]
    arr[min_idx]=tem
print(arr) # [2, 3, 4, 7, 9, 39, 10, 23, 111, 223]

#내림차순
arr=[3,7,4,9,10,223,111,23,2,39]

for i in range(0,len(arr)-1):
    max_idx=i
    for j in range(i+1,len(arr)):
        if(arr[max_idx]<arr[j]):
            max_idx=j

    tem=arr[i]
    arr[i]=arr[max_idx]
    arr[max_idx]=tem
print(arr) # [223, 111, 39, 23, 10, 9, 7, 4, 3, 2]



```