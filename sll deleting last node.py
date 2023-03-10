class Node:
    def __init__(self,data):
        
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        
    def deletion_end(self):
        temp=self.head.next  
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None   #last but before node's next  is deleted so it results in the deltion of last nod
   
            
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
print("before deletion")
obj.display()
print("")
print("after deletion")
obj.deletion_end()
obj.display()

