# 

def find_triplets(arr, n):
    # two pointer
    arr.sort()
    out = []
    for i in range(n-2):
        print(f"checking for {i}")
        j = i+1
        k = n-1
        while(j<k):
            print(" j & k", j, k)
            if (arr[i]+arr[j]+arr[k]) == 0:
                out.append((arr[i], arr[j], arr[k]))
                j+=1
                k-=1
            elif (arr[i]+arr[j]+arr[k]) < 0:
                j+=1
            else: 
                k-=1
        return out
if __name__ == '__main__':
    print("execution start")
    arr = [0, -1, 1, -1, 2, 4]
    # ans = [(-1, -1, 2), (-1, 0, 1)]
    out = find_triplets(arr, len(arr))
    print(out)


