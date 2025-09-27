# --------------------------------------------------SELECTION SORT--------------------------------------------------
# def selection_sort(nums):
#     n = len(nums)
#     for i in range(n):
#         min_index = i
#         for j in range(i+1, n):
#             if nums[j] < nums[min_index]:
#                 min_index = j
#         # swap inside the outer loop
#         nums[i], nums[min_index] = nums[min_index], nums[i]
       
    
# # Example usage time complexity-------0(n(N+1))/2------0(n2)
# # sc-0(1)
# nums=[1,2,4,6,6,2]
# selection_sort(nums)
# print(nums)  # Output: [5, 6, 7, 8, 9]
# -------------------------------------------------------Bubble sort---------------------------------------------------
# nums=[5,1,2,34,5]
# n=len(nums)
# for i in range(n-2,-1,-1):
#     for j in range(0,i+1):
#         if nums[j]>nums[j+1]:
#             nums[j],nums[j+1]=nums[j+1],nums[j]       
# tc-0(n(n+1))/2----0(n2)
                                                        #  sc--0(N)(worst case)
                                                        # (best case)-
                                                        # tc-0(n)and sc-0(1)
                                                        
# print(nums)
# ---------------------------------------------------best case ---------------------------------------------------------
# nums=[1,2,3,4,5]
# n=len(nums)

# for i in range(n-1,-1,-1):
#     is_swap=False
    
#     for j in range(0,i):
#         if nums[j]>nums[j+1]:
#             nums[j],nums[j+1]=nums[j+1],nums[j]
#             is_swap=True
#     if is_swap==False:
#         break
# print(nums)
# -------------------------------------------------------Insertion sort-xxxxxxxxx--------------------------------------------------
# nums=[3,5,6,8,4]
# n=len(nums)
# for i in range(1,n):
#     key=nums[i]
#     j=i-1
#     while j>=0 and nums[j]>key:
#         nums[j+1]=nums[j]
#         j-=1
#     nums[j+1]=key
# print(nums)

                # tc---0(n(n+1))/2---0(n2)
                # sc-0(1)
# ------------------------------------------------------MERGE SORT------------------------------------------------------------------
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left_arr = arr[:mid]      # Fixed
#     right_arr = arr[mid:]  
#     # Fixed

#     left = merge_sort(left_arr)
#     right = merge_sort(right_arr)

#     return merge_array(left, right)


# def merge_array(left, right):
#     result = []
#     i, j = 0, 0
#     n, m = len(left), len(right)

#     while i < n and j < m:
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
            

#     # Add remaining elements
#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result


# Example
# nums = [5, 2, 9, 1, 5, 6]
# print(merge_sort(nums))
# time complexity-0(log2(n*n))
# space complexity-0(n)
# --------------------------------------------------------Quick sort--------------------------------------------------

# nums = [3, 1, 2, 4, 6, 7, 8]

# def quick_sort(nums, low, high):
#     if low < high:  # Base case
#         p_ind = partition(nums, low, high)  # Fixed variable name
#         quick_sort(nums, low, p_ind - 1)
#         quick_sort(nums, p_ind + 1, high)


# def partition(nums, low, high):
#     pivot = nums[low]
#     i = low
#     j = high

#     while i < j:
#         while nums[i] <= pivot and i <= high - 1:
#             i += 1
#         while nums[j] > pivot and j >= low + 1:
#             j -= 1
#         if i < j:
#             nums[i], nums[j] = nums[j], nums[i]

#     # Place pivot in the correct position
#     nums[low], nums[j] = nums[j], nums[low]
#     return j


# # Example usage
# quick_sort(nums, 0, len(nums) - 1)
# print("Sorted array:", nums)
# # tc-0(logn*n) best case
# # tc-0(n2) worst case
# # sc-o(n)
