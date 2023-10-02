class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def binarySearch(self, arr, low, high, k):
        print("entered binary search func ")
        while(low<=high):
            m = int((low+high)/2)
            if k == arr[m]: return 1
            elif k < arr[m]: high = m-1
            else: low = m+1
        return -1

    def searchMatrix(self, A, B):
        n = len(A)
        m = len(A[0])
        if n ==1 and m==1 and A[0][0]==B:
            return 1
        if n == 1:
            return self.binarySearch(A[0], 0, m-1, B)
        low = 0
        high = n-1
        isPresent = -1
        while(low<=high):
            mid = int((low+high)/2)
            if B < A[mid][0]:
                high = mid-1
            if B> A[mid][m-1]:
                low=mid+1
            if A[mid][0] <= B and B <= A[mid][m-1]:
                arr = A[0]
                return self.binarySearch(A[mid],low=0, high=m-1, k=B)
        return isPresent

a = Solution()
ans = a.searchMatrix([[1,2,3,4],[11,12,13,14],[17,26,30,35]],27)
print("Ans: ",ans)