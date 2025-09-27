# # # # from array import *
# # # # a1=array('i',[5,10,15,40])
# # # # for i in range(4):
# # # #     print(a1[i])
# # # # one class has exactly one class object but can have any nummber of instance object 
# # # # class Text: these are class object iske andar variable 
# # #     # t1=Text()
# # #     # t2=Text() instance object bnne ke baad
# # #     # t3=Text() these are all instancxe object
    
    
# # # # class Tests:
# # # #     x=5  where is x is in class not instance variable 
# # # #     def f1():
# # # #         print("hello")
# # # # t1=Tests()
# # # # t2=Tests()
# # # class Test:
# # #     def __init__(self):
# # #         self.a=5
# # #         self.b=6
# # # t1=Test() 
# # # t2=Test()
# # # print(t1.a,t1.b)
# # # print(t2.a,t2.b)
# # # # it call the init  method t1 and self both call same object a and b are instance object variable
# # # class Test:
# # #     def __init__(self,a,b):
# # #     # a and b is local variable and self.a and self.b is instance variable
# # #         self.a=a
# # #         self.b=b
# # # t1=Test(3,4) 
# # # t2=Test(5,6)
# # # print(t1.a,t1.b)
# # # print(t2.a,t2.b)
# # # # it call the init  method t1 and self both call same object a and b are instance object variable
# # class Test():
# #     x=5
# #     def __init__(self,a,b):
# #         self.a=a
# #         self.b=b
# #     def show(self):
# #         print(self.a,self.b)
# #     @staticmethod
# #     def f2():
# #         print("hello")
# #     @classmethod
# #     def f3(cls):
# #         print(cls.x)
# # t1=Test(3,4)
# # t2=Test(5,6)
# # t1.show()
# # t2.show()
# # Test.f3()
# # Test.f2()
        
# # statiic variable and instance variable 
# # class Employee:
# #     def __init__(self,empid=None,name=None,sallary=None):
# #         self.empid=empid
# #         self.name=name
# #         self.sallary=sallary
# #     def showempid(self,empid):
# #         self.empid=empid
# #     def showname(self,name):
# #         self.name=name
# #     def showsallary(self,sallary):
# #         self.sallary=sallary
# #     def getempid(self):
# #         return self.empid
# #     def getname(self):
# #         return self.name
# #     def getsallary(self):
# #         return self.sallary
# # e1=Employee()
# # e2=Employee(1,"Rahul",40000)
# # e1.showempid(2)
# # e1.showname("ROMESH")
# # e1.showsallary(50000)
# # print(e1.getempid(),e1.getname(),e1.getsallary())
# # print(e2.getempid(),e2.getname(),e2.getsallary())


    
        
# # ----------------------------------------------largest no in array------------------------------------------------
# # nums=[55,32,-97,99,4,67]
# # largest=nums[0]
# # n=len(nums)
# # for i in range(0,n):
# #     # largest=max(largest,nums[i])
# #     if nums[i]>largest:
# #         largest=nums[i]
# #         print(largest)
# # time complexity-0(n)
# # space complexity0(1)
# # ----------------------------------------------------find 2 largest----------------------
# # nums=[55,32,-97,99,4,67]
# # nums.sort()
# # n=len(nums)
# # print(nums[n-2])
# # # brute force solution
# # ----------------------------------------------------find 2 largest----------------------

# # nums = [55, 32, -97, 99, 4, 67]

# # largest = float("-inf")
# # s_largest = float("-inf")

# # for num in nums:
# #     if num > largest:
# #         s_largest = largest   # purana largest ab second largest ho jayega
# #         largest = num         # naya largest mil gaya
# #     elif num > s_largest and num != largest:
# #         s_largest = num       # update second largest

# # print("Largest:", largest)
# # print("Second Largest:", s_largest)
# # time complexit 0(n+n=0(2n))==0(n)
# # sc=0{1}
# # ----------------------------------------------------find 2 largest----------------------
# nums = [55, 32, -97, 99, 4, 67]
# largest=float("-inf")
# s_largest=float("-inf")
# n=len(nums)
# for i in range(0,n):
#     if nums[i]>largest:
#         s_largest=largest
#         largest=nums[i]
#     elif nums[i]>s_largest and nums[i]!=largest:
#         s_largest=nums[i]
# print(s_largest)
# # timme complexity-0(n)
# # sc-0(n)
# # ------------------------------Remove duplicate--------------------------------------------
# # brute force solution

nums=[1,2,2,1,1,2,3,4,9]
n=len(nums)
freq_map={}
for i in range(0,n):
    freq_map[nums[i]]=0
j=0
for k in freq_map:
    nums[j]=k
    j+=1
print(j)
#     # time complexity-0(2n)==0(n)
#     # sc-0(n)
#     # --------------------------optimal solution----------------------------
# # nums = [1,2,2,1,1,2,3]
# # nums.sort()   # ✅ पहले sort किया ताकि duplicates साथ-साथ आ जाएँ
# # n = len(nums)

# # if n == 1:
# #     print(1)
# # else:
# #     i = 0
# #     j = i + 1
# #     while j < n:
# #         if nums[j] != nums[i]:
# #             i += 1
# #             nums[i], nums[j] = nums[j], nums[i]
# #         j += 1

# #     print(i+1)          # ✅ unique count
# #       # ✅ unique elements
# # # tc=0(n)
# # # sc-0(1)
# # ---------------------------------------------------rotate a list----------------------------------------------
# nums = [5, -2, 3, 9, 0, 6, 10, 7]
# n = len(nums)

# temp = nums[n-1]   # last element store karo
# for i in range(n-2, -1, -1):   # last se shift karo
#     nums[i+1] = nums[i]
# nums[0] = temp     # pehle position pe last element daal do

# print(nums)   # rotated list print karo
# # you can use sliceing but if not # nums[:]=nums[-1]+nums[0:n-1] isme 0(1)+0(n-1) which is equal to 0(n) # sc(0(1))
# # ---------------------------------------------------rotate a list by k plCE----------------------------------------------
# nums = [3, 9, 3, 4, 5, 64]
# k = 3
# n = len(nums)

# rotations = k % n
# for _ in range(rotations):
# 0(r)
#     e = nums.pop()       # O(1)
#     nums.insert(0, e)    # O(n)

# print(nums)

    # --------------------------------------------------by slicing----------------------------------------------
# nums = [3, 9, 3, 4, 5, 64]
# n = len(nums)
# k = 3   # jitna rotate karna hai

# rotations = k % n
# nums[:] = nums[n-rotations:] + nums[:n-rotations]

# print(nums)

# : ke baad khali chod do agar ending me jana h 0(k)+0(n-k)==0(n)sc(0(n))
# --------------------------------------------------OPTIMAL_---------------------------------------
# nums = [3, 9, 3, 4, 5, 64]

# def reverse(nums, left, right):
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1

# n = len(nums)
# k = 5
# k = k % n   # in case k > n

# # Step 1: reverse last k elements
# reverse(nums, n-k, n-1)

# # Step 2: reverse first n-k elements
# reverse(nums, 0, n-k-1)

# # Step 3: reverse whole array
# reverse(nums, 0, n-1)

# print(nums)
