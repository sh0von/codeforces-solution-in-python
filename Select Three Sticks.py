class Solution:
   def minMoves2(self, nums):
      nums.sort()
      counter = 0
      for i in nums:
         counter += abs(i-nums[len(nums)//2])
      return counter
ob1 = Solution()
T=int(input())
for i in range(T):
    n=int(input())
    arr=list(map(int, input().strip().split()))[:n]    
    print(ob1.minMoves2(arr))