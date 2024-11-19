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


    def search(self,n,c=0):
        if self.data == n:
            print("Node Found...! at position {}".format(c))
            return
        if self.data > n:
            if self.lchild:
                self.lchild.search(n,c+1)
            else:
                print("Node Not Found....!")
        else:
            if self.data > n:
                self.lchild.search(n,c+1)
            else:
                print("Node Not Found....!")

    def pre_order(self):
        print(self.data,' ',end=" ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()

    def in_order(self):

        if self.lchild:
            self.lchild.pre_order()
            print(self.data, ' ', end=" ")
        if self.rchild:
            self.rchild.pre_order()

    def post_order(self):
        if self.lchild:
            self.lchild.post_order()

        if self.rchild:
            self.rchild.post_order()
        print(self.data, ' ', end=" ")


root = BST(21)
l = [10,30,5,12,25,100,3,7]
for i in l:
    root.add_node(i)
print("Root Node:",root.data)
print("Left Child:",root.lchild.data)
print("Right Child:",root.rchild.data)

root.search(1)
print("Pre Order..")
root.pre_order()
print()
print("In Order...")
root.in_order()
print()
print("Post Order...")
root.post_order()
