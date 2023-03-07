class Node:
    def __init__(self,data):
        
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        
    def deletion_position(self,pos):
       temp=self.head.next
       prev=self.head
       for i in range(1,pos-1):
           temp=temp.next
           prev=prev.next
           prev.next=temp.next
           temp.next=None
       
       
            
    def display(self):
        if self.head is None :
            print("SLL is empty")
        else :
            temp=self.head
        while(temp):
            print(temp.data,"==>",end=" ")
            temp=temp.next
obj=SLL()
n=Node(100)
obj.head=n
n1=Node(200)
n.next=n1
n2=Node(300)
n1.next=n2
n3=Node(400)
n2.next=n3
n4=Node(500)
n3.next=n4
obj.display()
print("")
obj.deletion_position(3)
obj.display()
