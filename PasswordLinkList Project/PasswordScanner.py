import re

class Node(object):
    item = -1
    count = 1
    next = None
    prev = None

    def __init__(self, item):
        self.item = item

class LinkList():
    head = None
    tail = None
    size = 0

    def checkDuplicates(self, node):
        temp = self.head
        while(temp != None):
            if temp.item == node.item:
                return temp
            temp = temp.next
        return None 

    def addNode(self, node):
        #First Element
        if self.head == None:
            self.head = node
            self.tail = node
        else:
        #We are going to check if that element is already in the LinkList
            n = self.checkDuplicates(node)
            if n is not None:
                n.count += 1
            else:
                t = self.head
                node.next = t
                t.prev = node
                self.head = node
                self.size += 1
    def printL(self):
        t = self.head
        while t != None:
            print("Password: ", t.item, "Count: ", t.count)
            t = t.next
    
    def bubbleSort(self):
        print("Bubble sorting")
        for i in range(self.size):
            #print("pass:", i)
            t0 = self.head
            t1 = t0.next
            while t1 != None:
                if t0.count < t1.count:
                   t0, t1 = self.swap(t0, t1)
                t0 = t0.next
                t1 = t1.next
    
    def swap(self, n0, n1):
        n0.next = n1.next
        if n1.next != None:
            n1.next.prev = n0
        else:
            self.tail = n0
        n1.next = n0
        n1.prev = n0.prev
        n0.prev = n1
        if n1.prev != None:
            n1.prev.next = n1
        else:
            self.head = n1
        return n1, n0
    
    def mergeSort(self, l = head, r = tail):
        if l == r:
            return l
        m = self.findMiddle(l, r)
        left = self.mergeSort(l, m)
        right = self.mergeSort(m.next, r)
        print(left, right)
        sortedL = self.merge(left, right)
        return sortedL

    def merge(self, n0, n1):
        if n0 is None:
            return n1
        if n1 is None:
            return n0
        if n0.count < n1.count:
            n1.next = n0
            n0.prev = n1
            return n1
        else:
            n0.next = n1
            n1.prev = n0
            return n0
        
    def findMiddle(self, n0, n1):
        t0 = n0
        m = t0
        s = 0
        while(t0 != n1):
            t0 = t0.next
            s += 1
        mIndex = s // 2
        for i in range(int(mIndex)):
            m = m.next
        return m   

def solA():
    linkList = LinkList()
    file = open("PasswordsEx.txt", "r")
    i = 0
    for line in file:
        #We are only intereseted in the passwords, we are going to split username and item
        l = line.split()
        if(len(l)>1):
            i += 1
            node = Node(l[1])
            #print("Adding :", node.item, " ",i )
            linkList.addNode(node)
    linkList.bubbleSort()
    linkList.printL()
    print ("="*30)
    print("20 Most Popular Passwords")
    getPasswords(linkList, 20)

def solB():
    dic = dict()
    file = open("PasswordsEx.txt", "r")
    for line in file:
        l = line.split()
        if(len(l)>1):
            item  = l[1]
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 0
    for k,v in dic.items():
        print("Password: ", k, "Count:", v+1 )

def getPasswords(l, max):
    t = l.head
    for i in range(max):
        if(t == None):
            break
        print(i, t.item)
        t = t.next

solB()

