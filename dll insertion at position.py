class Node:
    def __init__(self,data):
        
        self.data=data
        self.previous=None
        self.next=None
class DLL:
    
    def __init__(self):
        self.head=None
        self.previous=None  #i 
    def insert_pos(self,pos):
        n=Node(500)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n

       
    def display(self):
        if self.head is None :
            print("DLL is empty")
        else :
            temp=self.head
        while(temp):
            print(temp.data,"<==>",end=" ")
            temp=temp.next
obj=DLL()
n1=Node(100)
obj.head=n1 
n2=Node(300)
n2.previous=n1
n1.next=n2
n3=Node(400)
n3.previous=n2
n2.next=n3
n4=Node(600)
n4.previous=n3
n3.next=n4
print("before insertion")
obj.display()
print("")
print("after  insertion")
obj.insert_pos(3)
obj.display()
