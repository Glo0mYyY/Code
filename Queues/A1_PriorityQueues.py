class PriorityQueue:
    def __init__(self):
        self.liste = []

    def is_Empty(self):
        return len(self.liste) == 0

    def enqueue(self, priority, value):
        element = priority, value
        self.liste.append(element)

    def dequeue(self):
        if not self.is_Empty():
            self.liste.sort()
            return self.liste.pop(-1)
        return None

    def peek(self):
        if not self.is_Empty():
            self.liste.sort()
            return self.liste[-1]
        return None

    def size(self):
        return len(self.liste)


queue = PriorityQueue()
queue.enqueue(3, "Jan")
queue.enqueue(1, "Peter")
queue.enqueue(2, "Kevin")
queue.enqueue(5, "John")

print(queue.is_Empty())
print(queue.peek())
print(queue.dequeue())
print(queue.size())
print(queue.peek())