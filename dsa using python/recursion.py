# # tail recursion
# # count=0
# # def func():
# #     global count
# #     if count==4:
# #         return
# #     print("Anirudh")
# #     count+=1
# #     func()
   
# # func()
# # head recursion

# # count=0
# # def func():
# #     global count
# #     if count==4:                                        TC-o(n+1)==o(n)
# #                                                         SC-o(n+1)==o(n)
# #         return 
# #     count+=1
# #     func()
# #     print("anirudh")    
# # func()                   

# # ----------------------------------------------Recursion using parameter----------------------------


# def func(x,n):
#     if n==0:
#         return
#     print(x)
#     func(x,n-1)
# func(15,4)
# # ---------------------------------------------------Print 1 to n by recursion----------------------------
# def func(i,n):
#     if i>n:
#         return
#     print(i)
#     func(i+1,n)
    
# func(1,4)
# # ---------------------------------------------------------1 to N tail recursion---------------------------
# # def func(i,N):
# #     if i>N:
# #         return
# #     func(i+1,N)
# #     print(i)
# # func(1,4)
# # -----------------------------------------------------------head recursion------------------------------------
# def func(N):
#     if N==0:
#         return
#     print(N)
#     func(N-1)
# func(4)
# --------------------------------Sum of 1 to n natural number -----------------------------------------
# def func(sum,i,N):
#      if i>N:
#          print(sum)
#          return
#      func(sum+i,i+1,N)
# func(0,1,4)
# # -------------------------------------------------------------------------------------------------------------
# # def func(N):
# #     if N >> 1:
# #         return 1
# #     return N + func(N - 1)

# # print(func(10))
# # ==================================================Factorial===========================================================
# # def factorial(n):
# #     if n==1 or n==0:
# #         return 1
# #     return n*factorial(n-1)
# # print(factorial(5))
# # =======================================================REVERSE OF ARRAY====================================
nums = [1, 2, 3, 4, 5, 6, 7, 8]

def func(nums, left, right):
    if left >= right:   # Base case: Stop when pointers meet or cross
        return
    nums[left], nums[right] = nums[right], nums[left]  # Swap elements
    func(nums, left + 1, right - 1)  # Move inward

def reverse_array(nums, l, r):
    func(nums, l, r)
    return nums

print(reverse_array(nums, 0, len(nums) - 1))

# # ============================PAlidrome================================
# # def is_palindrome(s):
# #     n = len(s)
# #     left = 0
# #     right = n - 1
# #     while left < right:
# #         if s[left] != s[right]:
# #             return False
# #         left += 1
# #         right -= 1
# #     return True
# # # time complexity 6 loop tc--0(n/2)----n
# # # sc--0(1)
# # s = "ANBCOOCBNA"
# # print(is_palindrome(s))
# # -----------------------------------as a recursion-----------------------

# # s = "ANBCOOCBNA"

# # def func(s, left, right):
# #     if left >= right:          # Base case: All characters checked
# #         return True
# #     if s[left] != s[right]:    # Mismatch found → Not a palindrome
# #         return False
# #     return func(s, left + 1, right - 1)  # Move towards the center

# # print(func(s, 0, len(s)-1))  # Call for the whole string
# # ==================================FIBONACCI SERIES=================================

# # class Student:
# #     def func(self, num):
# #         # Fibonacci base cases
# #         if num == 0:
# #             return 0
# #         elif num == 1:
# #             return 1
# #         # Recursive case
# #         return self.func(num-1) + self.func(num-2)

# #     def fib(self, n):
# #         return self.func(n)

# # # Example usage
# # obj = Student()
# # print(obj.fib(6))  # Output: 8 (0,1,1,2,3,5,8)
