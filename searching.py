# in an array every element occures twice except for 1. Find single element. 

arr = [1,2,3,1,2,3,4,8,9,9,4]
ans = arr[0]
for elem in arr[1:]:
    ans = ans ^ elem 
print(ans)