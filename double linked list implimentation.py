class Node:
    def __init__(self,data):
        
        self.data=data
        self.previous=None
        self.next=None
class DLL:
    
    def __init__(self):
        self.head=None
        self.previous=None
                                                     
            
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
obj.display()

