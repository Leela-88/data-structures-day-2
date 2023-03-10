#Single Linked List
class Node:
    def __init__(self,data):
        
        self.data=data
        self.next=None
class SLL:
    
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None :
            print("SLL is empty")
        else :
            temp=self.head
        while(temp):
            print(temp.data,"==>",end=" ")
            temp=temp.next
obj=SLL()
n1=Node(100)     # here n1 is the address of 100  
obj.head=n1      #here we are pointng the head to the node 1
n2=Node(200)      #here n2 contains  the next part(i.e  address ) of 200
obj.head.next=n2    # here we are creating link btw node1 and node2  # or we can write it as n1.next=n2
n3=Node(300)
obj.head.next.next=n3  #or (obj.head.next=n2) so we can write it as (n2.next=n3)
print(obj.display())
