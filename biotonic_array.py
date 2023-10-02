class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def binarySearchleft(self, A, l,h,k, p):
        while(l<=h):
            m = int((l+h)/2)
            if A[m] == k:
                return m
            elif k<A[m]:
                h=m-1
            else:
                l = m+1
        return -1
    def solve(self, A, B):
        n = len(A)
        l = 0
        h = n-1
        pos = -1
        while(l<=h):
            m = int((l+h)/2)
            if A[m-1]<A[m] and A[m]>A[m+1]:
                print("M ",m)
                break
            if A[m-1]<A[m] and A[m]<A[m+1]:
                l = m+1
            else:
                h=m-1
        pos = self.binarySearch(A, 0, m, B,m)
        if pos!=-1:return pos
        pos = self.binarySearch(A, m+1, n-1, B, m)
        return pos 

a = Solution()
ans = a.solve([1,2,3,4,5,6,7,9,10,20,19,18,17,16,15,14,13,12,11], 12)
print(ans)