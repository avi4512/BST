from pickle import PROTO


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


        def search(self, n, c=0):
        if self.data == n:
            print("Node Found...! at position {}".format(c))
            return True
        elif n < self.data:
            if self.lchild:
                return self.lchild.search(n, c + 1)
            else:
                print("Node Not Found....!")
                return False
        else:  # n > self.data
            if self.rchild:
                return self.rchild.search(n, c + 1)
            else:
                print("Node Not Found....!")
                return False
    

root = BST(10)
l = [20,4,30,4,1,5,6]
for i in l:
    root.add_node(i)
print("Root Node:",root.data)
print("Left Child:",root.lchild.data)
print("Right Child:",root.rchild.data)

root.search(1)
