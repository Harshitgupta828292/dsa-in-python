
# n=[5,3,2,2,1,5,5,7,5,10]
# m=[10,111,1,9,5,67,2]
# hash_list=[0]*11
# for num in n :
#     hash_list[num]+=1
# for num in  m:
#     if num<1 or num>10:
#         print(0)
#     else:
#         print(hash_list[num])
        
        # ----------------------------------------------METHOD 2-----------------------------------------
n=[5,4,3,3,2,2,22,234,4,5]
m=[5,4,6,7,8,56,4,3,3]
hash_map={}
for i in range(0,len(n)):
    if n[i] in hash_map:
        hash_map[n[i]]=+1
    else:
        hash_map[n[i]]=1
for x in m:
    print(hash_map.get(x,0))