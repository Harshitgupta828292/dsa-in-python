# # # # # n=5873
# # # # #
# # # # # num=n
# # # # # while num>0:
# # # # #    last_digit=num%10
# # # # #    print(last_digit)
# # # # #    num=num//10
# # # # n=5873
# # # # num=str(n)[::-1]
# # # #
# # # # print(num)
# # # # palindrome number
# # # n=121
# # # num=n
# # # result=0
# # # while num>0:
# # #     last_digit=num%10
# # #     result=result*10+last_digit
# # #     print(result)
# # #
# # #     num=num//10
# # # if n==result:
# # #     print("palidrome")
# # # else:
# # #     print("not palidrome")
# # #
# # # palidrome ki line
# # def is_palidrome(n):
# #     return str(n)==str(n)[::-1]
# # start=1
# # end=101
# # print(start,"and",end)
# # for num in range(start,end+1):
# #     if is_palidrome(num):
# #         print(num)
# # --------------------length---------
# count=0
# n=65675
# num=n
# while num>0:
#     count+=1
#     num=num//10
# print(count)
n = int(input())
students = []

for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

# scores list
scores = [s[1] for s in students]

# lowest score
min_score = min(scores)

# second lowest score (without set or sort)
second_lowest = float('inf')
for s in scores:
    if min_score < s < second_lowest:
        second_lowest = s

# print names with second lowest score, alphabetically
for name in sorted([s[0] for s in students if s[1] == second_lowest]):
    print(name)
