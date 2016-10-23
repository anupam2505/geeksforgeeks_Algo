__Author__ = 'Anupam Panwar'

__Created_On__ = 10 / 22 / 2016

from removedup_LinkedList import Node, LinkedList

linkedlist = LinkedList()
linkedlist.insert("Anupam")
linkedlist.insert("Panwar")
linkedlist.insert("Anupam")
linkedlist.insert("3")
linkedlist.insert("4")

def nthelementfromLast (linkedlist, n):
    current = linkedlist.head
    i=1
    while (i!=n) and current:
        current = current.get_next()
        i+=1
    print current.get_data()


nthelementfromLast(linkedlist,2)