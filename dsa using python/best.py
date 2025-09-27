# # # lecture 37
# # price=[8,2,1,5,6,4]
# # n=len(price)
# # max_profit=0
# # for i in range(0,n):
    
# #     for j in range(i+1,n):
# #         if price[j]>price[i]:
# #             p=price[j]-price[i]
# #             max_profit=max(max_profit,p)
# # print(max_profit)
# # -------------------------------
# price=[7,2,1,5,6,4,8]
# max_profit=0
# min_price=float("inf")
# n=len(price)
# for i in range(0,n):
#     min_price=min(min_price,price[i])
#     max_profit=max(max_profit,price[i]-min_price)
# print(max_profit)
# tc-0n
# sc-01