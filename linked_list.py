class Node:
     def __init__(self):
          self.data = None
          self.next = None

class LinkedList:
     def __init__(self):
          self.head = None
     
     def insert(self, data):
          node = Node()
          node.data = data
          node.next = self.head
          self.head = node

     def reverse(self):
        current = self.head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

     def __iter__(self):
          node = self.head
          while node:
               yield node.data
               node = node.next

     def swap(self): # iterative
          previous = Node()
          previous.next = self.head
          temp = previous
          
          while temp.next and temp.next.next:
               ptrOne = temp.next
               ptrTwo = temp.next.next

               # change the pointers to the swapped pointers
               temp.next = ptrTwo
               ptrOne.next = ptrTwo.next
               ptrTwo.next = ptrOne
               temp = temp.next.next
          self.head = previous.next

linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)

print ("Original list   : {}".format([ data for data in linked_list ]))
linked_list.reverse()
print ("Reversed list   : {}".format([ data for data in linked_list ]))
linked_list.swap()
print ("Swap Pair list  : {}".format([ data for data in linked_list ]))