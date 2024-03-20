class stack:
    def __init__(self):
        self.liste = []

    def is_Empty(self):
        return len(self.liste) == 0

    def enqueue(self, element):
        self.liste.append(element)

    def dequeue(self):
        if not self.is_Empty():
            return self.liste.pop(-1)
        return None

    def peek(self):
        if not self.is_Empty():
            return self.liste[-1]
        return None

    def size(self):
        return len(self.liste)


queue = stack()
queue.enqueue(2)
queue.enqueue(1)
queue.enqueue(3)

print(queue.is_Empty())
print(queue.dequeue())  # Liefert 3 zurück
print(queue.dequeue())  # Liefert 1 zurück
print(queue.peek())  # Liefert 2 zurück
print(queue.dequeue())  # Liefert 2 zurück
print(queue.size())  # Liefert 0 zurück
