# # # # # # # # nums=[1,2,3,4]
# # # # # # # # target=7
# # # # # # # # n=len(nums)
# # # # # # # # for i  in range(0,n-1):
# # # # # # # #     for j in range(i+1,n):
# # # # # # # #        if nums[i]+nums[j]==target:
# # # # # # # #            print(i,j)
# # # # # # # # ------------------------------optimal
# # # # # # # nums=[1,2,3,4]
# # # # # # # target=7
# # # # # # # n=len(nums)
# # # # # # # hash_map={}
# # # # # # # for i in range(0,n):
# # # # # # #     remaining=target-nums[i]
# # # # # # #     if remaining in hash_map:
# # # # # # #         print(hash_map[remaining],i)
# # # # # # #     hash_map[nums[i]]=i
# # # # # # #
# # # # # # # ---------------------subarray--------
# # # # # # nums=[4,3,2]

# # # # # # maxi=float("-inf")
# # # # # # n=len(nums)
# # # # # # for i in range(0,n):
# # # # # #     total = 0
# # # # # #     for j in range(i,n):
# # # # # #         total=total+nums[j]
# # # # # #         maxi=max(maxi,total)
# # # # # # print(maxi)
# # # # # # # tc-0(n(n+1))/2
# # # # # # ----------------------optimal----------
# # # # # # nums=[1,2,3,4,5]
# # # # # # n=len(nums)
# # # # # # maxi=float("-inf")
# # # # # # total=0
# # # # # # for i in range(0,n):
# # # # # #     total=total+nums[i]
# # # # # #     maxi=max(maxi,total)
# # # # # #     if total<0:
# # # # # #         total=0
# # # # # # print(maxi)
# # # # # # tc-0(n)
# # # # # # sc-0(1)
# # # # # # ---------------------rearrange of element-------------
# # # # # # nums=[5,10,-3,-1,-10,6]
# # # # # # pos=list(filter(lambda x:x>0,nums))
# # # # # # neg=list(filter(lambda x:x<0,nums))
# # # # # # for  i in range(len(pos)):
# # # # # #     nums[2*i]=pos[i]
# # # # # #     nums[2*i + 1]=neg[i]
# # # # # # print(nums)
# # # # # # -------------------optimal------------------------
# # # # nums=[5,10,-3,-1,-10,6]

# # # # n=len(nums)
# # # # result=[0]*n
# # # # posIndex,negIndex=0,1
# # # # for i in range(0,n):
# # # #     if nums[i]>=0:
# # # #         result[posIndex]=nums[i]
# # # #         posIndex+=2
# # # #     else:
# # # #         result[negIndex]=nums[i]
# # # #         negIndex+=2
# # # # print(result)
# # # # # sc(0(1))
# # # # # both 0(n) and 0(n) sc
# # # # ------------------------------longest consecutive sequence--------------------
# # # nums=[1,99,101,98,2,5,3,100]
# # # n=len(nums)
# # # max_count=0
# # # for i in range(0,n):
# # #     num=nums[i]
# # #     count=1
# # #     while num+1 in nums:
# # #         count+=1
# # #         num=num+1
# # #     max_count=max(max_count,count)
# # print(max_count)   
#     # 0(n2)
#     # sc=0(1)
# #     # --------------------my solution---------------------------not foor float -
nums = [1, 99, 101,98, 98, 2, 5, 3, 100, 1, 100]  # Added duplicates
nums.sort()  # Sort: [1, 1, 2, 3, 5, 98, 99, 100, 100, 101]
n = len(nums)
max_length = 1
longest_sequence = [nums[0]]
current_sequence = [nums[0]]
current_length = 1

for i in range(n - 1):
    diff = nums[i + 1] - nums[i]
    if diff == 1:  # Consecutive number, extend sequence
        current_length += 1
        current_sequence.append(nums[i + 1])
    elif diff > 1:  # Gap, start new sequence
        current_sequence = [nums[i + 1]]
        current_length = 1
    # If diff == 0 (duplicate), skip and continue
    if current_length > max_length:
        max_length = current_length
        longest_sequence = current_sequence[:]

print(f"Longest consecutive sequence: {longest_sequence}")
print(f"Length: {max_length}")
# #             # ---------------------------------optimise way---------------------------------------

