class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LL(object):
    def __init__(self):
       self.head = None
       
    def Insert_First(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def Insert_After(self,prev,data):
        new_node = Node(data)
        temp = self.head
        while(temp.next):
            if (prev.data == temp.data):
                new_node.next = prev.next
                prev.next = new_node
                break
            temp = temp.next
            
    def Insert_Last(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
            new_node.next = None
    
    
    def Print(self):
        temp = self.head
        while(temp):
            print(temp.data,end = " ")
            temp = temp.next
        
        
    def Delete_Node(self,key):
        temp = self.head
        if key == temp.data:
            self.head = temp.next
            return self.head
        else:
            while(temp):
                if key == temp.data:
                    break
                prev = temp
                temp = temp.next
            prev.next = temp.next
            
    def Get_Nth_Node(self,index):
         temp = self.head
         count = 0
         while(temp):
             if index == count:
                 print(temp.data)
                 break
             count +=1
             temp = temp.next
         
    def Get_Middle_Node(self):
         temp = self.head
         count = 0
         while(temp):
             count +=1
             temp = temp.next
         mid = count//2
         self.Get_Nth_Node(mid-1)
             
    
        

    
l = LL()
l.Insert_First(30)
l.Insert_First(10)
l.Insert_After(l.head,20)
l.Insert_Last(40)
l.Insert_Last(50)
l.Insert_Last(60)

print("List after insertion")
l.Print()
print("\n\nThe Middle element is")
l.Get_Middle_Node()
print("\nThe nth node is")
l.Get_Nth_Node(3)
print("\nList after deletion")
l.Delete_Node(60)
l.Print()
