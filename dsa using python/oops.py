# # # def main():
# # #     name=input("name")
# # #     study=input("class")
# # #     get_value(name,study)
# # # def get_value(name,study):
# # #     print(f"{name}and it {study}")
# # # if __name__=="__main__":
# # #     main()
    
    
# # # def main():
# # #     name=get_value()
# # #     classes=get_class()
# # #     print(f"{name} from {classes}")
# # # def get_value():
# # #     return input("name")
# # # def get_class():
    
# # #      return input("classes")
# # # if __name__=="__main__":
# # #      main()

# # # def main():
# # #     name,house=get_student()
# # #     print(f"{name} from a{house} ")
# # # def get_student():
# # #     name=input("enter")
# # #     house=input("enter")
# # #     return name,house
# # # if __name__=="__main__":
# # #     main()



# # # def main():
# # #     student=get_student()
# # #     print(f"{student[0]} from {student[1]}")
# # # def get_student():
# # #     name=input("name")
# # #     house=input("house")
# # #     return(name,house)
# # # if __name__=="__main__":
# # #     main()
# # # def main():
# # #     student=get_student()
# # #     if student[0]=="padma":
# # #         student[1]=="ravincrow"
# # #         print(f"{student[0]}from {student[1]}")
# # # def get_student():
# # #     name=input("name")
# # #     house=input("house")
# # #     return [name,house]
# # # if __name__=="__main__":
# # #     main()


# # # def main(): 
# # #     student=get_student()
# # #     print(f"{student['name']} from {student['house']}")
# # # def get_student():
# # #     student={}
# # #     student["name"]=input("name")
# # #     student["house"]=input("house")
# # #     return student
# # # if __name__=="__main__":
# # #     main()
        
# # # def main():
# # #     name=get_name()
# # #     house=get_house()
# # #     print(f"my name is {name} and my house is {house}")
# # # def get_name():
# # #     name=input("enter the name")
# # #     return name
# # # def get_house():
# # #     house=input("enter the house")
# # #     return house

# # # main()
# # def main ():
# #     student=get_student()
# #     if student[0]=="padma":
# #         student[1]="ravencrow"
# #     print(f"{student[0]} from{student[1]} ")
# # def get_student():
# #     name=input("enter the name of the student")
# #     house=input("enter the house of the student")
# #     return name,house
# # if __name__=="__main__":
# #     main()

# # def main ():
# #     student=get_student()
# #     if student[0]=="padma":
# #         student[1]="ravencrow"
# #     print(f"{student[0]}from {student[1]}")
# # def get_student():
# #     name=input("name")
# #     house=input("house")
# #     return [name,house]
# # if __name__=="__main__":
# #     main()
# def main():
#     student=get_student()
#     if student["name"]=="padma":
#         student['house']="killer"
#     print(f"{student['name']} from {student['house']}")
# def get_student():
    
#     name=input("name")
#     house=input("house")
#     return {"name":name,"house":house}
# if __name__=="__main__":
#     main()

# ---------------------------------------------------------------------------------------------
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
# my object

    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
       n=Node(data)  
    #    do not assign next because  next value is none 
       if not self.is_empty():
           temp=self.start
        #    temp se hum traversing 
           while temp.next is not None:
               temp=temp.next
           temp.next=n
       else:
            self.start=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None :
            n=Node(data,temp.next)
            temp.next=n
            # jodh diya 
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):
        return SLLIterator(self.start)
        # iski bajah se 1 class iterable hogi
class SLLIterator:
    def __init__(self,start):
        # not linked list start 
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next                        
        return data
                
        
        # new node
        
mylist=SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()
mylist.delete_item(30)
print()



for x in mylist:
    # kuch data type pehle se iterable hote h 
    print(x,end=' ')
print()

        
