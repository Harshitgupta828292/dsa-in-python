# -----------------------0(n)---------------------------------
    
# def get_square_number(number):
    
#     square_number=[]
#     for n in number:
#         square_number.append(n*n)
#     return square_number
# number=[2,3,8,9,6]
# print(get_square_number(number))
# -----------------------------------------0(1)------------------------
# def find_first_pr(index,eps,prices):
#     pr=prices[index]/eps[index]
#     return pr
# index=1
# eps=[10,23,46]
# prices=[2,5,56]
# print(find_first_pr(index,eps,prices))

# ---------------------------------------0(n2)-------------------------------


# number=[3,6,2,4,3,6,8,9,9]
# for i in range(len(number)):
    
#     for j in range(i,len(number)):
#         if number[i]==number[j]:
#             print("duplicate are",number[i])
#             break


# number=[3,6,2,7,3,6,7,9]
# duplicate=None
# for i in range(len(number)):
#     for j in range(i+1,len(number)):
#         if number[i]==number[j]:
#             duplicate=number[i]
#             # print(i)
#             break
# for i in range(len(number)):
#     if number[i]==duplicate:
#         print(i)

# 1-




# -------------------------------------LINKED LIST------------------
class Node:
    def __init__(self,data=None,next=None):
        # self,data,next is the it is the function when created the object
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.hand=None
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        itr=self.head
        llstr=''
        while itr:
            suffix=''
            if itr.next:
               suffix='-->'
            llstr +=str(itr.data) + suffix
            itr=itr.next
        print(llstr)
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count +=1
            itr=itr.next
        return count
if __name__=='__main__':
    root=LinkedList()
    root.insert_at_begining(5)
    root.insert_at_begining(10)
    root.insert_at_begining(15)
    print(root.get_length())