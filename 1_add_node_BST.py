class BST:

    def __init__(self,data):
        self.lchild = None
        self.rchild = None
        self.data = data

    def add_node(self,n):
        #if Root is Empty
        if self.data is None:
            self.data = n
            return
        #if Duplicated
        if self.data == n:
            return
        #if given n is less than the Root node
        if self.data > n:
            if self.lchild:
                self.lchild.add_node(n)
            else:
                self.lchild = BST(n)

        else:
            if self.rchild:
                self.rchild.add_node(n)
            else:
                self.rchild = BST(n)
root = BST(10)
l = [20,4,30,4,1,5,6]
for i in l:
    root.add_node(i)
print("Root Node:",root.data)
print("Left Child:",root.lchild.data)
print("Right Child:",root.rchild.data)
