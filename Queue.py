__Author__ = 'Anupam Panwar'

__Created_On__ = 10 / 22 / 2016

class Queue:
	    def __init__(self):
	        self.items = []

	    def isEmpty(self):
	        return self.items == []

	    def enqueue(self, item):
	        self.items.insert(0,item)

	    def dequeue(self):
	        return self.items.pop()

	    def size(self):
	        return len(self.items)

q=Queue()

q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)

for i in range(len(q.items)):
    print (q.dequeue())