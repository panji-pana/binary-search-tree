import random

class Node():
    def __init__(self,data,left=None,right=None) -> None:
        self.data = data
        self.left = left
        self.right = right



class Tree():

    def __init__(self) -> None:
        self.tree = []

   
    # Traversals
   
    def preTraverse(self,node=0) -> None:
        print(self.tree[node].data)
        if self.tree[node].left != None:
            self.preTraverse(self.tree[node].left)
        if self.tree[node].right != None:
            self.preTraverse(self.tree[node].right)

    
    def inTraverse(self,node=0) -> None:
        if self.tree[node].left != None:
            self.inTraverse(self.tree[node].left)
        print(self.tree[node].data)
        if self.tree[node].right != None:
            self.inTraverse(self.tree[node].right)

   
    def postTraverse(self,node=0) -> None:
        if self.tree[node].left != None:
            self.postTraverse(self.tree[node].left)
        if self.tree[node].right != None:
            self.postTraverse(self.tree[node].right)
        print(self.tree[node].data)

    
    # Insertion

    def insert(self,entry:int,current=0)->int:
        try:
            if (entry < self.tree[current].data):
                if (self.tree[current].left != None):
                    self.insert(entry, self.tree[current].left)
                else:
                    self.tree[current].left = len(self.tree)
            
            else:
                if (self.tree[current].right != None):
                    self.insert(entry, self.tree[current].right)
                else:
                    self.tree[current].right = len(self.tree)
        
        except IndexError:   # in the case where a tree is empty
            pass    

        self.tree+=[Node(entry)]
        return entry



def main():

    ex = Tree()

    print("---------------------Entries---------------------")
    for i in range(10):
        print(ex.insert(random.randint(1,100)))
    print("---------------------Pre Order---------------------")
    ex.preTraverse()
    print("---------------------In Order---------------------")
    ex.inTraverse()
    print("---------------------Post Order---------------------")
    ex.postTraverse()
    print("-------------------------------------------")

if __name__ == "__main__":
    main()