# # # # # # # # nums=[1,3,2,5,6,7,0,2,0]
# # # # # # # # n=len(nums)
# # # # # # # # temp=[]
# # # # # # # # for i in range(0,n):
# # # # # # # #     if nums[i]!=0:
# # # # # # # #         temp.append(nums[i])
# # # # # # # # nz=len(temp)
# # # # # # # # for i in range(0,nz):
# # # # # # # #     nums[i]=temp[i]
# # # # # # # # for i in range(nz,n):
# # # # # # # #     nums[i]=0
# # # # # # # # print(nums)
# # # # # # #     # time complexity-0(2n)==0(n)
# # # # # # #     # space compleity=0(n)
# # # # # # #     # ----------------------------optimal solution-------
# # # # # # # # def moveZeroes(nums):
# # # # # # # #     if len(nums) <= 1:
# # # # # # # #         return
    
# # # # # # # #     i = 0
# # # # # # # #     while i < len(nums) and nums[i] != 0:
# # # # # # # #         i += 1
    
# # # # # # # #     # agar saare non-zero hain
# # # # # # # #     if i == len(nums):
# # # # # # # #         return
    
# # # # # # # #     j = i + 1
# # # # # # # #     while j < len(nums):
# # # # # # # #         if nums[j] != 0:
# # # # # # # #             nums[i], nums[j] = nums[j], nums[i]
# # # # # # # #             i += 1
# # # # # # # #         j += 1

# # # # # # # # nums = [1, 2, 3, 4, 6, 7, 0, 7, 0]
# # # # # # # # moveZeroes(nums)
# # # # # # # # print(nums)   # [1, 2, 3, 4, 6, 7, 7, 0, 0]

# # # # # # # # # tc-0(n)
# # # # # # # # # sc-0(1)
# # # # # # # # -----------------------------------------------
# # # # # # # # linear search
# # # # # # # def linear_search(nums):
   
# # # # # # #     target=5
# # # # # # #     n=len(nums)
# # # # # # #     for i in range(0,n):
# # # # # # #         if nums[i]==target:
# # # # # # #             return i 
# # # # # # #     return -1
# # # # # # # nums=[1,2,3,4,5,6,7,8]
# # # # # # # print(linear_search(nums))

       
# # # # # #     # ----------------------------Merge 2 sorted array---------------------
# # # # # # def union_sorted(nums1, nums2):
# # # # # #     result = []
# # # # # #     n = len(nums1)
# # # # # #     m = len(nums2)
# # # # # #     i, j = 0, 0
    
# # # # # #     while i < n and j < m:
# # # # # #         if nums1[i] <= nums2[j]:
# # # # # #             if len(result) == 0 or result[-1] != nums1[i]:
# # # # # #                 result.append(nums1[i])
# # # # # #             i += 1
# # # # # #         else:
# # # # # #             if len(result) == 0 or result[-1] != nums2[j]:
# # # # # #                 result.append(nums2[j])
# # # # # #             j += 1
    
# # # # # #     # Add remaining elements
# # # # # #     while i < n:
# # # # # #         if result[-1] != nums1[i]:
# # # # # #             result.append(nums1[i])
# # # # # #         i += 1
    
# # # # # #     while j < m:
# # # # # #         if result[-1] != nums2[j]:
# # # # # #             result.append(nums2[j])
# # # # # #         j += 1
    
# # # # # #     return result


# # # # # # nums1 = [1,1,1,2,4,6,7]
# # # # # # nums2 = [1,2,3,4,6,8]
# # # # # # print(union_sorted(nums1, nums2))  
# # # # # # # Output: [1, 2, 3, 4, 6, 7, 8]
# # # # # # # tc-0(n+m)
# # # # # # # sc-0(1)
# # # # # #             #   sc worst case o(m+n)

# # # # # # --------------------find missing number in array---------------
# # # # # # brute force solution
# # # # # nums=[0,1,2,3,4,5,6,7]
# # # # # n=len(nums)
# # # # # for i in range(0,n+1):
# # # # #     if i not in nums:
# # # # #         print(i)
        
# # # #     tc=0(n^2)
# # # #     sc=0(1)
# # # # --------------------------better-------------
# # # nums=[0,1,2,3,4,5,6,7]
# # # freq={}
# # # n=len(nums)
# # # for i in range(0,n+1):
# # #     freq[i]=0
# # # for num in nums:
# # #     freq[num]=1
# # # for k,v in freq.items():
# # #     if v==0:
# # #         print(k)
# # #         # tc=0(3n)
# # #         # sc-0(n)
# # # ---------------------optimal solution-------
# # nums=[9,6,4,2,3,5,7,0,1]
# # n=len(nums)
# # # subb ka sum
# # print(n*(n+1)//2-sum(nums))
# # # tc=0(n)
# # sc-0(1)
# # -----------------max consecutive once----------------
# nums=[1,1,0,1,0,1,1,1,1,0,1,1]
# n=len(nums)
# count=0
# max_count=0
# for i in range(0,n):
#     if nums[i]==1:
#         count+=1
#     else:
#         max_count=max(max_count,count)
#         count=0
# print (max(max_count,count))
# # tc-0(n)
# # sc-0(1)