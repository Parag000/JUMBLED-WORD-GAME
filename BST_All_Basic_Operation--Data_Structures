import random
class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root,data)
    
    def _insert(self,cur,data):
        if data < cur.data:
            if cur.left is None:
                cur.left = Node(data)
            else:
                self._insert(cur.left,data)
        else:
            if cur.right is None:
                cur.right = Node(data)
            else:
                self._insert(cur.right,data)
    
    def inorder(self):
        stack = []
        cur = self.root
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                print(cur.data,end = " ")
                cur = cur.right
            else:
                break
     
    def search(self,key):
        if self.root is None:
            print("Not Present")
        else:
            self._search(self.root,key)
    
    def _search(self,cur,key):
        if key < cur.data and cur.left is not None:
            self._search(cur.left,key)
        elif key > cur.data and cur.right:
            self._search(cur.right,key)
        if key == cur.data:
            print("Found",cur.data)
     
    def MinVal(self,node):
        cur = node
        while(cur.left is not None):
            cur = cur.left
        return cur    
    
    def delete(self,key):
        if self.root is None:
            return self.root
        else:
            self._delete(self.root,key)
                 
    def _delete(self,cur,key):
        if key < cur.data:
            cur.left = self._delete(cur.left,key)
        elif key > cur.data:
            cur.right = self._delete(cur.right,key)
        else:
            if cur.left is None:
                temp = cur.right
                cur = None
                return temp
            else:
                temp = cur.left  
                cur = None
                return temp 
        
            temp = self.MinVal(cur.right)
            cur.data = temp.data
            cur.right = self._delete(cur.right,temp.data)
        return cur     
    
    def preorder(self):
        stack=[]
        stack.append(self.root)
        while(stack):
            curr = stack.pop()
            print(curr.data)
            if curr.right:
                stack.append(curr.right)
            else:
                stack.append(curr.left)
    
bst = BST()
for i in range(1,20):
    r = random.randint(1,20)
    bst.insert(r)                

bst.inorder()
