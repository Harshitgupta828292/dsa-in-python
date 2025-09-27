# # n=5873
# # num=n
# # while num>0:
# #     last_digit=num%10
# #     print(last_digit)
# #     num=num//10
# # # --------------------------------------------------------question 2_---------------------------
# # n=2883
# # num=n
# # while num>0:
# #     last_digit=num%10
# #     print(last_digit)
# #     num=num//10
# # -------------------------------------------------------question 3--------------
# # n=5432
# # l=str(n)[::-1]
# # for digit in l :
# #   print(digit)
# # ------------------------------------------------PALINDROME------------------------
# # n = 121
# # num = n
# # result = 0
#
# # while num > 0:
# #     lcd = num % 10
# #     result = (result * 10) + lcd
# #     num = num // 10
#
# # if n == result:
# #     print("Palindrome")
# # else:
# #     print("Not Palindrome")
#
# # ----------------------------------------------------------------------------------------------------------------------
# def is_palindrome(n):
#
#     return str(n) == str(n)[::-1]
#
# # Define the range
# start = 1
# end = 1000
#
# print("Palindrome numbers between", start, "and", end, "are:")
# for num in range(start, end + 1):
#     if is_palindrome(num):
#         print(num, end=' ')
# # -----------------------------------------------------------------count the number of digits--------------------------
# count=0
# n=5873
# num=n
# while num>0:
#     count+=1
#
#
#     num=num//10
# print(count)
# # --------------------------------------------SMART APPROACH--------------------------
from math import *
def countdigit(num):
    return int(log10(num)+1)
print(countdigit(5873))
#     # ----------------------------------Armstrong number--------------------------------
#
#
# n=121
# num=n
#
# total=0
# node=len(str(n))
# while num>0:
#     last_digit=num%10
#     total=total+(last_digit**node)
#     num=num//10
# print(total)
#
#         # -------------------------------------print factor-----------------------------------------------
# # a=int(input("enter the number "))
# # i=1
# # while a>=i:
# #     if a%i==0:
# #         print(i)
# #     i=i+1
# # ------------------------------------------STORE FREQUESNCY IN LIST-----------------------------------------
# nums=[1,2,2,1,3,443,36,6,3,5]
# freq_map={}
# for i in range(0,len(nums)):
#     if nums[i] in freq_map:
#         freq_map[nums[i]]+=1
#
#     else:
#         freq_map[nums[i]]=1
#
# print(freq_map[443])
# # ------------------------------------------------------METHOD 2------------------------------------------------------
nums = [1, 2, 3, 3, 2, 32, 43, 4211, 1]
hash_map = {}
n = len(nums)

for i in range(0, n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0)+1
print(hash_map)