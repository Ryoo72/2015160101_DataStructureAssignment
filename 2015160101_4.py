#original auther : Ryoo Kwangrok_ kwangrok21@naver.com 2015160101 Dept. of Physics
import os

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []

class Node:
    def __init__(self, newval,newcol):
        self.val = newval
        self.left = None
        self.right = None
        self.color = newcol
        self.p = None

class RedBlackTree:
    def __init__(self):
        self.nil = Node(None,"BLACK")
        self.root = self.nil
#사용자정의변수
        self.noData = []
        self.insertAmount = 0
        self.deleteAmount = 0
        self.nodeAmount = 0
        self.bnodeAmount = 0
        self.Temp_bheight = 0
        self.max_bheight = 1
        self.bh = 0
        self.itertest = 1

    def RBinsert(self,tree,n):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if n.val < x.val:
                x = x.left
            else:
                x = x.right
        n.p = y
        if y == self.nil:
            self.root = n
        elif n.val < y.val:
            y.left = n
        else:
            y.right = n
        n.left = self.nil
        n.right = self.nil
        n.color = "RED"
        self.insertFixup(self.root,n)

    def insertFixup(self,tree,n):
        while n.p.color == "RED":
            if n.p == n.p.p.left:
                y = n.p.p.right
                if y.color == "RED":
                    n.p.color = "BLACK"
                    y.color = "BLACK"
                    n.p.p.color = "RED"
                    n = n.p.p

                elif n == n.p.right:
                    n = n.p
                    self.leftRotate(tree,n)
                else:
                    n.p.color = "BLACK"
                    n.p.p.color = "RED"
                    self.rightRotate(tree,n.p.p)
            else:
                y = n.p.p.left
                if y.color == "RED":
                    n.p.color = "BLACK"
                    y.color = "BLACK"
                    n.p.p.color = "RED"
                    n = n.p.p
                elif n == n.p.left:
                    n = n.p
                    self.rightRotate(tree,n)
                else:
                    n.p.color = "BLACK"
                    n.p.p.color = "RED"
                    self.leftRotate(tree,n.p.p)
        self.root.color = "BLACK"

    def leftRotate(self,tree,x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def rightRotate(self,tree,y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.p = y
        x.p = y.p
        if y.p == self.nil:
            self.root = x
        elif y == y.p.right:
            y.p.right = x
        else:
            y.p.left = x
        x.right = y
        y.p = x

    def print(self,tree,level):
        if tree.right != self.nil:
            self.print(tree.right,level + 1)
        for i in range(level):
            print('   ', end='')
        print(tree.val,tree.color)
        if tree.left != self.nil:
            self.print(tree.left, level + 1)

    def RBprint(self,tree,level):
        if tree.right != self.nil:
            self.RBprint(tree.right,level + 1)
        for i in range(level):
            print('   ', end='')
        if tree.color == "RED":
            print("R")
        else:
            print("B")
        if tree.left != self.nil:
            self.RBprint(tree.left, level + 1)

    def RBtransplant(self,tree,u,v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p
    def RBdelete2(self,tree,z):
        z = self.search(tree, z)
        y = z
        y_original_color=y.color
        if z.left ==self.nil:
            x=z.right
            self.RBtransplant(tree,z,z.right)
        elif z.right == self.nil:
            x = z.left
            self.RBtransplant(tree,z,z.right)
        else:
            y = self.minimum(x.right)
            y_original_color = y.color
            x=y.right
            if y.p==z:
                x.p=y
            else:
                self.RBtransplant(tree,y,y.right)
                y.right = z.right
                y.right.p=y
            self.RBtransplant(tree,z,y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == "BLACK":
           self.RBdeleteFixup(tree,x)


    def RBdelete(self,tree,i):
        z = self.search(self.root,i)
        if z == self.root and z.left == self.nil and z.right == self.nil:
            self.root = self.nil
        if z == self.nil:
            self.noData.append(i)
        else:#original source
            self.deleteAmount+=1
            self.nodeAmount-=1
            y = z
            y_original_color = y.color
            if z.left == self.nil:
                x = z.right
                self.RBtransplant(tree,z,z.right)
            elif z.right == self.nil:
                x = z.left
                self.RBtransplant(tree,z,z.left)
            else:
                y = self.minimum(z.right)
                y_original_color = y.color
                x = y.right
                if y.p == z:
                    x.p = y
                else:
                    self.RBtransplant(tree,y,y.right)
                    y.right = z.right
                    y.right.p = y
                self.RBtransplant(tree,z,y)
                y.left = z.left
                y.left.p = y
                y.color = z.color
                if z.p == self.nil:
                    tree = y
            if y_original_color == "BLACK":
                self.RBdeleteFixup(tree,x)

    def minimum(self,x):
        while x.left != self.nil:
            x=x.left
        return x

    def RBdeleteFixup(self,tree,x):
        while x != self.root and x.color == "BLACK":
            if x == x.p.left:
                w = x.p.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.p.color = "RED"
                    self.leftRotate(tree,x.p)
                    w = x.p.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.p
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.rightRotate(tree,w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = "BLACK"
                    w.right.color = "BLACK"
                    self.leftRotate(tree,x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == "RED":#의문의 에러 지점_
                    w.color = "BLACK"
                    x.p.color = "RED"
                    self.rightRotate(tree,x.p)
                    w = x.p.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.p
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.leftRotate(tree,w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = "BLACK"
                    w.left.color = "BLACK"
                    self.rightRotate(tree,x.p)
                    x = self.root
        x.color = "BLACK"

    def search(self,x,k):
        if x == self.nil:
            return self.nil
        elif k == x.val:
            return x
        if k < x.val:
            return self.search(x.left,k)
        else:
            return self.search(x.right,k)

    def Input(self,val):
        if val > 0:#insert
            self.nodeAmount+=1
            self.insertAmount+=1
            self.RBinsert(self.root, Node(val,"RED"))
            #print("insert",val)
        elif val < 0:#delete
            self.RBdelete(self.root, -1 * val)
        else:#case of 0 exit the program
            print("else?")
            pass

    def inorder(self,tree):

        if tree == self.nil:
            if tree.p != None:
                if tree.p.color == "BLACK":#흑인 부모일경우
                    self.Temp_bheight-=1
            return
        else:
            if tree.color == "BLACK":#bnodeAmount 세기
                self.bnodeAmount+=1
            #딸네로 갈거임
            if tree.left.color == "BLACK":#흑인 딸일경우
                self.Temp_bheight+=1
                if self.max_bheight < self.Temp_bheight:
                    self.max_bheight=self.Temp_bheight
            self.inorder(tree.left)#    let's go to 딸
            #딸네 갔다가 내 집으로 돌아옴

            #**********내집*************
            #print(tree.val, end=' ')#   Me
            #**************************

            #아들네로 갈거임
            if tree.right.color == "BLACK":#흑인 아들일경우
                self.Temp_bheight+=1
                if self.max_bheight < self.Temp_bheight:
                    self.max_bheight=self.Temp_bheight
            self.inorder(tree.right)#   let's go to 아들
            #아들네 갔다가 내 집으로 돌아옴

            #**********내집*************

            #**************************

    def printInorder(self,tree):
        if tree == self.nil:
            return
        else:
            self.printInorder(tree.left)
            print(tree.val)
            self.printInorder(tree.right)

    def blackheight(self,tree):
        if tree == self.nil:
            print("bh = 1")
        else:
            bnode = tree
            while self.itertest == 1:
                if bnode.color == "BLACK":
                    self.bh+=1
                if bnode.left == self.nil:
                    print("bh =",self.bh)
                    self.itertest = 0
                else:
                    bnode = bnode.left


def main():
    rbt = RedBlackTree()
    f = open("input.txt", 'r')
    lines = f.readlines()
    for line in lines:
        number=int(line)
        if number != 0:
            rbt.Input(number)
        else:
            break
    f.close()
    #rbt.print(rbt.root,0)
    rbt.inorder(rbt.root)

    print("삭제되지 못한 입력 값 = ",rbt.noData)
    print("total = ",rbt.nodeAmount)
    print("nb = ",rbt.bnodeAmount)
    rbt.blackheight(rbt.root)
    rbt.printInorder(rbt.root)
    #rbt.inorder_iter(rbt.root)

if __name__ == '__main__':
    main()
