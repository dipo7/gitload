from timeit import default_timer

# def maxNum(x):
#     biggest = x[0]
#     for i in x:
#         if i > biggest:
#             biggest = i
#     return biggest

# start = default_timer()
# maxNum([i for i in range(1,101)])
# end = default_timer()
# print('function took %0.3f ms' % ((end-start)*1000.0))

# def findNum(x, y):
#     if x not in y:
#         return ('Not found')
#     for idx, elem in enumerate(y):
#         if elem == x:
#             return (idx, elem)
#     # return elem
# start = default_timer()
# x = findNum(20000, [i for i in range(1,20001)])
# end = default_timer()
# print(x)
# print('function took %0.3f ms' % ((end-start)*1000.0))



def bin_search(item, itemlist):
    startpt = 0
    endpt = len(itemlist)-1
    found = False
    while (startpt <= endpt and not found):
        midpt = (startpt + endpt)//2
        print(midpt)
        if midpt == item:
            found = True
        else:
            if midpt > item:
                endpt = midpt - 1
            else:
                startpt = midpt + 1
    return found

start = default_timer()
print (bin_search(444, range(1,1001)))
end = default_timer()
print('function took %0.3f ms' % ((end-start)*1000.0))








# class Linkedlist():
#     def __init__(self, d, nextNode=None):
#         self.d = d
#         self.nextNode = nextNode

# node1 = Linkedlist(3)
# node2 = Linkedlist(7)
# node3 = Linkedlist(10)
# node4 = Linkedlist(17)

# node1.nextNode = node2
# node2.nextNode = node3
# node3.nextNode = node4

# curNode = node1

# while True:
#     print(curNode.d,'-->',)
#     if curNode.nextNode is None:
#         print('None')
#         break
#     curNode = curNode.nextNode


# class LinkedListNode():
#     def __init__(self, d, nextNode=None):
#         self.d = d
#         self.nextNode = nextNode

# class linkedlist():
#     def __init__(self, head=None):
#         self.head = head

#     def insert(self, value):
#         node = LinkedListNode(value)
#         if self.head is None:
#             self.head = node
#             return

#         curNode = self.head
#         while True:
#             if curNode.nextNode is None:
#                 curNode.nextNode = node
#                 break
#             curNode = curNode.nextNode

#     def printLinkedList(self):
#         curNode = self.head
#         while curNode is not None:
#             print(curNode.d,'--> ',end="")
#             curNode = curNode.nextNode
#         print('None')

#     def countNode(self):
#         total = 0
#         curNode = self.head
#         while curNode is not None:
#             total += 1
#             curNode = curNode.nextNode
#         print(total)


# ll = linkedlist()
# ll.printLinkedList()
# ll.insert(4)
# ll.printLinkedList()
# ll.insert(7)
# ll.printLinkedList()
# ll.insert(5)
# ll.printLinkedList()
# ll.insert(1)
# ll.printLinkedList()
# ll.insert(144)
# ll.printLinkedList()
# ll.countNode()